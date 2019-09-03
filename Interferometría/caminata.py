import numpy as np
import matplotlib.pyplot as plt 

a = np.array([-1, 1])

def prim():
    x = 0
    n=0
    while (x!=1):
        x = x + np.random.choice(a)
        n = n + 1

    return n

z = range(200)
b = np.zeros(200)
c = np.zeros(50)
d=np.zeros(100)
e=np.zeros(500)
g=np.zeros(1000)

for i in range(200):
    b[i] = prim()



plt.hist(b, 200)
plt.savefig('normal.pdf')
plt.figure()
b=b[range(100)]
plt.hist(b, 200)
plt.savefig('zoom.pdf')
plt.figure()
b=b[range(50)]
plt.hist(b, 200)
plt.savefig('zoom2.pdf')
plt.figure()
b=b[range(25)]
plt.hist(b, 200)
plt.savefig('zoom3.pdf')




for i in range(50):
    c[i] = prim()


for i in range(100):
    d[i] = prim()


for i in range(500):
    e[i] = prim()


for i in range(1000):
    g[i] = prim()

print np.mean(c)
print np.mean(d)
print np.mean(e)
print np.mean(g)



