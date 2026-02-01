from attributes import attr
obj=attr(5)
# print(attr.__dict__)
# print("next")
# print(obj.temp)
obj.__dict__["temp"]=10 # updating instance attribute through dict 
# print(obj.temp)
obj.add()
print(vars(attr))
print(vars(obj))