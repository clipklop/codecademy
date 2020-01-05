"""
    * Become a Pokèmon master 
"""


class Pokemon:
    """A class for creating Pokemons"""

    def __init__(self, name, ptype, level):
        self.name = name
        self.type = ptype
        self.level = level
        self.max_health = level * 5
        self.current_health = level * 5
        self.is_knocked_out = False

    def __repr__(self):
        return f"'{self.name}' is a type of '{self.type}' pokemon \
with current health of '{self.current_health}' and his knocked out status is '{self.is_knocked_out}'"
    
    def knock_out(self):
        self.is_knocked_out = True
        if self.current_health != 0:
            self.current_health = 0
        print('Whoops, {} Pokemon was knocked out.'.format(self.name))

    def revive(self):
        self.is_knocked_out = False

        if self.current_health <= 0:
            self.current_health = 1
        print('Hooray! {} Pokemon has been revived.'.format(self.name))

    def lose_health(self, health):
        self.current_health -= health

        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print("Ouch, {} now has {}".format(self.name, self.current_health))
    
    def gain_health(self, health=2):
        if self.current_health == 0:
            self.revive()
        
        self.current_health += health

        if self.current_health >= self.max_health:
            self.current_health = self.max_health
        print('Good! You healed, and now have {} health.'.format(self.current_health))

    def attack(self, other_pokemon):
        if other_pokemon.is_knocked_out:
            print("{} can't attack {} anymore because it's knocked out!".format(self.name, other_pokemon.name))
            return
        
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print("{} attacked {} for {} damage.".format(self.name, other_pokemon.name, round(self.level * 0.5)))
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        
        if (self.type == other_pokemon.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)

        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)


class Trainer:
    def __init__(self, pokemons, name, potions):
        self.pokemons = pokemons
        self.name = name
        self.potions = potions
        self.active_pokemon = 0

    def __repr__(self):
        print("The trainer {} has the following pokemons:".format(self.name))
        [print("\t{} level {}".format(pokemon.name, pokemon.level)) for pokemon in self.pokemons]
        return "The current active pokemon is {}".format(self.pokemons[self.active_pokemon].name)

    def switch_pokemons(self, new_poke):
        if new_poke < len(self.pokemons) and new_poke >= 0:
            if self.pokemons[new_poke].is_knocked_out:
                print("Soz, you can't choose a pokemon that already knocked out.")
                return
            elif new_poke == self.active_pokemon:
                print("You won't belive but {} is already your active pokemon".format(self.pokemons[new_poke].name))
                return
            else:
                self.active_pokemon = new_poke
                print("Go {}, it's your turn now!".format(self.pokemons[new_poke].name))

    def use_potions(self):
        if self.potions > 0:
            print("You used one healing potion on {}".format(self.pokemons[self.active_pokemon].name))
            self.pokemons[self.active_pokemon].gain_health()
            self.potions -= 1
        else:
            print("Soz, no more potions for you.")

    def attack_other_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.active_pokemon]
        other_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
        
        my_pokemon.attack(other_pokemon)



class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)


charmander2 = Charmander(2)
squirtle3 = Squirtle(3)
bulbasaur4 = Bulbasaur(4)
charmander1 = Charmander(1)
squirtle4 = Squirtle(5)
bulbasaur2 = Bulbasaur(2)

# while bulbasaur.current_health > 0:
#     squirtle.attack(bulbasaur)

trainer_senya = Trainer([charmander2, squirtle3, bulbasaur4], 'Senya', 2)
trainer_mom = Trainer([charmander1, squirtle4, bulbasaur2], 'Mom', 3)

# print(trainer_mom)

trainer_mom.switch_pokemons(2)

trainer_senya.attack_other_trainer(trainer_mom)
trainer_senya.attack_other_trainer(trainer_mom)
trainer_senya.attack_other_trainer(trainer_mom)
trainer_senya.attack_other_trainer(trainer_mom)
trainer_senya.attack_other_trainer(trainer_mom)

trainer_mom.use_potions()


"""
    # TO-DO:

1. Give Pokémon experience for battling other Pokémon. 
    A Pokémon’s level should increase once it gets enough experience points.
2. Create specific Classes that inherit from the general Pokémon class.
    For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
3. Let your Pokémon evolve once they hit a certain level.
4. Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense.
     All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.
"""
