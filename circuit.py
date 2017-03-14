class Line:
    def __init__(self, NodeIn, NodeOut, R = 1.):
        self.NodeIn = NodeIn
        self.NodeOut = NodeOut
        self.R = R
        self.I = 0.
    def TimeStep(self, dt = 0.001):
        self.I += (self.DeltaV() - self.R*self.I)*dt
    def VOut(self):
        return self.NodeOut.V
    def VIn(self):
        return self.NodeIn.V
    def DeltaV(self):
        return self.VIn() - self.VOut()

    def GetPotentialChange(self, Node):
        if Node is not self.NodeIn and Node is not self.NodeOut:
            print "wrong nodes!"
            exit(0)
        if Node is self.NodeIn:
            return self.NodeOut.V - self.I*self.R
        else:
            return self.NodeIn.V + self.I*self.R

    def GetCurrent(self):
        return self.I


class Node:    
    def __init__(self, V=0.):
        self.V = V
        self.Lines = []
    def AddWire(self, line):
        self.Lines.append(line)
    def Recalculate(self):
        if len(self.Lines) < 2:
            return
        self.V = 0.
        for Wire in self.Lines:
            self.V += Wire.GetPotentialChange(self)

        self.V /= len(self.Lines)

    def TimeStep(self, dt = 0.001):
        if len(self.Lines) == 0:
            return
        if len(self.Lines) == 1:
            Wire = self.Lines[0]
            if Wire.NodeIn is self:
                Wire.TimeStep(dt)
                return

        InCurrent = 0.
        OutWires = []

        for Wire in self.Lines:
            if Wire.NodeOut is self:
                InCurrent += Wire.I
            else:
                OutWires.append(Wire)

        if len(OutWires) == 0:
            return

        if len(OutWires) == len(self.Lines):
            exit(0)

        if len(OutWires) == 1:
            OutWires[0].I = InCurrent
            self.Recalculate()
            return

        OutCurrent = 0.
        for Wire in OutWires[:-1]:
            Wire.TimeStep(dt)
            OutCurrent += Wire.I

        OutWires[-1].I = InCurrent - OutCurrent
        self.Recalculate()



class Circuit:
    def __init__(self):
        self.Nodes = []
        self.Lines = []

    def AddNode(self, V=0.):
        node = Node(V)
        self.Nodes.append(node)
        return node

    def AddWire(self, NodeIn, NodeOut, R=1.):
        line = Line(NodeIn, NodeOut, R)
        self.Lines.append(line)
        NodeIn.AddWire(line)
        NodeOut.AddWire(line)
        return line

    def TimeStep(self, dt = 0.001):
        for node in self.Nodes:
            node.TimeStep(dt)