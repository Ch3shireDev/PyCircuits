'''File for node types. To be imported only by internal files.'''

class GroundNode(object):
    '''Generic class for zero potential node, ground of the system.'''
    def __init__(self):
        self.Wires = []

    def GetV(self):
        return 0.

    def Recalculate(self):
        return 0

    def AddWire(self, Wire):
        '''Adds wire to line list.'''
        self.Wires.append(Wire)

    def TimeStep(self, Circuit, dt):
        '''Generic TimeStep function, does not requires redefinition in child classes.'''
        if len(self.Wires) == 0:
            return 0
        if len(self.Wires) == 1:
            Wire = self.Wires[0]
            Wire.TimeStep(dt)
        else:
            LastWire = None
            for Wire in self.Wires:
                if Wire.IsChecked is False:
                    LastWire = Wire
                    break
            if LastWire is not None:
                Current = 0.
                for Wire in self.Wires:
                    if Wire is LastWire:
                        continue
                    Wire.TimeStep(dt)
                    Current += Wire.GetCurrent(self)
                LastWire.SetCurrent(self, -Current)
        return self.Recalculate()


class SourceNode(GroundNode):
    '''Class for constant source.'''
    def __init__(self, V=0):
        self.Wires = []
        self.V = V

    def GetV(self):
        return self.V

    
class AlternatingNode(SourceNode):
    '''Voltage source with changing value, given by specified function.'''
    def __init__(self, Vt):
        self.Wires = []
        self.Vt = Vt
        self.V = Vt(0.)

    def TimeStep(self, Circuit, dt):
        SourceNode.TimeStep(self, Circuit, dt)
        self.V = self.Vt(Circuit.GetTime())


class CustomNode(SourceNode):
    '''Custom node class. Suitable for every cross between wires without given voltage.'''
    def __init__(self):
        SourceNode.__init__(self)

    def GetV(self):
        '''Returns potential value.'''
        return self.V

    def Recalculate(self):
        '''Recalculates potential value. Requires to be redefined in child classes.'''
        V0 = self.V
        self.V = 0.
        for Wire in self.Wires:
            self.V += Wire.GetPotentialChange(self)
        self.V /= len(self.Wires)
        return abs(V0-self.V)
