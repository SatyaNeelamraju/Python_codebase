#Managed attributes decouple what users write from how the value is handled.
#You want to evolve the code behind an attribute without forcing end users to change how they use it
#This type of attribute prevents you from introducing breaking changes into your APIs

from datetime import datetime

class Age:
    def __init__(self,dob):
        self.dob=dob

        

    @dob.setter
    def dob(self,value):
        birth_year = datetime.strptime(value, "%Y-%m-%d").year
        if birth_year >= datetime.now().year:
            raise Exception ("Not a valid dob")
        self._dob=birth_year

    @property
    def dob(self):
        return datetime.now().year - self._dob
    
a=Age('2027-06-07')
print(a.dob)