# File person.py

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name=name
        self.job= job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))
    def __str__(self):
        return '[Person:%s,%s]'%(self.name,self.pay)






if __name__=='__main__':
    bob=Person('Robert zieliński')
    anna=Person('Anna Czerwona', job='programista',pay=100000)
    print(bob)
    print(anna)
    print(bob.lastName(),anna.lastName())
    anna.giveRaise(.10)
    print(anna)

