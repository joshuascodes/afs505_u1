from sys import argv
filename = argv
print("Filename:", test.txt)

print(f"We're going to erase {test.txt}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
