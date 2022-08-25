from abc import ABC,abstractmethod
class parent(ABC):
    def show(self):
        None
    def info(self):
        None
class Child(parent):
    def show(self):
        print("In self")
    def info(self):
        print("In def")

class Xyz:
    pass
obj=Child()
obj.show()
obj.info()
print(type(parent))
print(type(Child))
print(type(Xyz))
print(type(obj.info))


