class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(name, number_of_floors)


    def go_to(self, new_floor):
        floor = 0
        print(new_floor)

        print(f"Дом {self.name} имеет {self.number_of_floors} этажей \n Поднимаемся на {new_floor} - й")

        if new_floor > self.number_of_floors or new_floor < 1:
            print(floor + 1)


        else:
            for floor in range(new_floor):
                print(f"{new_floor + 1} - Такого этажа не существует")




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(18)
h2.go_to(2)

