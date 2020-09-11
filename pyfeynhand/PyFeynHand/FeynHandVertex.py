class Vertex:
    """Base class for all vertices (points) in Feynman diagrams
    If you add an argument here it also has to be added to FeynHandTex.py"""

    def __init__(self, x, y, vtype='particle', label='', vcolor=None, lcolor=None, lpos=None):
        """Constructor"""
        self.setXY(x, y)
        self.vtype = vtype
        self.label = label
        self.vcolor = vcolor
        self.lcolor = lcolor
        self.lpos = lpos

    def __str__(self):
        s = []
        s.append('Vertex {} ({}, {}), label: {}, colours: {} {}, position: {}'.format(
            self.vtype, self.getX(), self.getY(), self.label,
            self.vcolor, self.lcolor, self.lpos))

        return '\n'.join(s)

    def setXY(self, xpos, ypos):
        "Set the x and y coordinates"
        self.setX(float(xpos))
        self.setY(float(ypos))
        return self

    def setX(self, x):
        "Set the x-coordinate"
        self.xpos = x
        return self

    def setY(self, y):
        "Set the y-coordinate"
        self.ypos = y
        return self

    def setType(self, vtype):
        "Set the type of vertex"
        self.vtype = vtype
        return self

    def setLabel(self, label):
        "Set the label"
        self.label = label
        return self

    def setVertexColor(self, vcolor):
        "Set the vertex color"
        self.vcolor = vcolor
        return self

    def setLabelColor(self, lcolor):
        "Set the label color"
        self.lcolor = lcolor
        return self

    def setLabelPos(self, lpos):
        "Set the label position"
        self.lpos = lpos
        return self

    def getX(self):
        "Return the x-coordinate"
        return self.xpos

    def getY(self):
        "Return the y-coordinate"
        return self.ypos

    def getXY(self):
        "Return the x and y coordinates as a 2-tuple."
        return self.getX(), self.getY()

    def getType(self):
        "Return the type of vertex"
        return self.vtype

    def getLabel(self):
        "Return the label"
        return self.label

    def getVertexColor(self):
        "Return the vertex color"
        return self.vcolor

    def getLabelColor(self):
        "Return the label color"
        return self.lcolor

    def getLabelPos(self):
        "Return the label position"
        return self.lpos
