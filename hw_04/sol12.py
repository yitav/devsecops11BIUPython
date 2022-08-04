import random

max_number_of_guesses = 20
luck_numbers_list = random.sample(range(2, 50), 5)
guesses_list = []

print(luck_numbers_list)

counter = 0;
while len(luck_numbers_list) > 0:

    guess_number = int(input(f'Please make your {counter + 1} number guess : '))

    if guess_number < 1 or guess_number > 49:
        continue

    counter += 1

    if guess_number in guesses_list:
        print('You guessed a number twice - now exiting')
        break;

    guesses_list.append(guess_number)

    if guess_number in luck_numbers_list:
        print("you made a hit")
        luck_numbers_list.remove(guess_number)
    else:
        print("Wrong guess - try again")
    if counter >= max_number_of_guesses and len(luck_numbers_list) > 0:
        print(f'Your number of guesses : {counter} is too high - starting the game again')
        luck_numbers_list = random.sample(range(2, 50), 5)
        guesses_list = []
        counter = 0;
        print(luck_numbers_list)

print(f'The number of guesses was {counter}')