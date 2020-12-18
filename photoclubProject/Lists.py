from Inputs import Inputs
class Lists(object):
    def __init__(self):
        self.accepted = []
        self.waitlist = []
        self.overcap = []
        self.drivers = []

    def addToAccepted(self, Person):
        self.accepted.append(Person)
    
    def addToWaitlist(self,Person):
        self.waitlist.append(Person)

    def addToOvercap(self, Person):
        self.overcap.append(Person)
    
    def moveFromWaitlist(self, Person):
        self.accepted.remove(Person)
        self.waitlist.remove(Person)
    def heirarchy(self, SortedList, Drivers, AmtAccepted, AmtWaitlist):
        #driver function
        number_of_people_accepted = AmtAccepted
        number_of_people_waitlist = AmtWaitlist
        sortedList = SortedList
        numDrivers = Drivers
        sortedList_noDrive = []
        ogDriverList = []

        person_counter = 0
        for person in sortedList:
            if person.driver == True:
                ogDriverList.append(person)
            else:
                sortedList_noDrive.append(person)
            person_counter+=1
        counter = 0
        for person in ogDriverList:
            #still broken plz fix
            mem_counter = 0
            for new_person in ogDriverList:
                if new_person.member>0:
                    mem_counter += 1
            if counter<numDrivers:
                if person.member>0:
                    self.accepted.append(ogDriverList[counter])
                    self.drivers.append(ogDriverList[counter])
                if mem_counter<1:
                    self.accepted.append(ogDriverList[counter])
                    self.drivers.append(ogDriverList[counter])
            counter += 1

        counter = 0
        #add people to accepted
        for number in range(0, number_of_people_accepted-numDrivers):
            self.addToAccepted(sortedList_noDrive[counter])
            counter += 1
        #add people to waitlist
        for number in range(0, number_of_people_waitlist):
            self.addToWaitlist(sortedList_noDrive[counter])
            counter += 1
        
        overcap_counter = 0
        overcap_counter += counter
        #add people to overcap
        for number in range(overcap_counter, len(sortedList_noDrive)):
            self.addToOvercap(sortedList_noDrive[counter])
            counter += 1
           
    def printLists(self):
        print("---Accepted---")
        for person in self.accepted:
            print(person.name, ":", str(person.attendancePoints))
        print()
        
        print("---Waitlist---")
        for person in self.waitlist:
            print(person.name, ":", str(person.attendancePoints))
        print()

        print("---Overcap---")
        for person in self.overcap:
            print(person.name, ":", str(person.attendancePoints))
        print()

        print("---Drivers---")
        for person in self.drivers:
            print(person.name, ":", str(person.attendancePoints))
    """
    def sendEmail(self, Confirmed, Waitlist, Overcap, Drivers):
        email = EmailTemplate
        for person in self.accepted:
            #sendEmail I guess
        for person in self.waitlist:
            #sendEmail I guess
        for person in self.overcap:
            #sendEmail I guess
        for person in self.drivers:
            #sendEmail I guess
    """
     

    #def chargeVenmo():
        #venmo API
        
    #def noVenmo():
        #venmoAPI



    