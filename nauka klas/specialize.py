class Super:
    def method(self):
        print("w Super method")
    def delegate(self):
        self.action()   #przekazanie działania metody do klasy podrzędnej 

class Inheritor(Super):
    pass
class Replacer(Super):
    def method(self):
        print("w Replacer.method")
class Extender(Super):
    def method(self):
        print("początek extender method")
        Super.method(self)
        print("koniec extender method")
class Provider(Super):
    def action(self):
        print("w provider.action")

if __name__ =='__main__':
    for klass in (Inheritor, Replacer,Extender):
        print('\n'+klass.__name__+'...')
        klass().method()  #wywołujemy metodę w zależności od zmiennej "klass" która przybiera postaci predefiniowanych klass
    print('\nProvider...')
    x=Provider()
    x.delegate()