

class chiefcomplaint:
    def __init__(self, onset, location, duration, quality):
        self.onset = onset
        self.location = location
        self.duration = duration
        self.quality = quality
    
    def printcc(self):
        print("Onset: " + self.onset)
        print("Location: " + self.location)
        print("Duration: " + self.duration)
        print("Quality: " + self.quality)



class patient:
    def __init__(self, name, age, chiefcomplaint):
        self.name = name
        self.age = age
        self.chiefcomplaint = chiefcomplaint

    def printpatient(self):
        print("Patient name: " + self.name)
        print("Patient age: " + str(self.age))
        print("Patient chief complaint: " + self.chiefcomplaint.onset + " " + self.chiefcomplaint.location + " " + self.chiefcomplaint.duration + " " + self.chiefcomplaint.quality)
    
    