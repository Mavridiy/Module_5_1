
class House:


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        first_floor = 1
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            while first_floor <= new_floor:
                print(first_floor)
                first_floor += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)









# Исходные данные:
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"
# Примечания:
# self - это переменная указывающая на объект. Используйте её для обращения к атрибутам или методам объекта.
# Обращение к атрибутам или методам объекта/класса происходит при помощи "."
# Метод __init__ вызывается в момент создания объекта.