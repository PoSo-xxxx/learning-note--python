#loop description
#if, elif, else
a = 1; b = 2
if a == b:
     print('a, b is the same')
elif a > b:
     print('a is bigger than b')
else:
     print('a is smaller than b')                             #a is smaller than b
#if condition:expression
#elif condition:expression
#else:expression
#if condition is true->expression or (elif condition is true->expression).
#or (else->expression).

#ternary operator
print('a') if c else print('b')                               #a
#conditional expression, just like in C: c ? a:b.

#while
a,b = 1,1
while a is b:
    a += 1
    b += 1
print(a, b, id(a), id(b))                                     #257 257 memory_address memory_address
#while condition:expression
#condition is true->expression and repeat again; condition is false->break.

#for...in...
for base in [1,2,3,4,5,6,7,8,9]:
    for mul in [1,2,3,4,5,6,7,8,9]:
           print(base*mul ,end =' ')                          #this nested for loop will output a multiplication table from 1 to 9
    print('')
#for variable in a range:expression
#repeat the expression in a range.

#continue&break
for a in range(1,10):
    if a == 6:
        print("continue", end = '')
        continue
    if a == 9:
        print("break", end = '')
        break
    print(a, end = '')                                        #12345continue78break
print('')
#range(a,b):from a to b-1, used to represent a range.
#continue will pass the expression and keep doing the next term of the loop.
#break will leave the loop.

#different between 'range' and 'slice':
#range is used for creating data. a = list(range(0,10)).
#slice is used for seperating data or specifying data. a[1:5] = [1].