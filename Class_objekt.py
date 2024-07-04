class House:
    def __init__(self, name, number_of_floors=1):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        print(self.name)
        for i in range(1,new_floor +1):

            if i > self.number_of_floors:
                print('Такого этажа не существует')
                break
            else:
                print(i)
h1 = House('ЖК Горький', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(h1)
print(h2)







        #for f in range(0, 10):
            #f1 = f + 1
            #print('текущий этаж равен', f1)








