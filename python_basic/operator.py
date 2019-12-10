#mathematical operators
a = 14; b = 4
print(a+b, a-b, a*b, b**2)                  #18 10 56 16
print(a/b, a//b, a%b)                       #3.5 3 2
#a+b == a+=b    a-b == a-=b....etc, all mathematical.
#operaiton can be written in these two style.
#'**': power calculation.
# '/': division with quotient in floating number.
#'//': division with quotient in interger.
# '%': the remainder of division.
a = 'ABC'; b = 'DEF'
print(a+b, a*2)                             #ABCDEF ABCABC
#string can only do the addtion and multiplication.

#comparison(ralation) operators
a = 1; b = 1; c = 2
print(a==b, a!=b)                           #True False
print(a>c, a<c)                             #False True
print(a>=c, a<=c)                           #False True

#logical operators
a = 12; b = 25
print(bin(a), bin(b))                       #0b1100 0b11001
print(a or b, bin(a or b), sep = "\t")      #12      0b1100
print(a and b, bin(a and b), sep = '\t')    #25      0b11001
print(not a, bin(not a), sep = '\t')        #False   0b0
#a and b: if a is true, then b else a.
# a or b: if a is true, then a else b.
#not a: if a is true, then false, else true.
#operation "not" will output boolean result.

#identity operators
print(id(a), id(b))                         #140719515595360 140719515595776
print(a is b, a is not b)                   #False True
#this kind of operator using there id(memory address) to compare.

#bitwise operators
a,b = 123,456
print(a, bin(a), b, bin(b))                #123 0b1111011 456 0b111001000
print(a<<1,bin(a<<1), a>>1,bin(a>>1))      #246 0b11110110 61 0b111101
print(a&b, bin(a&b),a|b, bin(a|b))         #72 0b1001000 507 0b111111011
print(a^b, bin(a^b), ~a, bin(~a))          #435 0b110110011 -124 -0b1111100
#a^b:a xor b(in binary).
#a<<1:a*2 a>>1:a/2.

#member operator
a = 'hello '; b = 'python'
print('h' in a, 'b' not in b)          #True True
#a (not) in b:this operator is used for check out that is a data(a)
#inside a group of data(b) (or not).

#operator priority:
#Operator                                         |Description
#------------------------------------------------------------------------------------------------
#lambda                                           |Lambda expression
#------------------------------------------------------------------------------------------------
#if – else                                        |Conditional expression
#------------------------------------------------------------------------------------------------
#or                                               |Boolean OR
#------------------------------------------------------------------------------------------------
#and                                              |Boolean AND
#------------------------------------------------------------------------------------------------
#not x                                            |Boolean NOT
#------------------------------------------------------------------------------------------------
#in, not in, is, is not,                          |Comparisons, 
#------------------------------------------------------------------------------------------------
#<, <=, >, >=, !=, ==                             |including membership tests and identity tests
#------------------------------------------------------------------------------------------------
#|                                                |Bitwise OR
#------------------------------------------------------------------------------------------------
#^                                                |Bitwise XOR
#------------------------------------------------------------------------------------------------
#&                                                |Bitwise AND
#------------------------------------------------------------------------------------------------
#<<, >>                                           |Shifts
#------------------------------------------------------------------------------------------------
#+, -                                             |Addition and subtraction
#------------------------------------------------------------------------------------------------
#*, @, /, //, %                                   |Multiplication, matrix multiplication
#                                                 |, division, floor division, remainder
#------------------------------------------------------------------------------------------------
#+x, -x, ~x                                       |Positive, negative, bitwise NOT
#------------------------------------------------------------------------------------------------
#**                                               |Exponentiation
#------------------------------------------------------------------------------------------------
#await x                                          |Await expression
#------------------------------------------------------------------------------------------------
#x[index], x[index:index],                        |Subscription, slicing,
#x(arguments...), x.attribute                     |call, attribute reference
#------------------------------------------------------------------------------------------------
#(expressions...),[expressions...],               |Binding or parenthesized expression, list display,
#{key: value...}, {expressions...}                |dictionary display, set display
