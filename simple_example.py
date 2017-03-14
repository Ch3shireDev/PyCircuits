#File for first working example I was able to code. Since it's very simple it doesn't give much information, but using this function
#I was able to compare later class with this solution. Shape of the system:

#             |---[  ]---|
# V0 o--[  ]--o          o---[  ]---o Ground
#             |---[  ]---|
#
# All resistors ( [  ] ) have resistance 1 Ohm, V0 is 100 V

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
