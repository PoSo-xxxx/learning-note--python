#read & write
f = open('test_learning.txt', 'r')
print(f.name, f.read(), sep = '\n')                 #test_learning.txt
                                                    #123456789
f = open('test_learning.txt', 'a')
f.write('Learning Python is easy')  
f = open('test_learning.txt', 'r+')
print(f.readline())                                 #123456789Learning Python is easy
f.write('abc')
f = open('test_learning.txt', 'r')                  #123456789Learning Python is easyabcLearning Python is easyabc
print(f.read())
f = open('test_learning.txt', 'w')
f.write('123456789')
f.close()
#open(file_name, mode, buffer):open the file_name in mode with buffer.
#mode:the default is 'rt',it contain three character:'XYZ'.
#X->r: read only.                                                  w:write only(will clear the file first).
#   x:write only(create a new file,error occurs when file exist).  a:write only(continue writing at the end of data).
#Y->b:open the file in binary mode.                                t:open the file in strings.
#Z->+:updating mode(can write or read).
#buffer: turn on the line_buffer(0:turn off, 1:turn on).
#file.write(contain):write the contain into file.
#file.read(long(optional)):read the contain in file, the default is the whole file, adding the argument'long'
#into funciton, function will only read the number of long in the file.
#file.readline():read the contain in file once a line,and stop reading when find a '\n' character,
#if we repeated using readline(), every time we call, it will start with next line of data.
#if readline() return a null string, it means 'EOF'.
#file.close():save the data in buffer into fil eand close the opening file.