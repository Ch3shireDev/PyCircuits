#File for class structure of Circuit (whole system), Nodes (intersections in circuit) and Lines (or wires). For now Lines have only resistance
#parameter, so it's just complicated simulation of simple mid-school resistors system.

class Line:

    def __init__(self, NodeIn, NodeOut, R = 1.):
        self.NodeIn = NodeIn
        self.NodeOut = NodeOut
        self.R = R
        self.I = 0.
        self.IsChecked = False

    def TimeStep(self, dt = 0.001):
        if self.IsChecked is True:
            return
        self.SetChecked()
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

    def GetCurrent(self, Node):
        if self.NodeIn is Node:
            return self.I
        else: 
            return -self.I

    def SetCurrent(self, Node, Current):
        self.SetChecked()
        if self.NodeIn is Node:
            self.I = Current
        else:
            self.I = -Current

    def SetChecked(self, flag=True):
        self.IsChecked = flag


class Node:
    
    def __init__(self):
        self.V = 0.
        self.Lines = []
        self.IsConstant = False

    def SetConstant(self, flag = True):
        self.IsConstant = flag
    
    def AddWire(self, line):
        self.Lines.append(line)
    
    def Recalculate(self):
        if self.IsConstant:
            return
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

    def AddNode(self):
        Node_ = Node()
        self.Nodes.append(Node_)
        return Node_

    def AddSource(self, V):
        Node = self.AddNode()
        Node.V = V
        Node.SetConstant()
        return Node

    def AddGround(self):
        Node = self.AddNode()
        Node.SetConstant()
        return Node

    def AddWire(self, NodeIn, NodeOut, R=1.):
        Wire = Line(NodeIn, NodeOut, R)
        self.Lines.append(Wire)
        NodeIn.AddWire(Wire)
        NodeOut.AddWire(Wire)
        return Wire

    def TimeStep(self, dt = 0.001):
        for Wire in self.Lines:
            Wire.SetChecked(False)
        for Node in self.Nodes:
            Node.TimeStep(dt)