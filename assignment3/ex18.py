# def = creates a function
# print_two = the name we created for the function
# (*args) is like argv but it is for functions and has to be inside paretheses
 # a colon --> : indents the next line. anything in indented lines becomes attached to
 # the function print_two
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

######################################

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

######################################
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Joshua", "Freimark")
print_two_again("Joshua", "Freimark")
print_one("First!")
print_none()
