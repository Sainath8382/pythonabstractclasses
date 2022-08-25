#concept Metaclass
class Xyz:
    pass
name="Sam"
age=27
sal=20.4
def fun():
    pass
print(type(Xyz))
print(type(name))
print(type(age))
print(type(sal))
print(type(fun))
print(type(fun()))
print(' ')
print(type(type(Xyz)))
print(type(type(name)))
print(type(type(age)))
print(type(type(sal)))
print(type(type(fun)))
print(type(type(fun())))
print(name.__class__)
