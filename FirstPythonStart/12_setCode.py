#if we want to store unique element only for a larger no of data we uses set

# we can chage tuple to set by adding element inside {}

marks = {95,97,96,65, 65, 65}

print(marks)

#index doesn't exist in set uncomment print to check the output error
#print(marks[0])            # will give TypeError: 'set' object is not subscriptable

#can only iterate data using only loop not with index
print("Set in python :")
for score in marks :            #only give unique value only
    print(score)

