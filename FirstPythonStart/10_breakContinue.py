students = ["ram", "Rahul", "Raja", "Radha", "Radhika"]

#break the student list when Raja matches and print all the name before him from the list.
print("Print break section :")
for student in students :
    if student == "Raja" :
        break                   #break when keywork matches and print the list till before its break
    print(student)


# continue will skip the matched name and proceed to print all name
print("")
print("Print Continue section")
for stud in students :
    if stud == "Raja" :
        continue                   #break when keywork matches and print the list till before its break
    print(stud)


#pass
#exit
#break 2
#sys.exit()
#quite()