from hw_01.helpers import num

sum_of_numbers = 0
while(number := num(input("Please enter a number: "))) >= 0 :
    sum_of_numbers += number

print(sum_of_numbers)