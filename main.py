#!/usr/bin/python

#Main file of a solution. In simple_example I keep my first working example, in circuit file there is developed class describing numerical
#system in object-oriented regime

from circuit import Circuit
# from examples import example01
import matplotlib.pyplot as plt
from math import sin


dt = 0.001
N = 20000
V0 = 100.

System = Circuit(dt)
# a = System.AddAlternatingSource(lambda t: V0*sin(t))
a = System.AddSource(V0)
b = System.AddNode()
c = System.AddNode()
d = System.AddGround()

ab = System.AddResistor(a, b, 1)
bc0 = System.AddResistor(b, c, 1)
bc1 = System.AddResistor(b, c, 1)
cd = System.AddResistor(c, d, 1)

Tab0, Tab1, Tab2, Tab3 = [], [], [], []

for i in range(N):
    System.TimeStep()
    Tab0.append(ab.GetCurrent())
    Tab1.append(bc0.GetCurrent())
    Tab2.append(bc1.GetCurrent())
    Tab3.append(cd.GetCurrent())


Time = [i*dt for i in range(N)]

plt.plot(Time, Tab0)
plt.plot(Time, Tab1)
plt.plot(Time, Tab2)
plt.plot(Time, Tab3)
plt.show()