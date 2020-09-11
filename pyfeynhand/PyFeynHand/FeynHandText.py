from .FeynHandVertex import Vertex

class Text(Vertex):
    """Base class for adding text to Feynman diagrams"""

    def __init__(self, text, x, y, color=None, first=False):
        """Constructor"""
        self.text = text
        self.setXY(x, y)
        self.color = color
        self.first = first

    def __str__(self):
        s = []
        s.append(r'Text {}, position: ({} {}), colour: {}, first: {}'.format(
            self.text, self.getX(), self.getY(),
            self.color, self.first))

        return '\n'.join(s)

    def setText(self, text):
        "Set the text"
        self.text = text
        return self

    def setTextColor(self, tcolor):
        "Set the text color"
        self.tcolor = tcolor
        return self

    def getText(self):
        "Return the text"
        return self.text

    def getTextColor(self):
        "Return the text color"
        return self.color

    def getFirst(self):
        "Return the boolean to draw first"
        return self.first
