"""
    * Become a Pokèmon master 
"""


class Pokemon:
    """A class for creating Pokemons"""

    def __init__(self, name, level, ptype):
        self.name = name
        self.type = ptype
        self.level = level
        self.max_health = level * 5
        self.current_health = level * 5
        self.is_knocked_out = False

    def __repr__(self):
        return f"'{self.name}' is a type of '{self.type}' pokemon \
with current health of '{self.current_health}' and hes knocked out status is '{self.is_knocked_out}'"
    
    def knock_out(self):
        self.is_knocked_out = True

    def revive(self):
        pass

    def lose_health(self, type, health):
        if self.current_health <= 0:
            self.is_knocked_out = True
            return "Whoops, your Pokemon is out."
    
    def gain_health(self):
        pass

    def attack(self):
        pass


charmander = Pokemon('Charmander', 1, 'fire', 20, 20, False)
print(charmander)
