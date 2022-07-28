from statistics import mean

five_numbers_list = [8, 1000, -3, 2, 5]

print(sum(five_numbers_list))
print(max(five_numbers_list))
print(min(five_numbers_list))
print(mean(five_numbers_list))
five_numbers_list.pop(len(five_numbers_list) // 2)
print(five_numbers_list)
print(sorted(five_numbers_list))
print(five_numbers_list*5)
five_numbers_list.pop(0)
print(five_numbers_list)
print(list(filter(lambda number: number < mean(five_numbers_list), five_numbers_list)))
