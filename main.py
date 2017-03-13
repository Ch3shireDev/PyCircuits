#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
N = 10000

I0 = 0.
I1 = 0.
I2 = 0.
I3 = 0.

V0 = 100.

V1 = 0.
V2 = 0.
V3 = 0.
V4 = 0.
V5 = 0.
V6 = 0.
V7 = 0.

r0 = 1.
r1 = 1.
r2 = 1.
r3 = 1.

Tab0 = np.array([])
Tab1 = np.array([])
Tab2 = np.array([])
Tab3 = np.array([])

for i in range(N):
    
    I0 += (V0 - V3 - r0*I0)*dt
    V1 = V3 + r0*I0
    V2 = V0 - r0*I0

    #branches

    #branch 1

    I1 = I0 - I3
    V3 = V5 + r1*I1
    V4 = V2 - r1*I1

    #branch 2

    I3 += (V2 - V5 - r3*I3)*dt

    #branch 1

    I2 = I1 + I3

    V5 = V7 + r2*I2
    V6 = V4 - r2*I2

    Tab0 = np.append(Tab0, I0)
    Tab1 = np.append(Tab1, I1)
    Tab2 = np.append(Tab2, I2)
    Tab3 = np.append(Tab3, I3)


Time = np.arange(N)*dt
plt.ticklabel_format(useOffset=False, style='plain')
plt.plot(Time, Tab0, label="1")
plt.plot(Time, Tab1, label="2")
plt.plot(Time, Tab2, label="3")
plt.plot(Time, Tab3, label="4")
plt.legend(loc='upper right', shadow=True)
plt.show()

# class Wire:
#     R = 1.
#     L = 1.
#     I = 0.

#     InWires = []
#     OutWires = []

#     VIn = 0.
#     VOut = 0.

#     def __init__(self):
#         self.InWires = []
#         self.OutWires = []
#         self.R = 1.
#         self.L = 1.
#         self.I = 0.

#         self.VIn = 0.
#         self.VOut = 0.

#     def TimeStep(self, flag = False, dt=0.001):
        
#         VOut = self.GetVOut()
#         VIn = self.GetVIn()

#         if len(self.InWires) == 0:
#             DeltaV = VIn - VOut
#             self.I += (DeltaV - self.I*self.R)*dt/self.L

#         else:
#             self.I = 0.
#             for wire in self.InWires:
#                 self.I += wire.I

#         if len(self.InWires) == 0 and len(self.OutWires) == 0:
#             return

#         if len(self.OutWires) != 0:
#             self.VOut = VIn - self.I*self.R
#         if len(self.InWires) != 0:
#             self.VIn = VOut + self.I*self.R

#     def GetVOut(self):
#         if len(self.OutWires) == 0:
#             return self.VOut
#         else:
#             return self.OutWires[0].VIn

#     def GetVIn(self):
#         if len(self.InWires) == 0:
#             return self.VIn
#         else:
#             return self.InWires[0].VOut

#     def AddInWire(self, In):
#         self.InWires.append(In)

#     def AddOutWire(self, Out):
#         self.OutWires.append(Out)

# a = Wire()
# a.VIn = 100

# b = Wire()
# c = Wire()
# d = Wire()

# a.AddOutWire(b)
# a.AddOutWire(c)

# b.AddInWire(a)
# b.AddOutWire(d)

# c.AddInWire(a)
# c.AddOutWire(d)

# d.AddInWire(b)
# d.AddInWire(c)

# for i in range(N):
#     a.TimeStep()
#     b.TimeStep()
#     c.TimeStep()
#     d.TimeStep()

#     Tab0 = np.append(Tab0, a.I)
#     Tab1 = np.append(Tab1, b.I)
#     Tab2 = np.append(Tab2, c.I)
#     Tab3 = np.append(Tab3, d.I)

# Time = np.arange(N)*dt
# plt.ticklabel_format(useOffset=False, style='plain')
# plt.plot(Time, Tab0, label="1")
# plt.plot(Time, Tab1, label="2")
# plt.plot(Time, Tab2, label="3")
# plt.plot(Time, Tab3, label="4")
# plt.legend(loc='upper right', shadow=True)
# plt.show()

# plt.cla()

# # exit(0)

# Q2 = 0.

# Tab0 = np.array([])
# Tab1 = np.array([])
# Tab2 = np.array([])
# Tab3 = np.array([])


