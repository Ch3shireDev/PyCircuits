'''File for node types. To be imported only by internal files.'''

class Node(object):
    '''Generic node class. Suitable for every cross between wires without given voltage.'''
    def __init__(self):
        self.V = 0.
        self.Wires = []

    def GetV(self):
        '''Returns potential value.'''
        return self.V

    def AddWire(self, Wire):
        '''Adds wire to line list.'''
        self.Wires.append(Wire)

    def Recalculate(self):
        '''Recalculates potential value. Requires to be redefined in child classes.'''
        self.V = 0.
        for Wire in self.Wires:
            self.V += Wire.GetPotentialChange(self)
        self.V /= len(self.Wires)

    def TimeStep(self, Circuit, dt):
        '''Generic TimeStep function, does not requires redefinition in child classes.'''
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
            return
        Current = 0.
        for Wire in self.Wires:
            if Wire is LastWire:
                continue
            Wire.TimeStep(dt)
            Current += Wire.GetCurrent(self)
        LastWire.SetCurrent(self, -Current)
        self.Recalculate()

class AlternatingNode(Node):
    '''Voltage source with changing value, given by specified function.'''
    def __init__(self, Vt):
        Node.__init__(self)
        self.Vt = Vt
        self.V = Vt(0.)

    def Recalculate(self):
        pass

    def TimeStep(self, Circuit, dt):
        Node.TimeStep(self, Circuit, dt)
        self.V = self.Vt(Circuit.GetTime())

class SourceNode(Node):
    '''Class for constant source.'''
    def __init__(self, V):
        Node.__init__(self)
        self.V = V

    def GetV(self):
        return self.V

    def Recalculate(self):
        pass

class GroundNode(Node):
    '''Class for zero potential node.'''
    def __init__(self):
        Node.__init__(self)
        self.V = 0.

    def GetV(self):
        return 0.

    def Recalculate(self):
        pass
