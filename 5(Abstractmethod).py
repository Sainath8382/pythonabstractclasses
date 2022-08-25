from abc import ABC,abstractmethod
class Company(ABC):
    @abstractmethod
    def address(self):
        pass

class emp(Company):
    def address(self):
        print("CYberciTY")

obj=emp()
obj.address()
#obj2=Company() Type Error

