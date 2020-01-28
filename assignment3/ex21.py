def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("LET'S DO SOME MATH WITH FUNCTIONS!!!")

age = add(20, 5)
height = subtract(75, 3)
weight = divide(350, 2)
iq = multiply(55, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

what =add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That comes: ", what, "Can you do it by hand?")
