
class SuperHero:
    def __init__(self, name):
        self.__name = name
        print("new super hero is born")


class Flyer(SuperHero):

    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{ self._SuperHero__name } is flying")


class Climber(SuperHero):

    def __init(self,name):
        super().__init__(name)

    def climb(self):
        print(f"{self._SuperHero__name} is climbing")

class Speeder(SuperHero):
    def __init__(self,name):
        super().__init__(name)

    def forceSpeed(self):
        print(f"{self._SuperHero__name} is force speeding")


superman = Flyer("Clark Kent")
superman.fly()

hulk = Climber("Bruce Banner")
hulk.climb()

flash = Speeder("Barry Allen")
flash.forceSpeed()