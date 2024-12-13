# Dictonary : Just like set but has a feature of key-value pair

#adding key-value pair in the markslist
marks = {"english" : 95, "chemistry" : 89, "maths" : 85}


print("Fetching one element:")
print(marks["english"])         #key will work as index now 

#adding new element in the dictonary
print("Added new element in the marks :")
marks["physics"] = 76

print(marks)

#updating one element value
print("Update dictonary data value :")
marks["maths"] = 99
print(marks)