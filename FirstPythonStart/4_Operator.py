# taking 1st and 2nd no input from user
f1 = input("Input first no : ")            
f2 = input("Input second no : ")  

#type conversion to int
x = int(f1)
y =  int(f2)
z = int(3) #direct valse parsing


#Arithematic operation
sum = x + y         #Add
sub = x - y         #sub
mul = x * y         #Multiply
div = float(x/y)    #Divide and return with float value
intDiv = x//y       #Divide and return only integer value
rem = x % y         #Module shows reminder feature
pow = x ** 3        #Power of 3 over x
z += y              #Adding z and y and storing in z


#print the above output
print("Sum : "+str(sum))
print("Sub : "+str(sub))
print("Mul : "+str(mul))
print("Div : "+str(div))
print("Int_Div : "+str(intDiv))
print("Rem : "+str(rem))
print("Pow : "+str(pow))
print("Add minim : "+str(z))

#operator precedance
# /, *,+, - (goes higer to lower)