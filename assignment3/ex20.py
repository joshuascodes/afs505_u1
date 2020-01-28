from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#OUTPUT
# use python ex20.py text.txt in the command line
#PS C:\Users\Joshu\afs505_u1\assignment3> python ex20.py test.txt
#First let's print the whole file:
#
#ÿþT h i s   i s   a   t e s t   f i l e .

 #I   h a v e   m o r e   l i n e s

# n o w
#Now let's rewind, kind of like a tape.
#Let's print three lines:
#1 ÿþT h i s   i s   a   t e s t   f i l e .
#
#2
#
#PS C:\Users\Joshu\afs505_u1\assignment3>
