Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> quit()
>>> python
<<<<<<< HEAD

=======
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> python -V
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    python -V
NameError: name 'python' is not defined
>>> python -V
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    python -V
NameError: name 'python' is not defined
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> hi everyone
SyntaxError: invalid syntax
>>> input1 = input()
print(input1)
>>>>>>> 993ebf303719f43aa3f34106237df638d2cb59d3
>>> input1 = input()
6
>>> print(input1)
6
>>> val = input("enter your value: ")
enter your value: 12345
>>> print(val)
12345
>>> print("How old are you?", end=' ')
<<<<<<< HEAD
How old are you?
=======
How old are you? 
>>>>>>> 993ebf303719f43aa3f34106237df638d2cb59d3
>>> age =input()
25
>>> print(f"So, you're {age}")
So, you're 25
>>> print("How tall are you?", end=' ')
<<<<<<< HEAD
How tall are you?
=======
How tall are you? 
>>>>>>> 993ebf303719f43aa3f34106237df638d2cb59d3
>>> height = input()
25
>>> print(f"So you're {age} old, {height} tall")
So you're 25 old, 25 tall
>>> height = input()
6'0
SyntaxError: multiple statements found while compiling a single statement
>>> height = input()
6'0
>>> print(f"so you're {age}, and {height} tall?")
so you're 25, and 6'0 tall?
>>> print("how much do you weight?", end=' ')
<<<<<<< HEAD
how much do you weight?
>>> weight = input()
175
>>> print("how much do you weight?", end=' ')
how much do you weight?
>>> print(f"So you're {age} old, {height} tall and {weight} heavy? ")
So you're 25 old, 6'0 tall and 175 heavy?
=======
how much do you weight? 
>>> weight = input()
175
>>> print("how much do you weight?", end=' ')
how much do you weight? 
>>> print(f"So you're {age} old, {height} tall and {weight} heavy? ")
So you're 25 old, 6'0 tall and 175 heavy? 
>>>>>>> 993ebf303719f43aa3f34106237df638d2cb59d3
>>> So, you're 25
SyntaxError: EOL while scanning string literal
>>> y = input("Name? ")
Name? Josh
>>> print(y)
Josh
>>> age = input("How old are you? ")
How old are you? 25
>>> height = input("How tall are you? ")
How tall are you? 6'0
>>> weight = input("How much do you weight? ")
How much do you weight? 175 lbs
>>> print(f"So, you're {age} and {height} tall, and {weight} heavy?")
So, you're 25 and 6'0 tall, and 175 lbs heavy?
>>> print("How old are you?: {age}")
How old are you?: {age}
>>> print("How old are you?" {age})
SyntaxError: invalid syntax
<<<<<<< HEAD
>>>
=======
>>> 
>>>>>>> 993ebf303719f43aa3f34106237df638d2cb59d3
