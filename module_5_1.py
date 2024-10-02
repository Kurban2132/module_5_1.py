class House():                                      #Создаем класс House
    def __init__(self, name, number_of_floors):     #Создаем на основе класса House экземпляр.
        self.name = name
        self.number_of_floors = number_of_floors    #Вывод домов с этажами
        print(name, number_of_floors)



    def go_to(self, new_floor):
        self.new_floor = int()
        print(1, new_floor)  #Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).

        print(new_floor)                          #Выводить этаж для h1 и h2
        for new_floor in range(1, new_floor + 1): #Вывод количество этажей
            print(new_floor)

        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('"Такого этажа не существует"')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)



