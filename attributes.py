# Simple use of class attribute 
class demo:
    total = 600
    def __init__(self,marks):
        self.marks=marks
        print(marks)

    def calc_percent(self):
        self.percent=(self.marks/demo.total)*100
        print(self.percent)       

# d=demo(570)
# d.calc_percent()

#Alternative use of class attribute in inheritance


class premium_customers:
    disc = 0.1
    def __init__(self,price):
        self.price = price
        print(self.price)
    def calc_disc(self):
        self.price=self.price-(self.price*(self.disc))  
        #python checks for if disc value is from instance attributes if not from class 
    #attributes then the super class 

        print(self.price)

class normal_customers(premium_customers):
    disc=0.05

# obj1= premium_customers(1000)
# obj1.calc_disc()
# obj2=normal_customers(1000)
# obj2.calc_disc()

#updating class atrribute 
# updating counter by 1 if it is even and 2 if it is odd but the counter is updated by 3 when it is odd 

class even_nos:
    counter=0
    def __init__(self,num):
        self.num=num

    def finder(self):
        if self.num %2 ==0:    
            even_nos.counter+=1
        else:
            even_nos.counter+=2    
        print(even_nos.counter)
        
class childcl(even_nos):
    counter=0

# obje=even_nos(4)
# obje1=childcl(3)
# obje.finder()
# obje1.finder()

# works as expected when class attribute is not called with class.attribute 

class even_nos:
    counter=0
    def __init__(self,num):
        self.num=num

    def finder(self):
        if self.num %2 ==0:    
            type(self).counter+=1
        else:
            type(self).counter+=2    
        print(self.counter)
        
class childcl(even_nos):
    counter=0

obje=even_nos(4)
obje2=even_nos(2)
obje1=childcl(3)
obje.finder()
obje2.finder()
obje1.finder()
        



    
        

