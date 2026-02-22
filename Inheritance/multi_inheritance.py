#In single inheritance, you can call the parent using the class name directly (e.g., A.__init__(self)), but it’s better to use super().
#super() follows Python’s MRO, keeps the code flexible, and prevents issues if you later add multiple inheritance.
#So even in single inheritance, using super() is the recommended and future-proof approach. It resolved diamond problem.

#        A
#       / \
#      B   C
#       \ /
#        D

#Every class must call super()

#Use **kwargs if parameters differ

#Never directly call parent classes

#Keep signatures cooperative

class Device:
    def __init__(self,device_id,location,**kwargs):
        super().__init__(**kwargs)
        self.device_id=device_id
        self.location=location
    
    def device_info(self):
        print(f"The {self.device_id} is discovered at {self.location}")

class Camera(Device):
    def __init__(self,resolution,**kwargs):
        super().__init__(**kwargs)
        self.resolution=resolution

    def record(self):
        print(f"{self.resolution} video is recorded using {self.device_id} at {self.location} ")    

    def capture_image(self):
        print(f"{self.resolution} image is clicked using {self.device_id} at {self.location}")


class Alarm(Device):
    def __init__(self,alarm_type,**kwargs):
        super().__init__(**kwargs)
        self.alarm_type=alarm_type

    def trigger_alarm(self):
        print(f"Alarm type {self.alarm_type} is found at location {self.location}")    

    def stop_alarm(self):
        print("Stop the alarm")

class SmartSecurityDevice(Camera,Alarm):
    def __init__(self,battery_level,device_id,location,resolution,alarm_type):
        super().__init__(
# has to explicitly mention paramaters to avoid positioning paramterization 
            resolution=resolution,
            alarm_type=alarm_type,
            device_id=device_id,
            location=location
            
            )
        self.battery_level=battery_level

    def emergency(self):
        print(f"Emergency, Batter level is down {self.battery_level} in {self.location}")
    

if __name__=="__main__":
    obj=SmartSecurityDevice("1percent","123","India","4k","snooze")
    obj.emergency()