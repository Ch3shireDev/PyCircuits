'''Main file for Circuit class, built on undirected graph structure. Import only Circuit.'''
from wires import *
from nodes import *

class Circuit:
    '''Main class for the circuit system, needed alone to import.'''
    def __init__(self, dt=0.001):
        self.Nodes = []
        self.Wires = []
        self.Time = 0.
        self.dt = dt

    def AddNodeToList(self, Node):
        '''Internal function.'''
        self.Nodes.append(Node)

    def AddNode(self):
        '''Adds single node without set potential.'''
        Node = CustomNode()
        self.AddNodeToList(Node)
        return Node

    def AddSource(self, V):
        '''Adds constant potential node.'''
        Node = SourceNode(V)
        self.AddNodeToList(Node)
        return Node

    def AddAlternatingSource(self, Function):
        '''Adds varying potential node, changes described by given function.'''
        Node = AlternatingNode(Function)
        self.AddNodeToList(Node)
        return Node

    def AddGround(self):
        '''Adds zero potential node, known as Ground.'''
        Node = GroundNode()
        self.AddNodeToList(Node)
        return Node

    def AddWire(self, NodeIn, NodeOut):
        '''Adds simple wire with zero resistance.'''
        Wire = Line(NodeIn, NodeOut)
        self.Wires.append(Wire)
        NodeIn.AddWire(Wire)
        NodeOut.AddWire(Wire)
        return Wire

    def AddResistor(self, NodeIn, NodeOut, R=100.):
        '''Adds wire with given resistance.'''
        Wire = Resistor(NodeIn, NodeOut, R)
        self.Wires.append(Wire)
        NodeIn.AddWire(Wire)
        NodeOut.AddWire(Wire)
        return Wire

    def AddDiode(self, NodeIn, NodeOut):
        '''Adds diode with given parameters.'''
        Wire = Diode(NodeIn, NodeOut)
        self.Wires.append(Wire)
        NodeIn.AddWire(Wire)
        NodeOut.AddWire(Wire)
        return Wire

    def TimeStep(self, n=100):
        '''Main TimeStep function to be called by the user.'''
        for i in range(n):
            x = 0
            for Node in self.Nodes:
                x += Node.TimeStep(self, 0)
            if x < 1e-6:
                break
        for Wire in self.Wires:
            Wire.SetChecked(False)
        for Node in self.Nodes:
            Node.TimeStep(self, self.dt)
        self.Time += self.dt

    def GetTime(self):
        '''Returns total time of the simulation.'''
        return self.Time
