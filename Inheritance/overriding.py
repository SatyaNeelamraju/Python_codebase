class common:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        self.result=self.num1+self.num2
        print(f"The sum of numbers is {self.result} which is not absolute")

class abs_add(common):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
    
    def add(self):
        self.result = abs(self.num1)+abs(self.num2)
        print(f"The absolute result is {self.result}")

if __name__=="__main__":
    obj=common(-3,-6)
    obj.add()
    ob=abs_add(-3,-6)
    ob.add()
