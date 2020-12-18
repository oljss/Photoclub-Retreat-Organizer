from Inputs import Inputs
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Google import Create_Service
from Lists import Lists
class Sheets(object):
    def __init__(self, responseSheetName, originalSheetName):
        self.scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.responseSheet = self.client.open(responseSheetName).sheet1
        self.originalSheet = self.client.open(originalSheetName).sheet1
        self.sheetNames = ['Accepted', 'Waitlist', 'Overcap', 'Drivers']
        self.newSheets = []

    def createSheets():
        lists = Lists()
        for name in self.sheetNames:
            newSheet = self.ogSheetName.add_worksheet(name, 30, 30)
            self.newSheets.append(newSheet)
        
        self.newSheets[0].append_row(["Name", "Email","Attendence Points", "Phone", "Venmo"])
        self.newSheets[1].append_row(["Name", "Email","Attendence Points", "Phone", "Venmo"])
        self.newSheets[3].append_row(["Name", "Email","Attendence Points", "Phone", "Venmo"])

        for person in lists.accepted:
            newSheets[0].append_row([person.name, person.email,person.attendancePoints, person.phone, person.venmo])
        
        for person in lists.waitlist:     
            newSheets[1].append_row([person.name, person.email,person.attendancePoints, person.phone, person.venmo])

        for person in lists.drivers:
            newSheets[3].append_row([person.name, person.email,person.attendancePoints, person.phone, person.venmo])
        

    
