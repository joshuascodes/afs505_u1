Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(pydoc)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    help(pydoc)
NameError: name 'pydoc' is not defined
>>> from sys import argv
>>> python3.6 ex13.py first 2nd 3rd
SyntaxError: invalid syntax
>>> python ex13.py first 2nd 3rd
SyntaxError: invalid syntax
>>> script, user_name = argv
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    script, user_name = argv
ValueError: not enough values to unpack (expected 2, got 1)
>>> python3.6 ex13.py first 2nd 3rd
SyntaxError: invalid syntax
>>> from sys import argv
>>> python3.6 ex13.py first 2nd 3rd
SyntaxError: invalid syntax
>>> script, user_name = argv
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    script, user_name = argv
ValueError: not enough values to unpack (expected 2, got 1)
>>> from sys import argv
>>> script, first, second, third = argv
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 1)
>>> script = argv
>>> script, first = argv
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    script, first = argv
ValueError: not enough values to unpack (expected 2, got 1)
>>> first = argv
>>> second = argv
>>> third = argv
>>> script, first, second, third = argv
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 1)
>>> print("The script is called:", script)
The script is called: ['']
>>> print("Your first variables is:", first)
Your first variables is: ['']
>>> print("Your second variable is:", second)
Your second variable is: ['']
>>> print("Your third variable is:", third)
Your third variable is: ['']
>>> python3.6 ex13.py first second third
SyntaxError: invalid syntax
>>> import sys
>>> print("This is the name of the script:", ex13.py)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("This is the name of the script:", ex13.py)
NameError: name 'ex13' is not defined
>>> print("This is the name of the script:", ex13.py)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("This is the name of the script:", ex13.py)
NameError: name 'ex13' is not defined
>>> print("This is the name of the script:", ex13.py)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("This is the name of the script:", ex13.py)
NameError: name 'ex13' is not defined
>>> 
>>> 
>>> print("number of arguments.", len(sys.argv)
      1
      
SyntaxError: invalid syntax
>>> print("number of arguments.", len(sys.argv)
      print("The arguments are:", str(sys.argv)
	    
SyntaxError: invalid syntax
>>> print("number of arguments.", len(sys.argv)
      fun
      
SyntaxError: invalid syntax
>>> import sys
>>> program_name = sys.argv[0]
>>> arguments = sys.argv[1:]
>>> count = len(arguments)
>>> import sys
>>> for x in sys.argv:
	print "Argument", x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Argument", x)?
>>> for x in sys.argv:
	print ("Argument",) x
	
SyntaxError: invalid syntax
>>> len(sys.argv),
(1,)
>>> count = len(arguments)
>>> len(sys.argv),
(1,)
>>> import sys
>>> if len (sys.argv)
SyntaxError: invalid syntax
>>> if len (sys.argv)!=
SyntaxError: invalid syntax
>>> if len (sys.argv)!=2:
	print"Usage: python ex.py"
	
SyntaxError: invalid syntax
>>> python ex.py
SyntaxError: invalid syntax
>>> ### none of this shit works i wonder if its cause pydoc doesnt work