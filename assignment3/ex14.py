from sys import argv

user_name = input("user_name")
user_nameJoshua
>>> user_name
'Joshua'
>>> script = input("script")
scriptex15.py
>>> print(f"Hi {user_name}, I'm the {script} script.")
Hi Joshua, I'm the ex15.py script.
>>> print("I'd like to ask you a few questions.")
I'd like to ask you a few questions.
>>> print(f"Do you like me {user_name}?")
Do you like me Joshua?
>>> likes = input(prompt)
>Of course
>>> print(f"Do you like me {user_name}?")
Do you like me Joshua?
>>> likes = input(yeah)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    likes = input(yeah)
NameError: name 'yeah' is not defined
>>> print(f"Where do you live {username}?")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(f"Where do you live {username}?")
NameError: name 'username' is not defined
>>> print(f"Where do you live {user_name}?")
Where do you live Joshua?
>>> lives = input(prompt)
>Pullman
>>> print("What kind of computer do you have?")
What kind of computer do you have?
>>> computer = input(prompt)
>windows
>>> print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")

Alright, so you said Of course about liking me.
You live in Pullman. Not sure where that is.
And you have a windows computer. Nice

>>> python3.6 ex15.py Joshu
SyntaxError: invalid syntax
>>>
>>> car = input(prompt)
>BMW
>>> print(f"So you drove a {car} ??")
So you drove a BMW ??
>>> 
