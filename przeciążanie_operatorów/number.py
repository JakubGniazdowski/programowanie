


class Number:
    def __init__(self, start):
        self.data= start
    def __sub__(self, other):
        return Number(self.data - other)

X=Number(5)
Y=X-2
Y.data

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X=Indexer()
X[2]
for i in range(5):
    print(X[i])

class Indexer:
    data=[5,6,7,8,9]
    def __getitem__(self, index):
        print('getitem:',index)
        return self.data[index]

X=Indexer()
X[0]
X[1]
X[-1]

class steper:
    def __getitem__(self, i):
        return self.data[i]
X= steper()
X.data="Mielonka"
X[1]
for item in X:
    print(item)

[c for c in X]
list(map(str.upper, X))


class Squares:
    def __init__(self,start,stop):
        self.value = start
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.value==self.stop:
            raise StopIteration
        self.value +=1
        return self.value ** 2

for i in Squares(1,5):
    print(i)
