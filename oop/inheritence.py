class animal:
    status = "alive"
    def sleep(self):
        print("bro this animal is sleeping")
    def eating(self):
        print("Sheesh this guy is sleeping")
class tiger(animal):
    pass
class radahn(animal):
    pass

tigerr = tiger()
radahnn = radahn()
print(tigerr.eating())