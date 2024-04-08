class Pokemon:
    def __init__(self, name):
        self.name = name

    def use_power(self):
        print(f"{self.name}: Кииия! минус 100хп.")


class PokemonSupport(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.p_class = 'поддержка'
        self.__heal_power = 20

    def heal(self):
        print(f"Лечу на {self.__heal_power} хп")

    def use_ability(self):
        print(f"Бафаю на +100 к атаке")


class PokemonWarrior(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.p_class = 'воин'
        self.__attack_rating = 90
        self.__attack_damage = 50

    def attack(self):
        print(f"Бью на {self.__attack_damage} хп")

    def use_ability(self):
        print(f"Контратака на {self.__attack_damage * 3} хп")


pokemon = PokemonSupport('Нихачу')
pokemon_war = PokemonWarrior('Лолхачу')

print(f"Покемон - {pokemon.name}, класс - {pokemon.p_class}, использует супервозможность:")

pokemon.heal()
pokemon.use_ability()


print(f"Покемон - {pokemon_war.name}, класс - {pokemon_war.p_class}, использует супервозможность:")

pokemon_war.attack()
pokemon_war.use_ability()

