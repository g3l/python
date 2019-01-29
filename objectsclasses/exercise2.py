class People:
    name = ""
    age = ""
    nation = ""

    def description(self):
        def_desc = "Your name is %s, you are %d years old and you are from %s" % (self.name, self.age, self.nation)
        return def_desc

person1 = People()
person2 = People()

person1.name = "Godfrey Lemi"
person1.age = 22
person1.nation = "South Sudan"

person2.name = "Aristote Bobwa"
person2.age = 20
person2.nation = "Congo"

print (person1.description())
print (person2.description())
