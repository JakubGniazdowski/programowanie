class MixedNames:
    data="mielonka"
    def __init__(self,value):
        self.data=value
    def display(self):
        print(self.data, MixedNames.data)

# x=MixedNames(1)
# y=MixedNames(2)
# x.display(); y.display()

class NextClass:
    def printer(self, text):
        self.message=text
        print(self.message)

x=NextClass()
x.printer("wywo³anie isntancji")
x.message

NextClass.printer(x,"wywo³anie klasy")
x.message





class Super:
    def method(self):
        print('w Super.method')

class Sub(Super):
    def method(self):
        print("poczatek Sub.method")
        Super.method(self)
        print('koniec Sub.method')

x=Super()
x.method()

x=Sub()
x.method()
