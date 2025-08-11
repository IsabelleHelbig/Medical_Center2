class Doctor:
    def __init__(self, id, name, specialty, schedule, qualification, roomNumber):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.qualification = qualification
        self.roomNumber = roomNumber

    def formatDrInfo(self, id, name, specialty, schedule, qualification, roomNumber):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.qualification = qualification
        self.roomNumber = roomNumber
        return "{}_{}_{}_{}_{}_{}\n".format(self.id, self.name, self.specialty, self.schedule, self.qualification, self.roomNumber)

    def __str__(self):
        print("{:5s} {:15s} {:20s} {:15s} {:15s} {}".format(self.id, self.name, self.specialty, self.schedule, self.qualification, self.roomNumber))




