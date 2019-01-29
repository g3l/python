astring = "Hello world!"
print("single quotes are ' '")

print(len(astring)) #length of string/how many characters (12)


#That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.
astring = "Hello world!"
print(astring.index("o"))


astring = "Hello world!"
print(astring.count("l")) #counts the number of l's in the string. Therefore, it should print 3.

