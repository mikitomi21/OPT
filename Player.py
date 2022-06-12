class Player:
    def __init__(self, name):
        self._name = name
        self._age = 0
        # Skala wszystkich umiejetnosci 0-20
        self._health = 10
        self._power = 10
        self._loyal = 10
        self._money = 10
        self._isAlive = True

    def __del__(self):
        print(f"{self._name} umarl, zyl {self._age} lat")

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_health(self):
        return self._health

    def add_health(self, health):
        if self._health + health >= 20:
            self._health = 20
        else:
            self._health += health

    def get_power(self):
        return self._power

    def add_power(self, power):
        if self._power + power >= 20:
            self._power = 20
        else:
            self._power += power

    def get_loyal(self):
        return self._loyal

    def add_loyal(self, loyal):
        if self._loyal + loyal >= 20:
            self._loyal = 20
        else:
            self._loyal += loyal

    def get_money(self):
        return self._money

    def add_money(self, money):
        if self._money + money >= 20:
            self._money = 20
        else:
            self._money += money

    def get_isAlive(self):
        return self._isAlive

    def set_isAlive(self):
        if self._health <= 0 or self._power <= 0 or self._loyal <= 0 or self._money <= 0:
            self._isAlive = False
        else:
            self._age+=1

    def print_skills(self):
        print(f"Health: {self._health}")
        print(f"Power: {self._power}")
        print(f"Loyal: {self._loyal}")
        print(f"Money: {self._money}")

    def add_skills(self, skills):
        self.add_health(skills[0])
        self.add_power(skills[1])
        self.add_loyal(skills[2])
        self.add_money(skills[3])

