

number = input('Please enter a number:')
number_list = list(number)
number_list_numbers = list(map(int, number_list))
print(sum(number_list_numbers))
