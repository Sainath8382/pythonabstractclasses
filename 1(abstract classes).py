from abc import ABC, abstractmethod
class Parent(ABC):
    def property(self):
        print("Property")
    @abstractmethod
    def marry(self):
        pass
class Child(Parent):
    def marry(self):
        print("Def")

obj=Child()
obj.property()
obj.marry()
