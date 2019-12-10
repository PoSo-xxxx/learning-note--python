from Course_def import Course

# create object
c1 = Course('Python', 18)
# call method
c1.display_course()
print('c1.show_course() =',c1.show_course())
# get data member
print('c1.name =',c1.name)
print('c1.hours =',c1.hrs)
#class is a group of definition, it can be used for data protection.
#class name:declare a class named name.
#__init__:the base definition of a class.
#self: a special argument used for class definition
#the rest of the usage of class is the same as other coding usage in Python.
#when calling the class function, class object is call by value
#which means the change only remain in funciton.
#if we want to change the real object in prgram, using call by reference data type,
#or return the changed object