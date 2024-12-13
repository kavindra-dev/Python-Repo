#Constructors are generally used for instantiating an object. 
#The task of constructors is to initialize(assign values) to the data members 
#of the class when an object of the class is created

#In Python the __init__() method is called the constructor and is always called when an object is created.

#Syntax : def __init__(self) :
#           body of the constructor mention here

#Types of constructor :
#1. default constructor : 
#The default constructor is a simple constructor which doesn’t accept any arguments. 
#Its definition has only one argument which is a reference to the instance being constructed.

#Check example code below :

# class Test:
 
#     # default constructor
#     def __init__(self):
#         self.d = "Test Default Constructor"    
 
#     # a method for printing data members
#     def print_test(self):                   # Instance method is created.
#         print(self.d)
 
 
# # creating object of the class
# obj = Test()
 
# # calling the instance method using the object obj
# obj.print_test()



#2. parameterized constructor: 
#Constructor with parameters is known as parameterized constructor. 
# The parameterized constructor takes its first argument as a reference 
# to the instance being constructed known as self and the rest of the arguments are provided by the programmer

#Check Example code below:

class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s) :              #create a constructor and assign parameter value
        self.first = f
        self.second = s

    def display(self) :                                     #create a method to display first and second no.
        print("First No = "+str(self.first))
        print("Second No = "+str(self.second))
        print("Addition of No are ="+str(self.answer))

    def calculate(self) :                                   #calculte the sum of two no.
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(500,200)                            #passing the parameter to the constructor

# perform Addition on obj1
obj1.calculate()

# display result of obj1
obj1.display()