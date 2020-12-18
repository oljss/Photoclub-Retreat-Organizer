class Inputs(object):
    def __init__(self, FileName, Email):
        self.fileName = FileName
        self.numTotalPeople = 0
        self.drivers = 0
        self.numWaitlist = 0
        self.emailTemplate = Email
        self.formCloseDate = 0

    def setNumTotalPeople(self):
        numPeople = int(input("How many people? (int): "))
        self.numTotalPeople+=numPeople

    def setNumWaitlist(self):
        waitlist = int(input("How many people on the waitlist? (int): "))
        self.numWaitlist+=waitlist

    def setDrivers(self):
        drivers = int(input("How many drivers? (int): "))
        self.drivers+=drivers
    
    def setformCloseDate(self):
        closeDate = int(input("When does this close?"))
        self.formCloseDate+=closeDate
