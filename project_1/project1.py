from random import randint
import os
import csv
from functools import cmp_to_key

game_filename = "findTheTreasure.txt"
number_of_top_best = 10
top_best_filename = "topBest.csv"


def write_treasure_file():
    try:
        fi = open(game_filename, "wb")
        str_to_write = ""
        for i in range(10):
            str_to_write += str(i) * randint(1, 20)
        str_to_write += "TREASURE"
        for i in range(9, -1, -1):
            str_to_write += str(i) * randint(1, 20)
        fi.write(str_to_write.encode('ascii'))
        fi.close()
    except IOError:
        print("I/O error")


def get_file_size(_f):
    old_file_position = _f.tell()
    _f.seek(0, os.SEEK_END)
    size_ans = _f.tell()
    _f.seek(old_file_position, os.SEEK_SET)
    return size_ans


def play_game():
    try:
        f = open(game_filename, "r")
        size = get_file_size(f)
        counter = 1
        while True:
            direction = input("Where you want to move? [1- forward 2-backwards] \n")
            if not (direction == "1" or direction == "2"):
                print("illegal direction")
                continue
            steps = int(input("How many characters?\n"))
            new_position = 0
            if direction == "1":
                new_position = f.tell() + steps
            else:
                new_position = f.tell() - steps
            if new_position < 0 or new_position >= size:
                print("illegal steps")
                continue

            f.seek(new_position, os.SEEK_SET)
            char = f.read(1)
            f.seek(new_position, os.SEEK_SET)
            print(f" You hit \"{char}\"")
            if char in list("TREASURE"):
                print(f"Yow win - game ended with {counter} attempts")
                return counter
            counter += 1
        f.close()
    except IOError:
        print("I/O error")


def read_results_and_player_name(_number_of_attempts):
    try:
        with open(top_best_filename, "r") as f:
            reader = csv.reader(f, delimiter=",")
            _results_with_no_header = list(reader)[1:]
            _player_name = None
            if len(_results_with_no_header) == 0 or (int(_results_with_no_header[-1][1]) > _number_of_attempts):
                _player_name = input(f"You are on the top {number_of_top_best} - Please enter your name: \n")
            return _results_with_no_header, _player_name
    except FileNotFoundError:
        _player_name = input(f"You are on the top {number_of_top_best} - Please enter your name: \n")
        return [], _player_name


def compare(item1, item2):
    return int(item1[1]) - int(item2[1])


def write_results(_results_with_no_header, _player_name, _number_of_attempts):
    new_results = _results_with_no_header + [[_player_name, _number_of_attempts]]
    new_results_sorted = sorted(new_results, key=cmp_to_key(compare))
    with open(top_best_filename, 'w', newline='') as file:
        output = csv.writer(file, delimiter=',')
        output.writerows([
                             ["player name", "attempts"],
                         ] + new_results_sorted[:number_of_top_best])


write_treasure_file()
number_of_attempts = play_game()

results_with_no_header, player_name = read_results_and_player_name(number_of_attempts)

if player_name is not None:
    write_results(results_with_no_header, player_name, number_of_attempts)
