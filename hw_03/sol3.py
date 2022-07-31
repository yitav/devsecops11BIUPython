from hw_01.helpers import num
from statistics import mean

number_of_numbers = 7
numbers = []
for i in range(number_of_numbers):
    numbers.append(num(input(f'Please enter the {i + 1} number:')))

print(mean(numbers))