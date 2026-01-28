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

class even_nos:
    counter=0
    def __init__(self,num):
        self.num=num

    def finder(self):
        if self.num %2 ==0:    
            type(self).counter+=1 #type(self) can be replaced with self
        else:
            type(self).counter+=2  #type(self) can be replaced with self  
        print(self.counter)
        
class childcl(even_nos):
    counter=0

obje=even_nos(4)
obje2=even_nos(2)
obje1=childcl(3)
obje.finder()
obje2.finder()
obje1.finder()        

print(even_nos.__dict__)

#| Expression              | What it means               | Use case               |
#| ----------------------- | --------------------------- | ---------------------- |
#| `self.class_attr`       | Read attribute via instance | Reading values         |112
#| `self.class_attr += 1`  | Creates instance attr       | ⚠️ Usually a bug       |
#| `type(self).class_attr` | Access class attribute      | ✅ Correct for counters |122
#| `type(self.class_attr)` | Type of the value           | ❌ Not for class access |


# Key Difference: type(self).counter vs. self.counter

# type(self) refers to the class of the instance (e.g., even_nos for all instances in the test). So type(self).
# counter accesses and modifies the class-level attribute counter,which is shared by all instances of that class (and subclasses, unless overridden).
# self.counter creates instance attributes, which are unique to each object. Changes don't affect other instances or "carry over."
    
        
# instance attributes 

class attr:
    def __init__(self,tmp):
        self.temp=tmp
    
    def add(self):
        self.result=self.temp+1
        print(self.result)

o=attr(2)
o.add()


