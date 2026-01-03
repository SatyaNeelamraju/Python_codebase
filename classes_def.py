#simple class definition 
class CircleArea_1:
    
    def __init__(self,radius):
        self.pi=3.14
        self.radius=radius

    def area(self):
        return self.pi * self.radius ** 2