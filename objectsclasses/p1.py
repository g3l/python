#Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes.
#Classes are essentially a template to create your objects.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
#assign class/es to object
# can create multiple different objects that are of the same class but will be individual copies
myobjectx = MyClass()
myobjecty = MyClass()
myobjectz = MyClass()
#Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".

#change the string in the variable so its different to myobjectx
myobjecty.variable = "yackity"
myobjectz.variable = "Asega"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)
print(myobjectz.variable)
#To access a function inside of an object you use notation similar to accessing a variable:

myobjectx.function()

#thats all there is so far
