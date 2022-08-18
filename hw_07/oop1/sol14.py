
class Actor:
    def __init__(self, first_name, last_name, salary, phrase):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary
        self.__phrase = phrase

    def print_phrase(self):
        print(f"and {self.__first_name} says : {self.__phrase}")

    def tip_actor(self, tip):
        if tip % 2 == 1 or self.__salary < 1000:
            self.__salary += tip
            print("tip accepted - thank you")
        else:
            print("no thank you - take back your tip")

brad_pit = Actor("bred", "pit", 999.99, "I am achiles")
brad_pit.print_phrase()
brad_pit.tip_actor(1)
brad_pit.tip_actor(2)
brad_pit.tip_actor(1)