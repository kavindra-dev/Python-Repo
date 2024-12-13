#take input as string,int, float or boolean  type specifing is not needed.
name = "Kavindra"  
age = 24
is_adult = True
print("Hello")
print(name)
print(age)
print(is_adult)

#take input from user, by default input will be as string
name2 = input("What is your name ?")
print("Hello " + name2)

#type conversion of user input needed to specific primitive type (int, float, string, boolean)
age2 = input("What is your age ?")
new_age = int(age2)+2
print("Age :  ", new_age)
