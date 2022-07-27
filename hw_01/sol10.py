
from hw_01.helpers import num

math_addition_equation = input("please enter your addition equation: ")

addition_equation_list = math_addition_equation.split()
addition_equation_right_side = num(addition_equation_list[-1])

only_numbers = filter(lambda item: item != "+", addition_equation_list[:-2])
parsed_numbers = map(num, only_numbers)
calculated_sum = sum(parsed_numbers)

print(calculated_sum == addition_equation_right_side)

