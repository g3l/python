#contains staff details
class staff:
    name = ""
    age = 0
    gender = ""
    role = ""
    shifts = ""
    staffid = 0
    def details(self):
        description = "Name: %s Age: %d Gender: %s Role: %s Shifts: %s staffid: %i" % (self.name, self.age, self.gender, self.role, self.shifts, self.staffid)
        return description

person1 = staff()
person1.name = "Godfrey Lemi"
person1.age = 22
person1.gender = "Male"
person1.role = "Preditor"
person1.shifts = "Mon-Thu"
person1.staffid = 1234

#phonebook
contacts = {
    
    "Godfrey" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781,
    "John" : 938214534
    }

if "Godfrey" in contacts:
    print (person1.details())
    print("Contact details: John",contacts["John"])
