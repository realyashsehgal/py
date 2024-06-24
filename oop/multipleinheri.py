class animal:
    status = "alive"
    def brething(self):
        print("Oh hell yeahh i can breathe")
class predators(animal):
    type = "Hunter"
    def hunt(self):
        print("go killem")
class prey(animal):
    type = "Gets hunted"
    def run(self):
        print("runs for his life")
class both(prey,predators):
    type = "Hunts but also get hunted lmao"
print("I am only going to call both one ")
fishes = both()
fishes.run()
fishes.hunt()