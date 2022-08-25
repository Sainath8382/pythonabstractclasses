from abc import ABC, abstractmethod
class Car(ABC):
    def properties(self):
        print("Sedan")
    @abstractmethod
    def parts(self):
        pass
class Components(Car):
    def parts(self):
        print("Engine")
class Comp2(Car):
    def parts(self):
        print("Tyre")

class Comp3(Car):
    def parts(self):
        print("Ac")

obj=Components()
obj.properties()
obj.parts()
obj=Comp2()
obj.parts()
obj=Comp3()
obj.parts()
