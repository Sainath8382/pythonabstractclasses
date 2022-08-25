class MetaOne(type):
    def __new__(cls,clsname,basecls,clsdict):
        print("Im here")
        print(clsname)
        if(len(clsdict)==4):
            raise "TypeError: More than one class variable not allowed"
        return super().__new__(cls,clsname,basecls,clsdict)

class A(metaclass=MetaOne):
    x=10
    #y=20
    #print("A")
class b(A):
    print("B")
    p=20
    #q=30
class C(A):
    x=56
    #y=101
print(type(A))
print(type(b))