#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
N = 10000



V0 = 100.

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
V4 = 0.
V5 = 0.
V6 = 0.
V7 = 0.

Tab0 = np.array([])
Tab1 = np.array([])
Tab2 = np.array([])

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
    Tab2 = np.append(Tab2, I3)

#             |---[  ]---|
# V0 o--[  ]--o          o---[  ]---o Ground
#             |---[  ]---|
#
# All resistors ( [  ] ) have resistance 1 Ohm, V0 is 100 V

Time = np.arange(N)*dt
plt.ticklabel_format(useOffset=False, style='plain')
plt.plot(Time, Tab0, label="1")
plt.plot(Time, Tab1, label="2")
plt.plot(Time, Tab2, label="3")
plt.legend(loc='upper right', shadow=True)
plt.show()
exit(0)


class Node:
    
    def __init__(self, V=0.):
        self.V = V
        self.Lines = []
    def AddLine(self, line):
        self.Lines.append(line)

class Line:

    def __init__(self, InNode, OutNode, R = 1.):
        self.InNode = InNode
        self.OutNode = OutNode
        InNode.AddLine(self)
        OutNode.AddLine(self)
        self.R = R
        self.I = 0.

    def GetDeltaV(self):
        return self.OutNode.V - self.InNode.V


class CircuitSystem:

    def __init__(self):
        self.Nodes = []
        self.Lines = []

    def AddNode(self, V = 0.):
        node = Node(V)
        self.Nodes.append(node)
        return node

    def AddLine(self, InNode, OutNode, R = 1.):
        line = Line(InNode, OutNode, R)
        self.Lines.append(line)
        return line

    def TimeStep(self, dt=0.001):
        for node in self.Nodes:
            for line in node.Lines:
                if line.InNode is node:
                    line.I += (line.GetDeltaV() - line.R*line.I)*dt
                    if len(line.InNode.Lines) > 1:
                        pass
                        # line.InNode.V = 


System = CircuitSystem()

a = System.AddNode(100.)
b = System.AddNode()
c = System.AddNode()
d = System.AddNode(0.)

System.AddLine(a, b)
System.AddLine(b, c)
System.AddLine(b, c)
System.AddLine(c, d)

System.TimeStep()