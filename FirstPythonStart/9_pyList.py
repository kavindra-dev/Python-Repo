# List => *Collection of items
#* We can store many primitive data type in a single place

marks = [90, 60, 60, 50]
marks2 =[45,67,87]

name =["My", "Name", "is" ,"Kavi"]

print("Join list into a single string :")
strname = " ".join(name)                #uses to join the element of list together
print(strname)      

print("Split a string into list of data :")
splitstr = strname.split()              # uses to split a string into a list
print(splitstr)

print("Print marks list:")
print(marks)

print("Print marks list in reverse:")
print(marks[-1]) # -1 represent reverse printing 3 to 0

print("print in normal flow direction")
print(marks[1]) # 1 nornal printing 0 to 4

print("print fromrange of 1 to 3-1:")
print(marks[1 : 3 ]) # print from a raange of initial no to less than 1 in end no.


#iterate each element in the list using for loop
print("Iterate using for loop:")
for score in marks :  
    print(score)


# We can perform opertion on list

print("Add new element at the end of marks:")
marks.append(99)            #Add new element at the end of list
print(marks)



print("Insert 99 at index 0 :")
marks.insert(0,99)          # Add element at the mentioned position in the list
print(marks)


print("Check for 99 existance in marks :")
print(99 in marks)          # Check for 99 exist in marks list if yes return boolean valur true else false


print("print length of marks list")
print(len(marks))           #return and print the length of marks list


print("Extend the exist list with new list :")
print(marks.extend(marks2))


#iterate marks using while loop :
i = 0
print("print iteration using while loop :")
while i < len(marks) :
    print(marks[i])         #print individual info
    i = i + 1


print("Cleared the marks list")
marks.clear()                 #Clear the marks list 
print(marks)