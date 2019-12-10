#module
from support_learning import bmi
print('171cm,65kg, the bmi is{:2.2f}'.format(bmi(65, 171)))  #171cm,65kg, the bmi is22.23
import support_learning
support_learning.showing()                                   #this is module testing!!!
print(dir(support_learning))                                 #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'bmi', 'showing']
#module can turn program into a library, for other program to use.
#the module name is the file name of a py file.(example:support_learning->support_learning.py).
#import module_name:import all funcitons in module_name.py to this program for use.
#from module_name import function_name:only import function_name from module_name.py for use.
#dir(module_name):will return a list of defined function in module_name in order.
#__name__ is a special system variable, which means the top scirpt envirnment.
#it can be __main__->then the module_name.py will exceucte as a script.
#            module->then the module_name.py will excecute as a imported module, used by other program.
#if __name__ = '__main__':use if loop the determine that a 'py' file will excecuted as a script or a module.
#be careful:using idle or spyder, we need to manually setting the path of import file.
