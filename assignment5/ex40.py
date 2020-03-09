# Modules / Object Oriented programming (OOC)
# access modules with . (dot) operator.

# Dict style
mystuff = {'apple' : "I AM APPLES!"}
print(mystuff['apple'])         # get apple from dict

# Module style
def apple():
    print("I AM apples!")         # get apple from the module

tangerine = "Living reflection of a dream"

# A module is like a specialized dict that stores python code
# and you can access it with the . (dot) operator.

# A class is a way to take a grouping of functions and data and place
# them inside a container so you can access them with the . (dot) operator.

# define the class

#class MyStuff(object):

#    def__init__(self):
#    self.tangerine = "And now a thousand years between"

#    def apple(self):
#        print("I AM CLASSY APPLES!")



## We instantiate (create) a class by calling the class like its a functions
# Class style
#things = MyStuff()          #this is the instantiate operation
#thing.apple()
#print(thing.tangerine)

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                                    "I don't want to get sued",
                                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                                         "With pickets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
