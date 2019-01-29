def my_function(): #use def to define function
    print("And a happy new year!")

#function with arguments
def my_function_with_args(username, greeting):
    print("Hello, %s, I wish you a %s!"%(username, greeting))
    
my_function_with_args("John Doe","Merry Christmass")
my_function()#call function like this

#function with return value
def sum_two_numbers(a, b):
    return a + b
x = 1
y = 2

print("Answer = %d" % sum_two_numbers(x,y)) #or print (sum_two_numbers(x,y)) if you dont want the extra text "Answer = ".

#web examples
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print ("answer is: %i" %x)
