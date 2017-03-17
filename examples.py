from circuit import Circuit
import matplotlib.pyplot as plt

def FoxPropagationTest(n = 200):
    '''Propagation test proposed by friend.
    Current model generates some inertia depending on wires number.''' 
    dt = 0.001
    V0 = 100.
    N = 100


    Tab0, Tab1 = [], []

    System1 = Circuit(dt)
    a = System1.AddSource(V0)
    b = System1.AddGround()

    R = 200.

    ab0 = System1.AddResistor(a, b, R)

    for i in range(N):
        System1.TimeStep()
        Tab0.append(ab0.GetCurrent())

    Time0 = [i*dt for i in range(N)]

    plt.plot(Time0, Tab0)

    System2 = Circuit(dt)
    a = System2.AddSource(V0)
    b = System2.AddNode()
    ab1 = System2.AddResistor(a, b, R/n)

    for i in range(n-2):
        c = System2.AddNode()
        bc = System2.AddResistor(b, c, R/n)
        b = c

    d = System2.AddGround()
    bd = System2.AddResistor(b, d, R/n)

    for i in range(N):
        System2.TimeStep()
        Tab1.append(bd.GetCurrent())

    Time1 = [i*dt for i in range(N)]



    plt.plot(Time1, Tab1)
    plt.show()

def example01():

    dt = 0.001
    N = 10000
    V0 = 100.
    
    System = Circuit()
    a = System.AddSource(V0)
    b = System.AddNode()
    c = System.AddNode()
    d = System.AddGround()

    ab = System.AddResistor(a, b, 1)
    bc0 = System.AddResistor(b, c, 1)
    bc1 = System.AddResistor(b, c, 1)
    cd = System.AddResistor(c, d, 1)

    Tab0 = []
    Tab1 = []
    Tab2 = []
    Tab3 = []

    for i in range(N):
        System.TimeStep()
        Tab0.append(ab.I)
        Tab1.append(bc0.I)
        Tab2.append(bc1.I)
        Tab3.append(cd.I)

    Time = [i*dt for i in range(N)]

    plt.plot(Time, Tab0, label="ab")
    plt.plot(Time, Tab1, label="bc0")
    plt.plot(Time, Tab2, label="bc1")
    plt.plot(Time, Tab3, label="cd")

    plt.legend(loc='upper right', shadow=True)
    plt.show()


### from simple_example.py:
#
#File for first working example I was able to code. Since it's very simple it doesn't give much information, but using this function
#I was able to compare later class with this solution. Shape of the system:

#             |---[  ]---|
# V0 o--[  ]--o          o---[  ]---o Ground
#             |---[  ]---|
#
# All resistors ( [  ] ) have resistance 1 Ohm, V0 is 100 V
#

import matplotlib.pyplot as plt

def example(dt, N):
    V0 = 100.
    V3 = 0.
    
    r0 = 1.
    r1 = 1.
    r2 = 1.
    r3 = 1.

    I0 = 0.
    I1 = 0.
    I2 = 0.
    I3 = 0.

    V1 = 0.
    V2 = 0.

    V3 = 0.

    Tab0 = []
    Tab1 = []
    Tab2 = []

    for i in range(N):
        
        I0 += (V0 - V1 - r0*I0)*dt
        #branches
        #branch 1
        I1 = I0 - I2
        #branch 2
        I2 += (V1 - V2 - r2*I2)*dt

        #branch 1
        I3 = I1 + I2

        V1 = (V0 - r0*I0) + (V2 + r1*I1) + (V2 + r2*I2)
        V1 /= 3

        V2 = (V1 - I1*r1) + (V1 - I2*r2) + (V3 + I3*r3)
        V2 /= 3

        Tab0.append(I0)
        Tab1.append(I1)
        Tab2.append(I3)


    Time = [i*dt for i in range(N)]
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.plot(Time, Tab0, label="1")
    plt.plot(Time, Tab1, label="2")
    plt.plot(Time, Tab2, label="3")
    plt.legend(loc='upper right', shadow=True)
    plt.show()
