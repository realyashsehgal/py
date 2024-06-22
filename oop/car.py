class cars:#so here the class is declared
    wheels = 4 #this is class variable same for all instance until or unles changed ggs
    def __init__(self,name,model,year,color) :#this is a constructor
        self.name = name#So these are instance variable diffrent for all instances
        self.model = model
        self.year = year
        self.color = color#slef i refering to the object like  car_!
    def drive(self):
        print("weee wooo i can drive")
    def stop(self):
        print("oh no i cant drive")
        