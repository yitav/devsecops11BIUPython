from hw_01.helpers import num


def get_in_range(min_value, max_value):

    while True:
        number = num(input(f'Please enter a number in range {min_value} - {max_value} : '))
        if number >= min_value and number <= max_value:
            return number


print(get_in_range(10,100))
