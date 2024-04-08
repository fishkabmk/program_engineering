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
        print(f"Лечу {self.__heal_power} хп")


pokemon = PokemonSupport('Нихачу')

print(f"Покемон - {pokemon.name}, класс - {pokemon.p_class}, использует супер силу:")

pokemon.use_power()
pokemon.heal()


