## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## Created a class called Animal
class Dog(Animal):


        def __init__(self, name):
            ## we can access the name class by using .name
            self.name = name

class Cat(Animal):

        def __init__(self, name):
            ##
            self.name = name

class Person(object):

        def __init__(self, name):

            self.name = name

            ## Person has-a pet of some kind

            self.pet = None

##
class Employee(Person):

        def __init__(self, name, salary):
            #Hmm what is this strange magic??
            super(Employee, self).__init__(name)
            ##
            self.salary = salary
#
class Fish(object):
    pass

class Salmon(object):
    pass

class Halibut(Fish):
    pass


# Rover is-a Dog
rover = Dog("Rover")

#
satan = Cat("Satan")

#
mary = Person("Mary")

#
mary.pet = satan

#
frank = Employee("Frank", 120000)

#
frank.pet = rover

#
flipper = Fish()

#
crouse = Salmon()

#
Harry = Halibut()


print(mary.pet.name)
