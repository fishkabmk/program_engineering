# Садовник и помидоры
class Tomato:
    states = ["отсутствует", "цветение", "зеленый", "красный"]  # Статичный атрибут со списком стадий роста томата

    def __init__(self, index):
        '''
        Класс томат
        :param index: Защищенный атрибут
        :param state: Защищенный атрибут
        '''
        self._index = 0
        self._state = Tomato.states[self._index]

    def grow(self):
        '''
        Метод роста томата
        Каждый раз при вызове метода, томат переходит на новую стадию роста, если еще не поспел
        '''
        if not self.is_ripe():
            self._index += 1
            self._state = Tomato.states[self._index]

    def is_ripe(self):
        '''
        Метод проверки томата на зрелость
        :return: Возвращает True если томат поспел
        '''
        if self._state == "красный":
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, tomatoes_count):
        self.tomatoes = []
        for t_idx in range(tomatoes_count):
            self.tomatoes.append(Tomato(t_idx))

    def grow_all(self):
        '''
        Метод вызывает рост всех томатов на кусте при вызове
        '''
        for t in self.tomatoes:
            if not t.is_ripe():
                t.grow()

    def all_are_ripe(self):
        '''
        Метод проверяет все ли томаты на кусте поспели
        :return: Возвращает True если томаты на кусте поспели
        '''
        ripe_cnt = 0
        for t in self.tomatoes:
            if t.is_ripe():
                ripe_cnt += 1
        if ripe_cnt == len(self.tomatoes):
            return True
        else:
            return False

    def give_away_all(self):
        '''
        Метот убирает томаты с куста, после сборки урожая
        '''
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, tomatoBush):
        '''
        Класс садовник
        :param name: Публичный атрибут
        :param tomatoBush: Защищенный атрибут
        '''
        self.name = name
        self._plant = tomatoBush

    def work(self):
        print(f"Садовник {self.name} ухаживает за кустом")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(
                f"Садовник {self.name} собирает урожай: Помидоры поспели, количество помидоров: {len(self._plant.tomatoes)}")
            self._plant.give_away_all()
        else:
            print(f"Садовник {self.name} собирает урожай: Не все помидоры на кусте созрели")

    @staticmethod
    def knowledge_base():
        print(f"Справка по садоводству: \n"
              f"Садовник собирает урожай с куста, если все помидоры на кусте созрели. \n")


Gardener.knowledge_base()
plant = TomatoBush(5)  # Садим куст с пятью помидорами
gardener = Gardener("Василий", plant)  # Нанимаем садовника Василия, ухаживать за кустом

gardener.work()  # Василий ухаживает за кустом
gardener.work()  # Василий ухаживает за кустом
gardener.harvest()  # Василий пытается собрать урожай
gardener.work()  # Василий ухаживает за кустом
gardener.harvest()  # Василий пытается собрать урожай
