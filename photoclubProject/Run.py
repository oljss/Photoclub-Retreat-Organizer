"""
Oliver Scott
Spring 2020
~retreat easymaker whoop whoop~
Copyright USC Photoclub
"""

from SignUps import SignUps
from SheetInfo import Sheets
from Members import Member
from Lists import Lists
import pprint
import string
#from Lists import Lists
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Google import Create_Service
from tkinter import *

root = Tk()
root.title("Retreat Signup Helper")
titleLabel = Label(root, text="Photoclub")
titleLabel.grid(row=0)


entry_total = Entry(root)
entry_waitlist = Entry(root)
entry_drivers = Entry(root)
entry_memFile = Entry(root)
entry_responseForm = Entry(root)
entry_signups = Entry(root)

label_total = Label(root, text="How many people? (int):")
label_waitlist = Label(root,text="How many people on the waitlist? (int):")
label_drivers = Label(root, text="How many Drivers? (int):")
label_memFile = Label(root, text="Name of member file:")
label_signups = Label(root, text="Name of Google Sheet:")
label_responseForm = Label(root, text="Name of Response Sheet:")

label_total.grid(row=1)
entry_total.grid(row=1, column=1)
label_waitlist.grid(row=2)
entry_waitlist.grid(row=2, column=1)
label_drivers.grid(row=3)
entry_drivers.grid(row=3, column=1)
label_memFile.grid(row=4)
entry_memFile.grid(row=4, column=1)
label_signups.grid(row=5)
entry_signups.grid(row=5, column =1)
label_responseForm.grid(row=6)
entry_responseForm.grid(row=6, column =1)



"""
#README:

#TO DO: 
    #- Sorted List, Signup list and heirarchy functions can be combined
    #- Driver function needs to be fixed in Lists class
"""

"""
#API STUFF:
"""


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

"""
#API STUFF
"""


def getFileName(event):
    sheetName = entry_signups.get()
    return sheetName 
def getResponseName(event):
    responseName = entry_responseForm.get()
    return responseName          
def getMemFileName(event):
    fileName = entry_memFile.get()
    return fileName
def getNumTotalPeople(event):
    numPeople = int(entry_total.get())
    return numPeople
def getNumWaitlist(event):
    numWaitlist = int(entry_waitlist.get())
    return numWaitlist
def getNumDrivers(event):
    numWaitlist = int(entry_drivers.get())
    return numWaitlist


def signupList(SheetName):
    sheet = SheetName
    counter = 1
    signupList = []

    first_name = sheet.col_values(4) 
    last_name = sheet.col_values(5)
    venmo = sheet.col_values(14)
    email = sheet.col_values(3)
    phone = sheet.col_values(7)
    driver = sheet.col_values(9)
    time = sheet.col_values(1)
     
    for number in range(0,len(venmo)-1):
        #name lowering
        name = ''.join([first_name[counter], last_name[counter]])
        name = name.lower()
        for character in name:
            if character == " ":
                name = name.replace(character, "")

        #time input
        for numeral in time[counter]:
            if numeral.isdigit()==False:
                time[counter] = time[counter].replace(numeral, "")

        #driver input
        if driver[counter] == "No":
            driver[counter] = False
        if driver[counter] == "Yes, I have a car and I would be willing to drive on this retreat":
            driver[counter] = True
        person = SignUps(name, venmo[counter], email[counter], phone[counter], driver[counter])
        
        #time
        person.setTime(int(time[counter]))
        #memberstatus
        members = memberList()
        isPersonMember(members, person)
        signupList.append(person)
        counter += 1
    
    return signupList
        
def memberList():
        memberList = []
        memFile = open("memberList.csv", "r")
        memFile.readline()
        for line in memFile:
            line = line.strip()
            line = line.split(",")
            name = line[2].lower()
            for character in name:
                if character == " ":
                    name = name.replace(character, "")
            member = Member(name)
            member.setAttendancePoints(int(line[7]))
            memberList.append(member)
        memFile.close()

        return memberList

def isPersonMember(Memberlist, Person):
        person = Person
        for member in Memberlist:
            if person.name == member.name:
                person.setAttendancePoints(member.attendancePoints)
                person.setMember(True)

def updateSheet(ResponseSheetName, AcceptedSheet, WaitlistSheet):

    # go through second form responses, check if no or yes, if no, check email against accepted sheet. 
    #if email in accepted sheet, delete from row and add first row of waitlist
    responseSheet = client.open(ResponseSheetName).sheet1
    lists = Lists()
    responses = responseSheet.col_values(3)
    emailAccepted = AcceptedSheet.col_values(2)
    emailResponses = responseSheet.col_values(2)
    counter = 1
    lists.waitlist.reverse()
    waitlist = lists.waitlist
    #go through responses
    for response in responses:
        if response == "no":
            counter = 1
            for email in emailAccepted:
                #check dropper email in response sheet against dropper email in accepted sheet
                if email==ResponseSheet(counter, 2):
                    AcceptedSheet.delete_row(counter) #delete row of dropper in accepted list
                    person = waitlist[len(waitlistPerson-1)] #takes from waitlist in order
                    WaitlistSheet.delete_row(2) #delete first row of Waitlist sheet
                    AcceptedSheet.append_row([person.name, person.email,person.attendancePoints, person.phone, person.venmo]) #Append row of waitlist person to accepted sheet
                    waitlist.remove(person) #remove new person from the waitlist
                    for human in lists.accepted: #remove dropper from accepted list
                        if human.email == email:
                            lists.accepted.remove(human)


                counter +=1

#def sendEmail():

def sortSignUps(SignUpList):
    sortedList = []
    signups = SignUpList
    max_points = 0
    counter = 0

    
    for person in signups:
        counter+=1

    while counter>0:
        #run through list of people in Sign Up list, find most attendance points
        for human in signups:
            if human.attendancePoints>max_points:
                max_points = human.attendancePoints
                max_points_name = human.name

        #main for loop
        for person in signups:
            if person.attendancePoints == max_points:
                if person.member == 1:
                    if person.name == max_points_name:
                        sortedList.append(person)
                        signups.remove(person)
                        

            if max_points == 0:
                mem_counter = 0
                for new_person in signups:
                    if new_person.member>0:
                        mem_counter += 1
                if person.member == 1:
                    #for accepted
                    sortedList.append(person)
                    signups.remove(person)
                if person.member == 0:
                    if mem_counter == 0:
                        sortedList.append(person)
                        signups.remove(person)
        max_points = 0
        counter = counter-1
    return sortedList

def run(event): #run(event)
    "Get Sheet Name"
    sheets = Sheets("testForm", "YosemiteResponses")#all sheet info
    lists = Lists()#from Lists class

    #get input info
    total_people = getNumTotalPeople(event)
    waitlist_people = getNumWaitlist(event)
    drivers = getNumDrivers(event)

    #open sheets
    signups = signupList(sheets.originalSheet) #from sheets, enter people into the system of signups
    

    sorted_list = sortSignUps(signups) #sort all the people into priority list
    lists.heirarchy(sorted_list, drivers, total_people, waitlist_people) #puts people into their respective lists
    lists.printLists()

    sheets.createSheets()

    #updateSheet("testForm", newSheets[0], newSheets[1])

run_button = Button(root, text="Go")
run_button.grid(row=7)
run_button.bind("<Button-1>", run)
root.mainloop()

