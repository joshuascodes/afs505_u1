from sys import argv

#Tells cmd line these are the arguments
script, filename = argv

# This opens the file, although its not really open, its just in a open mode
txt = open(filename)

#Prints the filename
print(f"Here's your file {filename}:")
#Prints the text in the file
print(txt.read())

print("Type the filename again:")
file_again = input ("> ")

txt_again = open(file_again)

print(txt_again.read())


 ###OUTPUT
#PS C:\Users\Joshu\afs505_u1\assignment3> python ex15.py ex15_sample.txt
#Here's your file ex15_sample.txt:
#This is the stuff I type into files
#When python is giving me a hard time
#arggggg .

## This is where it asked me for input

#Type the filename again:
#> ex15_sample.txt
#This is the stuff I type into files
#When python is giving me a hard time
#arggggg .

#PS C:\Users\Joshu\afs505_u1\assignment3>
