class Pokemon:
    def __init__(self, name, p_class):
        self.name = name
        self.p_class = p_class

    def use_power(self):
        print(f"{self.name}: Аааааа, ничего не хочу!")


pokemon = Pokemon('Нихачу', 'поддержка')

print(f"Покемон - {pokemon.name}, использует супер силу:")

pokemon.use_power()

