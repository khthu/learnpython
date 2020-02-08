Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> line="1+2+3"
>>> import eval
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import eval
ModuleNotFoundError: No module named 'eval'
>>> eval(line)
6
>>> 
=========== RESTART: /Users/Tran/Desktop/PythonPractice/PlayGround.py ==========
>>> 123+1
124
>>> done
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    done
NameError: name 'done' is not defined
>>> 123+1
124
>>> "123+1"
'123+1'
>>> 
=========== RESTART: /Users/Tran/Desktop/PythonPractice/PlayGround.py ==========
>>> "123+1"
'123+1'
>>> 
=========== RESTART: /Users/Tran/Desktop/PythonPractice/PlayGround.py ==========
Input your string = 123+1
>>> 
=========== RESTART: /Users/Tran/Desktop/PythonPractice/PlayGround.py ==========
Input your string = 1+2+3
6
>>> done
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    done
NameError: name 'done' is not defined
>>> 
=========== RESTART: /Users/Tran/Desktop/PythonPractice/PlayGround.py ==========
Input your string = 1+2+3
>>> 
>>> 
=========== RESTART: /Users/Tran/Desktop/PythonPractice/PlayGround.py ==========
Input your string = 1
1
Input your string = 1+2+3
6
Input your string = done
>>> 
