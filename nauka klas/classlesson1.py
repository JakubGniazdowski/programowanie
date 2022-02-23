class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'działanie musi zostać zdefionowane' 

x=Super()
x.delegate()


class Sub(Super):pass

x=Super()
x.delegate()


class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('działąnie musi zoostać redefiniowane')
x=Super()
x.delegate()

class Sub(Super):
    def action(self): print("mielonka")

x=Super()
x.delegate()

