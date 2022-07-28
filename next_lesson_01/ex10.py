
numbers_list = [1, 5, 7, 8, 100]

temp_max = numbers_list[0]
for item in numbers_list:
    if item > temp_max:
        temp_max = item

print(temp_max)