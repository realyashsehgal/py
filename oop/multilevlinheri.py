class organism:
    status = "alive"
    def breathing(self):
        print("yeah it is brething")
class animal(organism):
    def eats(self):
        print("duudde this animal can eat too")
class tiger(animal):
    def sleep(self):
        print("ayooo this animal is sleeping")
animal_1 = tiger()
print(animal_1.status)
print(animal_1.breathing())
print(animal_1.eats())
print(animal_1.sleep())