# Author: Irene Buck
# Date: 7/27/23
# 100 Days of Code - Functions and Ceasar Cipher

import math

# Create a function with more than one parameter
def greet_with(name="Levi", location="Rocklin"):
    print(f"Hello, {name}.")
    print(f"What is the weather like in {location}?")

greet_with("Waylon", "Roseville")
greet_with()



# How much paint is needed to paint a wall?
def paint_calc(height, width, cover):
    cans_needed = (height * width)/cover
    cans_needed = math.ceil(cans_needed)
    print(f'You\'ll need {cans_needed} cans of paint.')

test_h = int(input("Height of wall in meters: "))
test_w = int(input("Width of wall in meters: "))
coverage = 5   # meters per can

paint_calc(height=test_h, width=test_w, cover=coverage)



# Prime Number Checker
def prime_checker(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return print("It's not a prime number.")
    print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)