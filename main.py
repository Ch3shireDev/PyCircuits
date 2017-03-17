#!/usr/bin/python

from circuit import Circuit
import matplotlib.pyplot as plt

V0 = 100
R0 = 100.
dt = 0.001
N = 200

Tab0, Tab1, Tab2, Tab3 = [], [], [], []
Time = [i*dt for i in range(N)]

def GetTab(n):
    global dt, V0, R0

    R = R0/n

    System = Circuit(dt)
    a = System.AddSource(V0)
    b = System.AddNode()
    ab = System.AddResistor(a, b, R)

    for i in range(n-2):
        c = System.AddNode()
        bc = System.AddResistor(b, c, R)
        b = c

    d = System.AddGround()
    cd = System.AddResistor(c, d, R)

    Tab = []
    for i in range(N):
        System.TimeStep()
        Tab.append(ab.GetCurrent())

    return Tab


plt.plot(Time, GetTab(5), label="5 resistors")
plt.plot(Time, GetTab(20), label="20 resistors")

plt.legend(loc='upper right', shadow=True)
plt.show()