i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


## First function
your_age = 25
your_grade = 100
def your_stats(your_age, your_grade):
    print(f"Wow if you are {your_age}, then you are halfway to 50")
    print(f"You really think you will get a {your_grade} in the class?")

your_stats(your_age, your_grade)
