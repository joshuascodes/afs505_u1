from sys import exit











def fun1_function():
    print("How fun can we make this")
choice = input("> ")

if choice == "fun":
    exit(0)
else:
    print("send them to the loop")
    the_loop()


josh = 100
j1 = 200
j2 = 101.102

# Create a list
jlists = [1], [2], [3], [4]
# Remember this will return the 0,1,2nd value. So it will return 3
print(jlists[2])


#Create a dictonary
jdicts = {'a': 1, 'b' : 20, 'c' : 200, 'd' : "you can do strings too"}
##Reurns a value of the dictonary
q = jdicts['b']
print(q)





#Escape keys for text
def fun_function():
    print("""
    If you want to seperate using a \'slash\' just do \\ this will
    allow you to have \"cleaner\" code
    \t add some indenting
    \v find out what this does
    nicely done on your firday evening \n
    goodnight""")
fun_function()
