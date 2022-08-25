#Scenarios related to class ABC
#1 Blank class
from abc import ABC,abstractmethod
class A(ABC):
    None

obj=A() #No error thus object is created

#2 Concrete method without decorator
class B(ABC):
    def  info(self):
        print("In info")    #No error thus object is crreated

#3 Abstract Method
class C(ABC):
    @abstractmethod
    def dets(cls):
        pass

#obj=C() #Type error of instantiation

#4 Concrete method with abstract method decorator
class D(ABC):
    @abstractmethod
    def info(self):
        print("Info")

obj=D() #Same error of instantiation
