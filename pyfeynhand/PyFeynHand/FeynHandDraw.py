from .FeynHandVertex import Vertex

class Draw:
    """Base class for adding draw stuff to Feynman diagrams."""

    def __init__(self, draw, first=False):
        """Constructor"""
        self.draw = draw
        self.first = first

    def __str__(self):
        s = []
        s.append('Draw {}, first: {}'.format(
            self.draw, self.first))

        return '\n'.join(s)

    def getDraw(self):
        "Return the drawing text"
        return self.draw

    def getFirst(self):
        "Return the boolean to draw first"
        return self.first

class Line(Vertex):
    """Base class for drawing a line in Feynman diagrams."""

    def __init__(self, xy1, xy2, props='', color=None, first=False):
        """Constructor"""
        self.points = list()
        self.points.append(Vertex(xy1[0], xy1[1]))
        self.points.append(Vertex(xy2[0], xy2[1]))
        if color:
            self.props = ','.join([color, props])
        else:
            self.props = props
        self.first = first


    def __str__(self):
        s = []
        s.append(r'Line ({}, {}) to ({}, {}), properties: {}, first: {}'.format(
            self.getXn(0), self.getYn(0), self.getXn(1), self.getYn(1),
            self.props, self.first))

        return '\n'.join(s)

    def setProps(self, props):
        "Set the line properties"
        self.props = props
        return self

    def getXn(self, n):
        "Return the x-coordinate of a point"
        return self.points[n].getX()

    def getYn(self, n):
        "Return the y-coordinate of a point"
        return self.points[n].getY()

    def getXYn(self, n):
        "Return the x and y coordinates of a point as a 2-tuple."
        return self.points[n].getX(), self.points[n].getY()

    def getProps(self):
        "Return the properties"
        return self.props

    def getFirst(self):
        "Return the boolean to draw first"
        return self.first

class Arrow(Line):
    """Draw an arrow"""
    def __init__(self, xy1, xy2, arrow='->', props='', color=None, first=False):
        """Constructor"""
        self.xpos = list()
        self.ypos = list()
        self.setXY(xy1)
        self.setXY(xy2)
        if color:
            self.props = ','.join(map(str, [arrow, color, props]))
        else:
            self.props = ','.join(map(str, [arrow, props]))
        self.first = first
        