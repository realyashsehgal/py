class animal:
    def living(self):
        print("this animal is alive")
class tiger(animal):
    def living(self):
        print("Oh damnn the tiger is running")
creature = tiger()
creature.living()