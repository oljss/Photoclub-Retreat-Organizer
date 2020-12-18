class Member(object):
    def __init__(self, Name):
        self.name = Name
        self.attendancePoints = 0
    
    def setAttendancePoints(self, Points):
        self.attendancePoints += Points
    
    def __str__(self):
        s = ""
        s+=self.name+":"+str(self.attendancePoints)
        return s


