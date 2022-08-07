from hw_01.helpers import num


def add(y, x=0):
    return x + y


def sub (y, x=0):
    return y - x


def mul(y, x=0):
    return x * y


def div(y, x=1):
    return y / x


number1 = num(input("Please enter your 1st number: "))
number2 = num(input("Please enter your 2nd number: "))

print('add:', add(number1, number2))
print('sub:', sub(number1, number2))
print('mul:', mul(number1, number2))
print('div:', div(number1, number2))
