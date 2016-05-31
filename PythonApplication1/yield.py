#def gen():
#    for i in range(10):
#        X = yield i
#        print(X)

#G = gen()
#print G.next()
#G.send(77)
#print G.send(80)


def gensquares(N):
     for i in range(N):
         yield i ** 2

gen = gensquares(5)

print next(gen)
print next(gen)
ra = gensquares(6)
print next(ra)

G = (i for i in range(5))

print G.next()
print G
I = iter(G) # same iterator
print I

print '\n'

li = [i for i in range(5)]
I2, I3 = iter(li), iter(li) # different iterator
print I2, I3