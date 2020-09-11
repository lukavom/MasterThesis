class Propagator:
    """Base class for all propagator objects in Feynman diagrams."""

    def __init__(self, ptype, vtx1, vtx2,
        pcolor=None, label='', lcolor=None, reverse=False, labelRight=False):
        """Constructor."""
        self.ptype = ptype
        self.vtx = [vtx1, vtx2]
        self.label = label
        self.pcolor = pcolor
        self.lcolor = lcolor
        self.reverse = reverse
        self.labelRight = labelRight

    def __str__(self):
        s = []
        s.append('Propagator {} {} {} {} {}, reverse={}, labelRight={}'.format(
            self.ptype, self.vtx, self.label,
            self.pcolor, self.lcolor, self.reverse, self.labelRight))

        return '\n'.join(s)

    def getType(self):
        "Return the type of propagator"
        return self.ptype

    def getVertices(self):
        "Return the vertices"
        return self.vtx

    def getVertex1(self):
        "Return the first vertex"
        if self.reverse:
            return self.vtx[1]
        else:
            return self.vtx[0]

    def getVertex2(self):
        "Return the second vertex"
        if self.reverse:
            return self.vtx[0]
        else:
            return self.vtx[1]

    def getPropColor(self):
        "Return the color of propagator"
        return self.pcolor

    def getLabelColor(self):
        "Return the color of propagator label"
        return self.lcolor

    def getLabel(self):
        "Return the label of propagator"
        return self.label
    
    def getLabelRight(self):
        "Return if the label of propagator should be on the right"
        return self.labelRight
    