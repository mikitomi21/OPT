class Player:
    def __init__(self, name):
        self.name = name
        self._age = 0
        # Skala wszystkich umiejetnosci 0-20
        self._health = 10
        self._power = 10
        self._loyal = 10
        self._money = 10
        self._isAlive = True

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
