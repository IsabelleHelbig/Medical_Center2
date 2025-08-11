class Patient:
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    def formatPatientInfo(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age
        return "{}_{}_{}_{}_{}\n".format(self.id, self.name, self.diagnosis, self.gender, self.age)

    def __str__(self):
        print("{:5s} {:15s} {:15s} {:10s} {}".format(self.id, self.name, self.diagnosis, self.gender, self.age))




