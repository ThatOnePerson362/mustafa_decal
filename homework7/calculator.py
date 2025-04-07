import math_tools

a = float(input("Enter the first number: "))

b = float(input("Enter the second number here: "))

operation = input("Enter an operator ( + - * /): ")

if operation == "+":
    print(math_tools.add(a, b))
    
elif operation == "-":
    print(math_tools.subtract(a, b))

elif operation == "*":
    print(math_tools.multiply(a, b))

elif operation == "/":
    print(math_tools.divide(a, b))

#Source for Help: "Let's code a simple python CALCULATOR!" from Bro Code's YouTube channel. https://www.youtube.com/watch?v=yUrYouDQZL8