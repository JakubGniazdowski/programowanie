x=11
def f():
    print(x)

def g():
    x=22
    print(x)

class C:
    x=33
    def m(self):   #metoda 
        x=44
        self.x=55 #instancja, czemu instancja jest zakodowana w metodzie

if __name__=='__main__':
    print(x)
f()
g()
print(x)

obj=C()
print(obj.x)
obj.m()
print(obj.x)
print(C.x)

