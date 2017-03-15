'''File for wire types. To be imported only by internal files.'''

class Line(object):
    '''Basic class for all wire components.'''
    def __init__(self, NodeIn, NodeOut):
        self.NodeIn = NodeIn
        self.NodeOut = NodeOut
        self.I = 0.
        self.IsChecked = False

    def TimeStep(self, dt=0.001):
        '''Generic TimeStep function, does not require change'''
        if self.IsChecked is True:
            return
        self.SetChecked()
        self.I += (self.VIn() - self.VOut() - self.DeltaV())*dt

    def VOut(self):
        '''Auxiliary function to obtain VOut value'''
        return self.NodeOut.GetV()

    def VIn(self):
        '''Another auxiliary function'''
        return self.NodeIn.GetV()

    def DeltaV(self):
        '''Function describing voltage drop on component.
        Needs to be redefined in any child class.'''
        return 0.

    def GetPotentialChange(self, Node):
        '''Function for potential change from one node to another.
        Does not require redefining in child classes.'''
        if Node is not self.NodeIn and Node is not self.NodeOut:
            print("wrong nodes!")
            exit(0)
        if Node is self.NodeIn:
            return self.NodeOut.GetV() + self.DeltaV()
        else:
            return self.NodeIn.GetV() - self.DeltaV()

    def GetCurrent(self, Node=None):
        '''Function for obtaining the current coming to given Node.
        If no Node is given, returns just holded value.'''
        if Node is None:
            return self.I
        if self.NodeIn is Node:
            return self.I
        else:
            return -self.I

    def SetCurrent(self, Node, Current):
        '''Sets current from given Node'''
        self.SetChecked()
        if self.NodeIn is Node:
            self.I = Current
        else:
            self.I = -Current

    def SetChecked(self, Checked=True):
        '''Sets check for every line to not go through all lines twice.'''
        self.IsChecked = Checked

class Resistor(Line):
    '''Resistor class, requires to specify the resistance value.'''
    def __init__(self, NodeIn, NodeOut, R=100):
        Line.__init__(self, NodeIn, NodeOut)
        self.R = R

    def DeltaV(self):
        return self.R*self.I

class Diode(Line):
    '''Diode class, following the ideal diode law:
      I = I_S(exp(V_D/V_T)-1).
    '''

    def DeltaV(self):
        pass
