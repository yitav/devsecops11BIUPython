example_list_of_lists = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]

temp_min = example_list_of_lists[0][0]

for list_item in example_list_of_lists:
    for item in list_item:
        if item < temp_min:
            temp_min = item

print(temp_min)