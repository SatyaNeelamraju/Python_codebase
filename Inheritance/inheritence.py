# inheriting as is from parent class
class Car:
    def __init__(self,model,mfdyr):
        self.model=model 
        self.mfdyr=mfdyr
    
    def start(self):
        print(f"Starting Engine for {self.model} {self.mfdyr} model")
    
    def stop(self):
        print(f"Stopping Engine for {self.model} {self.mfdyr} model")

class inh(Car):
    pass

#When the main function is written The code executes only when this file is executed
#when you import class from here to other file this file is also executed by default but its controlled 
#by main function.

if __name__ == "__main__":
    b = inh("BMW", "2024")
    b.start()
    b.stop()


