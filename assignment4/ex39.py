##  LIST
#  a list for any sequence of things that need to be in order, and you
#  only need to look them up by a numeric index.

things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)


## DICT
# When you have to take one value and ”look up” another value. In
# fact, you could call dictionaries ”look up tables.”

stuff = {'name' : 'josh', 'age' : 25, 'height' : 6 * 12 }
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = 'SF'
print(stuff['city'])
stuff[1] ="Wow"
stuff[2] = "neato"
print(stuff[1])
print(stuff[2])
stuff.pop('city')
stuff.pop(1)
stuff.pop(2)
print(things)
print(stuff)

##### A long dictionary example states & cities

states = {
'Oregon' : 'OR',
'Florida' : 'FL',
'California' : 'CA',
'New York' : 'NY',
'Michigan' : 'MI',
}

# Create some cities insidie the states
cities = {
'CA' : 'San Fransisco',
'MI' : 'Detroit',
'FL' : 'Jacksonville'
}

## Add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities

print('-' * 10)
print("NY State has :", cities['NY'])
print("OR State has:", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Do it by usuing the state then cities dict

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


# Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities}[abbrev]")

    print('-' * 10)
    # Safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

# Get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is {city}")
