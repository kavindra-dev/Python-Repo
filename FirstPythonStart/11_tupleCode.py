# same as list but it is immutable, that is created it cannot be changed
# it is basically used for predefining element and and allowing to change later

marks = (95, 87, 65, 76, 76)
# () are not neccessary we can define same by marks = 95, 87,65,76,76 also for tuple.

marks = tuple()
#marks[0] = 99          #it will give TypeError: 'tuple' object does not support item assignment
#uncomment marks to check.


#can count the no of appearence of an element.
print(marks.count(95))

#can get the index of marks element
print(marks.index(76))
