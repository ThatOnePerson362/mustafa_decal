#1 Create a Module
def add(a, b):
    return a + b
    # takes the sum of two inputs
def subtract(a, b):
    return a - b
    # returns the difference between a and b
def multiply(a, b):
    return a * b
    #returns product of a and b
def divide(a, b):
    if b == 0:
        return "error"
    else:
        return a // b
    #returns quotient of a divided by b and returns an error if b equals 0.