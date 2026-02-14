class Vehicle:
    def __init__(self,model,yom,maxsp):
        self.model=model
        self.yom=yom
        self.maxsp=maxsp
    
    def message(self):
        print(f"The year of manufacturing for {self.model} is {self.yom} and max speed is {self.maxsp}"
              )
        
class Bike(Vehicle):
    def __init__(self, model,yom, maxsp,color):
        super().__init__(model,yom, maxsp)
        self.color=color

    def message(self):
        print(f"The year of manufacturing for {self.model} is {self.yom} and max speed is {self.maxsp} with {self.color}")

class Car(Vehicle):
    pass

if __name__ =="__main__":
    ob2=Bike("Fz","2024","180","Black")
    ob2.message()
    ob1=Car("BMW","2024","250")
    ob1.message()
