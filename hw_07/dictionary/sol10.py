
my_dictionary = {}

while (id_number:= input("Please enter id number : ")) != "-1":

    if id_number in my_dictionary:
        print("error - id number already in dictionary")
    else:
        fullname = input("Please enter full name : ")
        my_dictionary[id_number] = fullname

print(my_dictionary)