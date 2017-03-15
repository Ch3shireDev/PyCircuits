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
        self.I += (self.VIn() - self.VOut() - self.DeltaV())*dt
    
    def VOut(self):
        return self.NodeOut.GetV()
    
    def VIn(self):
        return self.NodeIn.GetV()
    
    def DeltaV(self):
        return self.I

    def GetVoltageDrop(self):
        return self.I

    def GetPotentialChange(self, Node):
        if Node is not self.NodeIn and Node is not self.NodeOut:
            print "wrong nodes!"
            exit(0)
        if Node is self.NodeIn:
            return self.NodeOut.GetV() - self.DeltaV()
        else:
            return self.NodeIn.GetV() + self.DeltaV()

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

    def SetChecked(self, Checked=True):
        self.IsChecked = Checked


class Node(object):
    
    def __init__(self):
        self.V = 0.
        self.Wires = []

    def GetV(self):
        return self.V
    
    def AddWire(self, line):
        self.Wires.append(line)
    
    def Recalculate(self):
        self.V = 0.
        for Wire in self.Wires:
            self.V += Wire.GetPotentialChange(self)
        self.V /= len(self.Wires)

    def TimeStep(self, Circuit, dt = 0.001):
        if len(self.Wires) == 0:
            return
        if len(self.Wires) == 1:
            Wire = self.Wires[0]
            Wire.TimeStep(dt)
            self.Recalculate()
            return
        LastWire = None
        for Wire in self.Wires:
            if Wire.IsChecked is False:
                LastWire = Wire
                break
        if LastWire is None:
            self.Recalculate()
        Current = 0.
        for Wire in self.Wires:
            if Wire is LastWire:
                continue
            Wire.TimeStep(dt)
            Current += Wire.GetCurrent(self)
        LastWire.SetCurrent(self, -Current)
        self.Recalculate()

class ExternalNode(Node):

    def __init__(self, V):
        Node.__init__(self)
        self.V = V

    def GetV(self):
        return self.V

    def Recalculate(self):
        pass

class GroundNode(Node):

    def __init__(self):
        Node.__init__(self)
        self.V = 0.

    def GetV(self):
        return 0.

    def Recalculate(self):
        pass

class Circuit:

    def __init__(self):
        self.Nodes = []
        self.Wires = []
        self.Time = 0.

    def AddNodeToList(self, Node):
        self.Nodes.append(Node)

    def AddNode(self):
        Node_ = Node()
        self.AddNodeToList(Node_)
        return Node_

    def AddSource(self, V):
        Node = ExternalNode(V)
        self.AddNodeToList(Node)
        return Node

    def AddAlternatingSource(self, Function):
        Node = self.AddNode()
        Node.V = Function(0)
        Node.SetExternal()
        self.AddNodeToList(Node)
        return Node

    def AddGround(self):
        Node = GroundNode()
        self.AddNodeToList(Node)
        return Node

    def AddWire(self, NodeIn, NodeOut, R=1.):
        Wire = Line(NodeIn, NodeOut, R)
        self.Wires.append(Wire)
        NodeIn.AddWire(Wire)
        NodeOut.AddWire(Wire)
        return Wire

    def TimeStep(self, dt = 0.001):
        for Wire in self.Wires:
            Wire.SetChecked(False)
        for Node in self.Nodes:
            Node.TimeStep(self, dt)
        self.Time += dt

