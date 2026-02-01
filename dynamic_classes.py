class demo1:
    pass

s=demo1()
s.price=50
s.quan=3
print(f'printing inst attrs 1st time {s.__dict__}')

def __init__(self,price,quan):
    self.price=price
    self.quan=quan

def calc(self):
    self.total=self.price*self.quan
    print(self.total)

demo1.__init__=__init__
demo1.calc=calc
print(f'printing class attrs {demo1.__dict__}')

s.calc()

print(f'printing class attrs 2nd time {demo1.__dict__}')