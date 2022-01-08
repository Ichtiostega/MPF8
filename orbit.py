import math as m
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.colors import Colormap

class Galaxy:
    def __init__(self, x, y, Vx, Vy, dt=24*60*60):
        self.G = 6.67408E-11
        self.Ms = 1.989E30
        self.AU = 149597870700

        self.x = x
        self.y = y
        self.Vy = Vy * self.AU
        self.Vx = Vx * self.AU
        
        self.dt = dt

    def iterate(self):
        r = m.sqrt(self.x**2 + self.y**2)

        self.Vx -= self.G * self.Ms * self.x * self.dt / (self.AU**2 * r**3)
        self.Vy -= self.G * self.Ms * self.y * self.dt / (self.AU**2 * r**3)

        self.x += self.Vx * self.dt / self.AU
        self.y += self.Vy * self.dt / self.AU

dt = 60*60

# EARTH

g = Galaxy(1,0,0,2*m.pi/(365*24*60*60), dt)

eX = [g.x]
eY = [g.y]
g.iterate()
eX.append(g.x)
eY.append(g.y)
fin = [g.x, g.y]
ei = 0
while g.x <= fin[0] or g.y >= fin[1]:
    ei += 1
    g.iterate()
    eX.append(g.x)
    eY.append(g.y)

plt.plot([0,0], [-1.2, 1.2], color='#999999')
plt.plot([-1.2, 1.2], [0,0], color='#999999')
plt.plot([0], [0], 'or')
plt.plot(eX, eY, label='Ziemia')
plt.title(f'Ziemia')
plt.xlabel('x[AU]')
plt.ylabel('y[AU]')
plt.legend()
plt.savefig("earth.png")
plt.clf()

# VENUS

g = Galaxy(0.72,0,0,2*0.72*m.pi/(365*24*60*60*0.62), dt)

vX = [g.x]
vY = [g.y]
g.iterate()
vX.append(g.x)
vY.append(g.y)
fin = [g.x, g.y]
vi = 0
while g.x <= fin[0] or g.y >= fin[1]:
    vi += 1
    g.iterate()
    vX.append(g.x)
    vY.append(g.y)

plt.plot([0,0], [-1.2, 1.2], color='#999999')
plt.plot([-1.2, 1.2], [0,0], color='#999999')
plt.plot([0], [0], 'or')
plt.plot(vX, vY, label='Venus')
plt.title(f'Venus')
plt.xlabel('x[AU]')
plt.ylabel('y[AU]')
plt.legend()
plt.savefig("venus.png")
plt.clf()

# BOTH

plt.plot([0,0], [-1.2, 1.2], color='#999999')
plt.plot([-1.2, 1.2], [0,0], color='#999999')
plt.plot([0], [0], 'or')
plt.plot(eX, eY, label='Ziemia')
plt.plot(vX, vY, label='Wenus')
plt.title(f'Ziemia i Wenus')
plt.xlabel('x[AU]')
plt.ylabel('y[AU]')
plt.legend()
plt.savefig("ev.png")
plt.clf()

# PARAMS

eRs = [m.sqrt(x**2 + y**2) for x, y in zip(eX, eY)]
vRs = [m.sqrt(x**2 + y**2) for x, y in zip(vX, vY)]

max_er = max(eRs)
min_er = min(eRs)
max_vr = max(vRs)
min_vr = min(vRs)

ee = (max_er - min_er) / (max_er+min_er)
ve = (max_vr - min_vr) / (max_vr+min_vr)

eT = ei * dt / (365.25 * 24 * 60 * 60)
vT = vi * dt / (365.25 * 24 * 60 * 60)

ea = (max(eX) - min(eX)) / 2
eb = (max(eY) - min(eY)) / 2
va = (max(vX) - min(vX)) / 2
vb = (max(vY) - min(vY)) / 2

print(f'EARTH: a={ea}, b={eb}, e={ee}, T={eT}')
print(f'VENUS: a={va}, b={vb}, e={ve}, T={vT}')