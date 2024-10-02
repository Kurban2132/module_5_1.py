class House():                                      #Создаем класс House
    def __init__(self, name, number_of_floors):     #Создаем на основе класса House экземпляр.
        self.name = name
        self.number_of_floors = number_of_floors    #Вывод домов с этажами
        print(name, number_of_floors)



    def go_to(self, new_floor):
        print(1, new_floor)  #Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')

        for new_floor in range(1, new_floor + 1): #Вывод количество этажей
            print(new_floor)
            





h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)



