

my_name = "Joe Bayden"

print(my_name[-5:])
first_third = len(my_name) // 3
print(my_name[:first_third])
print(my_name.count('a'))
print('b' in my_name)
print('B' in my_name)
my_name_list = my_name.split()
print(my_name_list)
my_name_list_reversed = list(reversed(my_name_list))
print(" ".join(my_name_list_reversed))
my_name_list_reversed[0] = my_name_list_reversed[0].upper()
print(" ".join(my_name_list_reversed))
middle = len(my_name_list_reversed[1]) // 2
if len(my_name_list_reversed[1]) % 2 == 0:
    my_name_list_reversed[1] = my_name_list_reversed[1][:middle-1] + my_name_list_reversed[1][middle+1:]
else:
    my_name_list_reversed[1] = my_name_list_reversed[1][:middle] + my_name_list_reversed[1][middle+1:]

print(" ".join(my_name_list_reversed))