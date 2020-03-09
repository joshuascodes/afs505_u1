from sys import exit

# using 'def' defines a function


def class_room():
    print("You lost credit on your homework.")
    print("Your teacher lets everyone leave and their is no participation")
    print("Better luck next semester")




def over():
    print("Well you didn't get your homework turned in, try harder next year")
    exit(0)


def adventure():
    print("As your walking back to class, you noice something strange...")
    print("Everybody seems ill and is barely able to walk..")
    print("You check you phone and see that the Coronovirus has infested all of Pullman!!")
    print("You sprint to health and wellness to buy the Corona virus vaccine")
    print("\n How much money do you offer the receptionist ")

    decision = input("> ")
    if "0" in decision or "1" in decision or "2" in decision:
        how_much = int(decision)
    else:
        dumb()

    if how_much < 500:
        print("Thats cute, they would never sell the vaccine for that cheap")
        exit(0)

    if how_much > 500:
        print("Nice you got the last vaccine.")
        print("Now go turn in your homework before your classmates and Dr. Ficklin catch the Coronovirus!!!")
        exit(0)

    else:
        print("Type a numerical number next time")





def home():
    print("Great you've made it home in 30 minutes.")
    print("You can relax and watch tv.")
    print("Or you can go back to turn in your assignment.")
    print("What are you going to do?")

    decision = input("> ")

    if "go back" in decision:
        adventure()

    elif "relax" in decision:
        print(" You fall asleep for 2 eternities")
        exit(0)

    elif "watch tv" in decision:
        print(" You fall asleep for an eternity")
        exit(0)

    else:
        dumb()


## Must define 'dumb' function from part 1
def dumb():
    print("That wasn't an option, try again!")
    exit(0)



def start():
    print("""
    After walking 30 minutes to class the teacher asks everyone to turn in
        their assignment, you realize you left it at home. You can go home and
        get your assignment or you can stay
        """)

    decision = input("> ")

    if decision == "go home":
        home()

    if decision == "go back":
        home()

    elif decision == "stay":
        class_room()
        
    else:
        dumb("That wasn't an option silly,")

start()
