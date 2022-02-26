import manynames

x=66
print(x)
print(manynames.x)

manynames.f()
manynames.g()
print(manynames.C.x)
I=manynames.C()
print(I.x) # tu pobieramy zmienną z klasy
I.m()
print(I.x) # a tu pobieramy zmienną z instancji, własna zmienna X z instancji jest tworzona dopiero gdy wywołamy metodę

x=11

def g1():
    print(x)
def g2():
    global x
    x=22
def h1():
    x=33
    def nested():
        print(x)
def h2():
    x=33
    def nested():
        nonlocal x
        x=44
    
