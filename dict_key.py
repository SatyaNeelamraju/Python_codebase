from attributes import attr
obj=attr(5)
print(attr.__dict__)
print("next")
print(obj.temp)
obj.__dict__["temp"]=10 # updating instance attribute through dict 
print(obj.temp)
obj.add()

### vars also work in the same way ###

print(vars(attr))
print(vars(obj))