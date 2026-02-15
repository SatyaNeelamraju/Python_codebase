class mul_only:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def validate(self):
        if not (isinstance(self.num1,int) and isinstance(self.num2,int)) :
            raise Exception ("Not a valid number")
    
    def mul(self):
        self.result=self.num1*self.num2
        print(f"The result after multiplication is {self.result}")


class add_mul_ops(mul_only):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
        super().validate()

    def add (self):
        super().mul()
        self.result=self.num1+self.num2
        print(f"The result after addition is {self.result}")

if __name__=="__main__":
    ob=add_mul_ops(2,3)
    ob.add()
