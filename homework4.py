# 2.1 Making a List Variable
zerototwenty = list(range(0,21))
print(zerototwenty)
# I tried [range(0:21)], but I got a syntax error. I also forgot that commas were the appropriate punctuation when using the range function and not colons.

# 2.2 Working with List Elements
zerototwenty = list(range(0,21))
def squareList():
    power = [i**2 for i in zerototwenty]
    return power
rectangle = squareList()
print(rectangle)
# I encountered errors in terms of trying to print things that were only defined within the function. For example, I tried to define rectangle = squareList(power), but power is only defined within the function. I changed it to rectangle = squareList(), and then I was able to print rectangle.

# 2.3 Slicing
rectangle = squareList()
def first_fifteen_elements(rectangle):
    fifteen = rectangle[0:15:1]
    return fifteen
print(first_fifteen_elements(rectangle))

# 2.4 Striding
rectangle = squareList()
def every_fifth_element(rectangle):
    five = rectangle[4:21:5]
    return five
print(every_fifth_element(rectangle))

# 2.5 Slicing & Striding
rectangle = squareList()

# 3.1 Creating a 5*5 2D List
twentyfive = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15], 
    [16, 17, 18, 19, 20], 
    [21, 22, 23, 24, 25]
    ]
def create_2D_list():
    for i in range(5):
        for j in range(5):
            print(twentyfive[i][j])
        return twentyfive
print(create_2D_list())
# I tried to return a list of all the variables in my for loop, but got the following error: "TypeError; 'int' object is not iterable."

# I tried skimming through a couple of videos to figure out how to make the matrix