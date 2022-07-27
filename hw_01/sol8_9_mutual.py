
from hw_01.helpers import num

def print_max_number(number_of_numbers):
    numbers = []
    for i in range(number_of_numbers):
        numbers.append(num(input("Enter the {} number :".format(i+1))))

    print(max(numbers))
