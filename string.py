name = "Godfrey Lemi"
age = 22
#using %
#note you cant just have % name, age. you need to put them in a bracket unlesss its just once variable
print("Hello, %s. You are %i" % (name, age))

# using format
# same outcome
#can leave {} empty or instert numbers to change order of what appears
print("Hello, {}. You are {}.".format(name, age))
# print("Hello, {1}. You are {0}.".format(name, age)) here it will say hello 22 then name

# read this for more https://realpython.com/python-f-strings/


#using other format
person = ("Godfrey", "Asega", "Amazon")
format_string = "Hello %s %s, You currently work at %s"

print(format_string % person)
