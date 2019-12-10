#'''
a = '''we need to use\'\'\' to output the data when we process with document
string and format output'''
#''' will be used to output docstring

#f-string
#a kind format output, supported since Python3.6
name, year = 'jj', 1987
print(f'{name} was born in {year}, now is {2019 - 1987}')     #jj was born in 1987, now is 32
#f/F'{content}...':content can be any content, string number ...etc
code = 123.456
print(f'{code:4.0f} {code:5.2f} {code:7.4f} {code:08.2f}')    # 123 123.46 123.4560 00123.46
#f'{content:x.yf}':output in floating number format,
#it will rounding the number to fit the format. for example:123.456->123.46.
#x is the total bits of showing number, y is the bits after decimal point.
#if the bits of showing number is not enough, it will add " "at left;
#and add "0" at right.
import time
from datetime import datetime
print(f'{datetime(1995,2,3,4,5,6):%Y-%m-%d %H:%M:%S}')        #1995-02-03 04:05:06    
name = 'fortune'
print(f'{name.upper()} is a talent')                          #FORTUNE is a talent
#the function of string can be used in f-strings
data = {'name':'john', 'age':28}
#this is dictionaries, which will be discussed later
print(f"he is called {data['name']}, {data['age']} years old")#he is called john, 28 years old
#be careful using dictionaries in f-strings,
#while using quotation mark for f-strings, we
#should use different quotation amrk for dictionaries.

#format
#also a format output with different style
name, age = 'john', 1987
print('{} born in {}'.format(name,age))                       #john born in 1987
print('{1} born in {0}'.format(name,age))                     #1987 born in john
#'{}'.format(variable):the variable's data will shown up in {}.
#we can also assign the order of data showing using number.

#%
#the oldest format output since Python 2.0
print('%s born in %d' %(name,age))                            #john born in 1987
#typing style is more close to C.

#escape character
print(" \\ \' \" \a  abc\bdef  abc\fdef  abc\ndef  abc\tdef abc\vdef")  # \ ' "   abdef  abc
                                                                        #                   def  abc
                                                                        #def  abc        def abc
                                                                        #                       def
#\\:remain \    \':remain '     \":remain "     \a:ring a bell
#\b:backspace   \f:formfeed     \n:linefeed     \t:horizontal tab
#\v:vertical tab\oXX:character with octal value XX.
#\xHH:character with hex value HH.
#all escape character are follow the format  of ASCII.