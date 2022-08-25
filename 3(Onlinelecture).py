#Introduction to property decorator
class Employee():
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    @property
    def info(self):
        return self.name,self.sal

    @info.setter
    def info(self,name):
        self.name=name

obj=Employee("Adam",50000)
print(obj.info)

obj.info="Adam Willis"
print(obj.info)

#Abstract Property
from abc import ABC,abstractmethod,abstractproperty
class Company(ABC):

    @abstractmethod
    def info(self):
        None
    @abstractproperty
    def name(self):
        None

class Employee(Company):
    def __init__(self,ename):
        self.ename=ename

    def info(self):
        print(self.ename)
    @property
    def name(self):
        return self.ename

obj=Employee("SAM")
obj.info()
print(obj.ename)