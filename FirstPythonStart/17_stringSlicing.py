# Slicing is basically used for slice a string or extracting a part of string or we can say substring
#syntax : 
# str[start : stop : step]
# *Note : If step value is positive (1,2,3 , etc.) it will go in forward direction.
#         If step value is negative (-1,-2,-3, etc.) it will go in backward direction.
#         Stop : will always execute till 1 less than specified value, i.e; stop value is not included.
# Exp : 

stVal = "Kavindra Tripathi"         #Define a string like your name

print("Print without start and end index data but steps is given positive flow:")
#in this start value and stop value not provide but steps is given and it is positive so start with index 0
print(stVal[::2])               
# Above will print string by leaving one after another 
#Output will be : Kvnr rpti


print("Print without step passed but start and end index is given positive flow:")
# No step provide below but has start and end value 2 & 3 so it starts from index 2 and go till index(3-1)
#And since no step is given default it take 0 i.e; positive so start reading string from "K" to "i"
print(stVal[2:3])        

print("Print without start and end index data but steps is given negative flow :")
#in this start value and stop value not provide but steps is given and it is negative so start with index from reverse
print(stVal[::-2])               
# Above will print string by leaving one after another 
#Output will be : itpr rnvK


print("Print without step passed but start and end index is given negative flow:")
# No step provide below but has start and end value -2 & -5 so it starts from index -2 and go till index(-5-(-1))
#And since no step is given default it take 0 i.e; positive so start reading string from "K" to "i"
print(stVal[-2:-5])        

print("Print with step passed along with start and end index is given negative flow:")
# step provide below along with start and end value -2 & -5 so it starts from index -2 and go till index(-5-(-1))
#And since step is given -1 i.e; negative so start reading string from "i" to "K"
print(stVal[-2:-5:-1])    

print("Print with step passed along with start and end index is given positive flow:")
#step provide below along with start and end value 2 & 5 so it starts from index 2 and go till index(5-1)
#And since step is given 1  i.e; positive so start reading string from "K" to "i"
print(stVal[2:5 : 1])    
