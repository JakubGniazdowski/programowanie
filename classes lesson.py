class FirstClass:
    def setdata(self, value):
        self.data=value
    def display(self):
        print(self.data)


class SecoundClass(FirstClass):
    def display(self):
        print('aktualna wartość="%s"'% self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data=value
    def __add__(self, other):
        return ThirdClass(self.data+other)
    def __str__(self):
        return '[ThirdClass: %s]'% self.data
    def mul(self,other):
        self.data*=other
