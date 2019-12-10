#try, execpt and raise:
f = open('test_learning.txt')
try:
    s = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print('file is not exist')                                          #file is not exist
except ValueError as e:
    print('can not convert data into interger, a {} occur'.format(e))   #can not convert data into interger, a invalid literal for int() with base 10: '' occur
except:
    print('unexpected error')                                           #unexpected error(then an error message shows up)
    raise
else:
    print(i)                                                            #12345679
finally:
    print('pass all error test')                                        #pass all error test
    f.close()
#the try loop used for testing the program, make error easier to handle.
#try: expression.
#excecute the expression, if error occurs, go to except.
#except error_name: expression.
#when error_name occurs, excecute the expression without occurs the error and show up the massege.
#except has many usage, for example:
#except(error1, error2...):handle error1, error2 or more.
#except error_name as e:make e as error_name's description.
#raise:let the error occurs.
#else: expression if no error occurs, excecute the expression.
#finally: expression when try loop finish, excecute the expression.
#(the finally loop will always excecute when try loop finish).
#the flow:
#   try--->safe--->else(optional)--->finally(optional)
#      --->error--->except--->finally(optional)
#for more error imformation:https://docs.python.org/3/library/exceptions.html

#with
with open('test_learning.txt', 'r') as f:
    print(f.read())                                 #123456789
    f.close()
#with open(...) as variable:
#it has better ability to handle the exception and error.
#it will automatically excecute flie.close() when exception or error occur and at the end of with loop.
