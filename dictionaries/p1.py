phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
del phonebook["Jill"]#delete someone, can also use phonebook.pop("John")
print(phonebook)

#Iterating over dictionaries
print ("iteration:")##prints names in alphbetical order
phonebook["Josh"] = 123456789
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
if "Jill" not in phonebook:
    print ("Jill is not one of the lads")
