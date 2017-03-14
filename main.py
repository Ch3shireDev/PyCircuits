#!/usr/bin/python

#Main file of a solution. In simple_example I keep my first working example, in circuit file there is developed class describing numerical
#system in object-oriented regime

from circuit import Circuit
from simple_example import example
import matplotlib.pyplot as plt

dt = 0.001
N = 10000
V0 = 100.

System = Circuit()

a = System.AddSource(V0)
b = System.AddNode()
c = System.AddNode()
d = System.AddGround()

ab = System.AddWire(a, b)
bc1 = System.AddWire(b, c)
bc2 = System.AddWire(b, c)
cd = System.AddWire(c, d)

Tab0 = []
Tab1 = []
Tab2 = []
Tab3 = []

for i in range(N):
    System.TimeStep()
    Tab0.append(ab.I)
    Tab1.append(bc1.I)
    Tab2.append(bc2.I)
    Tab3.append(cd.I)

Time = [i*dt for i in range(N)]

plt.plot(Time, Tab0, label="ab")
plt.plot(Time, Tab1, label="bc1")
plt.plot(Time, Tab2, label="bc2")
plt.plot(Time, Tab3, label="cd")

plt.legend(loc='upper right', shadow=True)
plt.show()

# example(dt, N)
