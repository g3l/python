# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
# your code goes here
car1 = Vehicle()
car1.color = "Red"
car1.value = 60000
car1.name = "Fer"
car1.kind = "convertible"

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.value = 10000.00 #don't need the .00 because %.2f adds them for you
car2.color = "blue"

# test code
print(car1.description())
print(car2.description())

#We have a class defined for vehicles. Create two new vehicles called car1 and car2.
#Set car1 to be a red convertible worth $60,000.00 with a name of Fer
#car2 to be a blue van named Jump worth $10,000.00.
