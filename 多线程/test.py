from collections import defaultdict
values = defaultdict()

def deco(func):
    def _deco(*args, **kwargs):
        p = args.__getitem__(1)
        values['p'] = p
        func(*args, **kwargs)
    return _deco

class C():
    @deco
    def A(self, p):
        B()

def B():
    p = values.get('p')
    print(p)

c = C()
c.A(1)
c.A(2)
c.A(3)