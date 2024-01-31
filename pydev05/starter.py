class Myclass:
    i = 123

    def f(self):
        return 'Hello world!'


x = Myclass()
print(f'x.i = {x.i},\nx.f = \'{x.f()}\'')


class MyComplex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart


x = MyComplex(3.0, -4.5)

print('{} {}i'.format(x.r, x.i))

x = Myclass()
xf = x.f

for i in range(4):
    print( xf() )
