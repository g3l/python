astring = "Godfrey Lemi!"
#prints a slice of the string, starting at index 3, and ending at index 6
print(astring[3:7])
#If you just have one number in the brackets, it will give you the single character at that index.
#If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in.
#If you leave out the second number, if will give you a slice from the first number to the end.
#-3 means "3rd character from the end".

print(astring[3:7:2])
#This prints the characters of string from 3 to 7 skipping one character.
#This is extended slice syntax. The general form is [start:stop:step].


#revers strings
print(astring[::-1])

#change case
print(astring.upper())
print(astring.lower())

#find if strings end or starts with something
print(astring.startswith("Go"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")# creates a list splitting words at space since ""
#basically deletes whateve you specify in ""
print(afewwords)
