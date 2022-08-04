import math


def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


user_number = int(input('Please enter a number to compute factorial: '));

# 1st way
print(factorial(user_number))
# 2nd way
print(math.factorial(user_number))
