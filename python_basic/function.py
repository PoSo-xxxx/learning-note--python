#function
def testing(a,b):
    return a+b
def testing1(a):
    print(type(a))
def testing2():
    print('testing!!!')
a = 1;b = 2;c = testing(a,b)
print(c)                                                      #3
testing1(c)                                                   #<class 'int'>
testing2()                                                    #testing!!!
#def function(argument):
#    expression
#
#when we call the function:
#function(argument)
#function is a smaller program, used to do some repeated instrcution,
#make the main program cleaner and easier to read.

#pass by assignment
def change(var):
    print("before:", var)                                     #before: hello
    var = "python"
    print("after:", var)                                      #after: python
v = "hello"
change(v)
print("outside:", v)                                          #outside: hello

def changeL(lt):
    print("before:", lt)                                      #before: [10, 20, 30]
    lt[2] = 50
    print("after:", lt)                                       #after: [10, 20, 50]
t = [10,20,30]
changeL(t)
print("outside:", t)                                          #outside: [10, 20, 50]
#using the immutable data type as argument:the value in main function will not be changed.
#using the mutable data type as argument:the value in main function will be changed.

#argument
def printinfo(tb = 'n\\a', db = 'n\\a', port = 'n\\a'):
    print('table name:', tb, end = ' ')
    print('data base:', db, end = ' ')
    print('port:', port, end = '\n')
printinfo('person')                                           #table name: person data base: n\a port: n\a
printinfo(tb = 'person')                                      #table name: person data base: n\a port: n\a
printinfo(port =3330, tb = 'product')                         #table name: product data base: n\a port: 3330
printinfo('person', 'mysql', 1433)                            #table name: person data base: mysql port: 1433
printinfo('product', port = 3300)                             #table name: product data base: n\a port: 3300
#def printinfo(tb = 'n\\a', db = 'n\\a', port = 'n\\a'):
#default argument:if function is called with no argument , the function will process
#using default value.(for example:'n\\a')
#printinfo('person', 'mysql', 1433):
#positional argument:argument following the order of function definition.
#printinfo(port =3330, tb = 'product'):
#keyword argument:setting value to argument in function definition,
#so it doesn't need to follow the order of definition.

#arbitrary argument:
def printnum(a, *v):
    print(a, end = ' ')
    for b in v:
        print(b, end = ' ')
printnum(10)                                                 #10
print()                                                      #newline
printnum(10,20,20,30,30,30,40,10)                            #10 20 20 30 30 30 40 10
print()                                                      #newline
#*argument:when the input of a function is not certain number of argument,
#we using *argument as argument so that funciton accept multiple input.


#lambda
def origin(a,b):
    return a+b
def operate(a,b,func):
    return func(a,b)
print('origin:', operate(1,2,origin))                        #origin:3
print('lambda:', operate(1,2,lambda a,b:a*b))                #lambda:2
#lambda:a temporary function
#insted of changing the original funciton, using lambda for temporary purpose.
#easier for use.


#global & local
total = 0
def sum_data(a1,a2):
    total = a1+a2
    print('in function: total = ', total)
sum_data(10,20)                                              #in function: total =  30
print('in main: total = ', total)                            #in main: total =  0

def cake():
    global fruit
    fruit = 'apple'
    print(fruit)
def icecream():
    fruit = 20
    print(fruit)
fruit = "banana"
print(fruit)                                                 #banana
icecream()                                                   #20
cake()                                                       #apple
print(fruit)                                                 #apple
#declare outside of function:grobal variable
#declare in function:local variable
#in a function, if grobal variable and local variable have the same name,
#local variable will replace global variable.
#function can reference by global variable.
#global variable:to reference global variable in function.
