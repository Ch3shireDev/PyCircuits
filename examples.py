from circuit import Circuit
import matplotlib.pyplot as plt

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
