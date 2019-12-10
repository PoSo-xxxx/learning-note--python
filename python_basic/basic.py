#basic of Python
#1.Python is Open Source and it is suitable for general purpose.
#2.It is also a scripting language with better function.

#print
print('hello python')
a = 1; b = 2; c = 3
print(a,b,c)                                #1 2 3
print(a,b,c, sep = ',')                     #1,2,3
print(a,b,c, end = '\\\n')                  #1 2 3\
#print(content, sep, end).
#content:the content that we want to show up.
#sep = ' ':content between the showing data.
#end = ' ':the ending mark.

#variable(bsic data type)
a=1; b=2.0; c=1+2j; d=True; e="ABC"
print('a:', type(a), '\t', id(a), a)        #a: <class 'int'>         140719515595008 1
print('b:', type(b), '\t', id(b), '\t', b)  #b: <class 'float'>       2332077559152   2.0
print('c:', type(c), '\t', id(c), '\t', c)  #c: <class 'complex'>     2332078288592   (1+2j)
print('d:', type(d), '\t', id(d), d)        #d: <class 'bool'>        140719515076944 True
print('e:', type(e), '\t', id(e), '\t', e)  #e: <class 'str'>         2332056406064   ABC
#every variable have three content:data type, id(memory address), value.
#the first word of a variable must be character.
#Python doesn't have character(char), and the boolean using interger instead.
#0<:False       0>:True.
#by the way, type(variable):used for check out the data type of a variable.
#id(variable):used for check out the memory address of the variable.
#the interger in python has no maximum and minimum.

#data type convert
a = 1
print(type(a), a, type(float(a)), float(a),
      type(complex(a)), complex(a))         #<class 'int'> 1 <class 'float'> 1.0 <class 'complex'> (1+0j)
#only can be used in numeric data type.

#input
i = input('write your name:')          #write your name:input
print(type(i))                         #<class 'str'>

#number expression
a = 46
print(a, bin(a), oct(a), hex(a))                            #46 0b101110 0o56 0x2e
print(type(a), type(bin(a)), type(oct(a)), type(hex(a)))    #<class 'int'> <class 'str'> <class 'str'> <class 'str'>
#use for converting number into different number system.
#after converting, the data type will be become string.

#eval
print(eval("5+5"))
i ,j = 'a' ,'b'
print(eval('i+j'))                      #ab
#eval is also workable on string calculation.

#the sort of data type:
#           |sequence      |non-sequence
#---------------------------------------------------------
# mutable   |list          |dict,set
# immutable |str, tuple    |frozenset
#int, float, complex are immutable data type

#call by value:string, int, float, complex
#call by reference:list, tuple, set, dictionary
#the data type above will noted in other python file


#sys & oc
import sys
print(dir(sys))                                     #['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__',
                                                    #'__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__',
                                                    #  '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding',
                                                    #  '_framework', '_getframe', '_git', '_home', '_pydevd_err_buffer_', '_pydevd_out_buffer_', '_xoptions',
                                                    #  'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 
                                                    # 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 
                                                    # 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 
                                                    # 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 
                                                    # 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 
                                                    # 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 
                                                    # 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 
                                                    # 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 
                                                    # 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 
                                                    # 'stderr_original', 'stdin', 'stdout', 'stdout_original', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']
print(sys.platform, sys.version)                    #win32 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]
#sys.exit(0)
#system library, have many function and instcution for handling environment situation.
#sys.plaform:show out the imformation of platform the program is excecuting with.
#sys.version:shout the imformation of Python version
#sys.exit(status(optional)):shock down the program.
#if status is 0:shock down when there is no error occurs.
#if status is 1:shock out whe error occurs.

import os
print(dir(os))                                      #['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 
                                                    #'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 
                                                    # 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', 
                                                    # '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', 
                                                    # '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 
                                                    # 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup',
                                                    #  'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 
                                                    # 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 
                                                    # 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 
                                                    # 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'original_execl', 
                                                    # 'original_execle', 'original_execlp', 'original_execlpe', 'original_execv', 'original_execve', 'original_execvp', 
                                                    # 'original_execvpe', 'original_spawnl', 'original_spawnle', 'original_spawnv', 'original_spawnve', 'pardir', 'path', 'pathsep', 
                                                    # 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 
                                                    # 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 
                                                    # 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 
                                                    # 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 
                                                    # 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
#operating system library, the most of functions here are used for file and folder procession. 
#os.rename(before, after):change  the file(or folder) name 'before' to 'after'.
#os.remove(file):delete the file.
#os.listdir(dirname):list all files and folders inside the 'dirname'.
#os.getcwd():this will return the current folder name(current work directory).
#os.chdir(dirname):change the current dicrevtory to 'dirname'.
#os.rmdir(dirname):delete the dirname.
#os.exit():shock down the program.


#pip
#all pip instructions are used in command line(cmd).
#python -V or python --version:check the version of python.
#pip -V or python --version:check the version of pip.
#pip list (-o,--outdated):list all packages that out of date.
#pip list (-u,--uptodate):list all packages that up to date.
#pip search 'package':search the package in PyPl.
#pip install 'project(version)':install the project.
#(version)->for example: == version->spcecific version.
#                        >= version1, < version2->newer or equal to version1, and older than version2.
#                        ~= version(1.x.y)->install 1.x version, but newer than version1.x.y.
#pip freeze > requirement.txt:list requirement packages and save in requirement.txt.
#pip install -r requirement.:install all packages on the requirement.txt.
#pip install --upgrade 'project':upgrade project.(it can also upgrade multiple package by reading the x.txt)
#pip install uninstall 'project':remove project.(it can also remove multiple package by reading the x.txt)
#numpy:a special library for mathmetical calculation,supporting array, specific calculation...etc.
