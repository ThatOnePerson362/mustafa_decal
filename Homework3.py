# Homework 3
# Problem 1: Oski Stole Your Power
def not_power(x, y):
    answer = 1
    for i in range(y):
        answer = answer*x
    return answer
print(not_power(2,3))

# Problem 2: What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    cold = min(readings) 
    warm = max(readings)
    return (cold, warm)
print(temperatureRange(readings))

# Problem 3: Check if its the Weekend
day = 8
def weekend(day):
    for i in range(day):
        if 6 <= i <= 7:
            print("True")
        else: 
            print("False")
weekend(day)

# Problem 4: Fuel Efficiency Calculator
def fuel (distance, fuel):
    efficiency = distance/fuel
    distance = 70 #miles
    fuel = 21.5 #gallons
    return efficiency
print(fuel(70, 21.5))

# # Problem 5: Secret Code
n = 12345
def decodeNumbers(n):
    five = n%20
    notfive = five * 10000
    move = n//10
    return notfive + move
print(decodeNumbers(n))

# Problem 6: Min & Max but with Loops!
# 6.1 For Loops
nums = [2024, 98, 131, 2, 3, 72]
def for_loop_min(nums):
   minimum = nums[0]
   for i in range(len(nums)):
    if nums[i] <= minimum:
        minimum = nums[i]
   return minimum
print(for_loop_min(nums))

def for_loop_max(nums):
   maximum = nums[0]
   for i in range(len(nums)):
    if nums[i] >= maximum:
        maximum = nums[i]
   return maximum
print(for_loop_max(nums))

# 6.2 While Loops
nums = [2024, 98, 131, 2, 3, 72]
def while_loop_min(nums):
   i = 0
   minimum = nums[0]
   while i < len(nums):
      if nums[i] < minimum:
         minimum = nums[i]
      i += 1
   return minimum
print(while_loop_min(nums))

def while_loop_max(nums):
   i = 0
   maximum = nums[0]
   while i > len(nums):
      if nums[i] > maximum:
         maximum = nums[i]
      i += 1
   return maximum
print(while_loop_max(nums))

# Problem 7: Counting Vowels
text = "UC Berkeley, founded in 1868!"
def letters(text):
    vowel_count = 0
    consonant_count = 0
    for letters in text:
        if letters in "AEIOUaeiou":
            vowel_count = vowel_count + 1
        elif letters in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
         consonant_count = consonant_count + 1
    return (vowel_count, consonant_count)
print(letters(text))

# # Problem 8: Calculate Digital Root
number = 2468
def digital_root(number):
   two = number // 1000
   four = 2 * two
   six = 3 * two
   eight = number % 10
   return two + four + six + eight
print(digital_root(number))