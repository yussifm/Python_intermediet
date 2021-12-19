class Character(object):
    def __init__(self,name,max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp =max_hp

    @property
    def hp(self):
        return self._hp

    @property
    def name(self):
        return self._name
    
    def take_damage(self, damage):
        self._hp -= damage
        self._hp = 0 if self._hp < 0 else self._hp

    @property
    def is_alive(self):
        return self._hp !=0

    @property
    def is_wounded(self):
        return self._hp < self._max_hp if self._hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive



player1 = Character("PlayeONe", 100)
print(player1.hp)
player1.take_damage(30)
print(player1.is_alive)
print(player1.is_wounded)
print(player1.hp)
print(player1.is_dead)
