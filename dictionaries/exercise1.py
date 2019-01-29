phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
del phonebook["Jill"]
phonebook["Jake"] = 938273443 #add a new item

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook. %i " % phonebook["Jake"])
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

print ("Contact book")
print (phonebook)
#Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
