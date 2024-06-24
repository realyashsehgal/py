class Car:
    def start(self):
        print("the car just started")
        return self
    def dirve(self):
        print("you just drove the car eh")
        return self
    def stop(self):
        print("Ayyooo you can stop this shit")
        return self
    def off(self):
        print("well ou just turned it off")
        return self
    
car = Car()
car.start(),car.dirve(),car.stop(),car.off()