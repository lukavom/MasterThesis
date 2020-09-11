import shlex
import subprocess
import sys

from .FeynHandVertex import Vertex
from .FeynHandPropagator import Propagator
from .FeynHandText import Text
from .FeynHandDraw import Line, Arrow, Draw


class FeynHandTeX:
    """Base class for creating FeynHand LaTeX file"""

    def __init__(self, font='newtx', linewidth='1.0pt', lcolor=None, pcolor=None, vcolor=None, debug=0):
        """Initialize FeynHand TeX object"""

        self.font = font
        self.linewidth = linewidth
        self.lcolor = lcolor
        self.pcolor = pcolor
        self.vcolor = vcolor
        self.debug = debug
        self.vertices = dict()
        self.propagators = list()
        self.texts = list()
        self.lines = list()
        self.draws = list()

    def __str__(self):
        s = []
        s.append('FeynHandTeX object')
        s.append('Font: {}'.format(self.font))
        s.append('Line width: {}'.format(self.linewidth))
        s.append('Label color: {}'.format(str(self.lcolor)))
        s.append('Propagator color: {}'.format(str(self.pcolor)))
        s.append('Vertex color: {}'.format(str(self.vcolor)))
        for key, vtx in self.vertices.items():
            s.append(r'Vertex {}, type: {}, position: {} {}, label: {}, colours: {} {}, position: {}'.format(
                key, vtx.getType(), vtx.getX(), vtx.getY(),
                vtx.getLabel(), vtx.getVertexColor(), vtx.getLabelColor(), vtx.getLabelPos()
            ))
        for prop in self.propagators:
            s.append(r'Propagator {} from {} to {}, label: {}, colours: {} {}'.format(
                prop.getType(), prop.getVertex1(), prop.getVertex2(),
                prop.getLabel(), prop.getPropColor(), prop.getLabelColor()
            ))
        for text in self.texts:
            s.append(r'Text {}, position: ({}, {}), colour: {}'.format(
                text.getText(), text.getX(), text.getY(), text.getTextColor()
            ))
        for line in self.lines:
            s.append(r'Line from ({}, {}) to ({}, {}), properties: {}'.format(
                line.getXn(0), line.getYn(0), line.getXn(1), line.getYn(1), line.getProps()
            ))

        return '\n'.join(s)

    def Vertex(self, name, x, y, vtype='particle', 
        label='', vcolor=None, lcolor=None, lpos=None):
        "Add a vertex"
        self.vertices[name] = Vertex(x, y, vtype=vtype,
            label=label, lcolor=lcolor, vcolor=vcolor, lpos=lpos)
        return

    def Propagator(self, ptype, vtx1, vtx2, pcolor=None,
        label='', lcolor=None, reverse=False, labelRight=False):
        "Add a propagator"
        self.propagators.append(Propagator(ptype, vtx1, vtx2, pcolor=pcolor,
            label=label, lcolor=lcolor, reverse=reverse, labelRight=labelRight))
        return

    def Text(self, text, x, y, color=None, first=False):
        "Add some text to the graph"
        self.texts.append(Text(text, x, y, color=color, first=first))
        return

    def Line(self, vtx1, vtx2, props='', color=None, first=False):
        "Add a line to the graph"
        self.lines.append(Line(vtx1, vtx2, props=props, color=color, first=first))
        return

    def Arrow(self, vtx1, vtx2, arrow='->', props='', color=None, first=False):
        "Add an arrow to the graph"
        _props = ','.join(map(str, [arrow, props]))
        self.lines.append(Line(vtx1, vtx2, props=_props, color=color, first=first))
        return

    def Draw(self, text, first=False):
        "Add a draw command to the graph"
        self.draws.append(Draw(text, first=first))
        return

    def open(self, file):
        "Open output TeX file"
        fout = open(file + '.tex', 'w')
        return fout

    def preamble(self):
        "Return a list of string with the preamble"
        self.preamble = list()
        self.preamble.append(r'\documentclass{standalone}')
        self.preamble.append(r'\usepackage[utf8]{inputenc}')
        if self.font == 'newtx':
            self.preamble.append(r'\usepackage{newtxtext}')
            self.preamble.append(r'\usepackage{newtxmath}')
        else:
            self.preamble.append(r'\usepackage{' + self.font + r'}')
        self.preamble.append(r'\usepackage[italic]{hepnicenames}')
        # Tweak to get decent overline width for slim letters
        self.preamble.append(r'\makeatletter\def\@shiftlen@anti@gen@bar{0mu}\makeatother')
        self.preamble.append(r'\usepackage[svgnames]{xcolor}')
        self.preamble.append(r'\usepackage{tikz-feynhand}')
        self.preamble.append('\n')
        self.preamble.append(r'\begin{document}')
        self.preamble.append(r'\begin{tikzpicture}')
        self.preamble.append(r'  \setlength{{\feynhandlinesize}}{{{}}}'.format(self.linewidth))
        if self.pcolor:
            self.preamble.append(r'  \tikzfeynhandset{every fermion={/tikz/color=' + self.pcolor + r'},}')
            self.preamble.append(r'  \tikzfeynhandset{every boson={/tikz/color=' + self.pcolor + r'},}')
        if self.vcolor:
            self.preamble.append(r'  \tikzfeynhandset{every dot={/tikz/color=' + self.vcolor + r'},}')
        self.preamble.append(r'  \begin{feynhand}')
        
        return self.preamble

    def write(self, file, compile=False):
        "Write Feynman graph to file"
        if self.debug > 0: print('Opening', file)
        fout = self.open(file)

        # Preamble
        for line in self.preamble():
            fout.write(line + '\n')

        # Text that should come first
        self.write_text(fout, True)
        # Lines that should come first
        self.write_lines(fout, True)
        # Extra stuff before graph
        self.write_draw(fout, True)

        # Feynman graph
        # Vertices
        self.write_vertices(fout)
        # Propagators
        self.write_propagators(fout)

        # Text that should come after graph
        self.write_text(fout, False)
        # Lines that should come after graph
        self.write_lines(fout, False)
        # Extra stuff after graph
        self.write_draw(fout, False)

        # Terminate Feynman graph
        fout.write(r'  \end{feynhand}' + '\n')
        fout.write(r'\end{tikzpicture}' + '\n')
        fout.write(r'\end{document}' + '\n')

        fout.close()

        # Run pdlalatex
        if compile:
            cmdstr = 'pdflatex ' + file
            cmd =  shlex.split(cmdstr)
            print('pdflatex command:', cmd)
            process = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            for line in iter(process.stdout.readline, b''):
                sys.stdout.write(line.decode(sys.stdout.encoding, errors='ignore'))

        return

    def write_vertices(self, fout):
        "Write vertices to TeX file"
        for key, vtx in self.vertices.items():
            if self.debug > 0: print('Vertex:', key, vtx)
            fout.write(r'    \vertex [{}'.format(vtx.getType()))
            _vcolor = None
            # Use label colour for particle vertices
            if vtx.getType() == 'particle':
                if vtx.getLabelColor():
                    _vcolor = vtx.getLabelColor()
                elif self.lcolor:
                    _vcolor = self.lcolor
                else:
                    _vcolor = self.getPropColor(key)
            # Use coloured blob 
            elif 'blob' in vtx.getType():
                fout.write(r', draw={}, pattern color={}'.format(self.vcolor, self.vcolor))
            # Use vertex colour for all other vertices
            else:
                if vtx.getVertexColor():
                    _vcolor = vtx.getVertexColor()
                elif self.vcolor:
                    _vcolor = self.vcolor
            if _vcolor:
                fout.write(r', {}'.format(_vcolor))
            # For dots and blobs add label here
            if vtx.getType() != 'particle':
                # print('Add label to dot etc.')
                if vtx.getLabel():
                    fout.write(r', label=')
                    if vtx.getLabelPos():
                        fout.write(r'{}:'.format(vtx.getLabelPos()))
                    if vtx.getLabelColor():
                        fout.write(r'\color{{{}}}'.format(vtx.getLabelColor()))
                    elif self.lcolor:
                        fout.write(r'\color{{{}}}'.format(self.lcolor))
                    fout.write(r'{}'.format(vtx.getLabel()))
            fout.write(r'] ({}) at ({}, {}) {{'.format(
                key, vtx.getX(), vtx.getY()))
            if vtx.getType() == 'particle':
                # print('Add label to particle')
                if vtx.getLabelColor():
                    fout.write(r'\color{{{}}}'.format(vtx.getLabelColor()))
                elif self.lcolor:
                    fout.write(r'\color{{{}}}'.format(self.lcolor))
                fout.write(r'{}'.format(vtx.getLabel()))
            fout.write(r'}')
            fout.write(';\n')

        return

    def write_propagators(self, fout):
        "Write propagators to TeX file"
        for prop in self.propagators:
            if self.debug > 0: print('Propagator:', prop)
            pline = r'    \propagator [{}'.format(prop.getType())
            if prop.getPropColor():
                pline += ', {}'.format(prop.getPropColor())
            elif self.pcolor:
                pline += ', {}'.format(self.pcolor)
            pline += r'] ({}) to'.format(prop.getVertex1())
            if prop.getLabelRight():
                tlabel = 'edge label\''
            else:
                tlabel = 'edge label'
            if prop.getLabel():
                if prop.getLabelColor():
                    pline += r' [{}={}, color={}]'.format(
                        tlabel, '{'+prop.getLabel()+'}', prop.getLabelColor())
                elif self.lcolor:
                    pline += r' [{}={}, color={}]'.format(
                        tlabel, '{'+prop.getLabel()+'}', self.lcolor)
                else:
                    pline += r' [{}={}, color={}]'.format(
                        tlabel, '{'+prop.getLabel()+'}', prop.getPropColor())
            pline += r' ({})'.format(prop.getVertex2())
            fout.write(pline + ';\n')

    def write_text(self, fout, first):
        " Write text strings to TeX file"
        for text in self.texts:
            if first and not text.getFirst(): continue
            if not first and text.getFirst(): continue
            if self.debug > 0: print('Text:', text)
            if text.getTextColor():
                pline = r'    \node at ({}, {}) {}'.format(
                    text.getX(), text.getY(), '{\\textcolor{'+text.getTextColor()+'}{'+text.getText()+'}}')
            else:
                pline = r'    \node at ({}, {}) {}'.format(
                    text.getX(), text.getY(), '{'+text.getText()+'}')
            fout.write(pline + ';\n')

    def write_lines(self, fout, first):
        "Write lines to TeX file"
        nl = 0
        for line in self.lines:
            if first and not line.getFirst(): continue
            if not first and line.getFirst(): continue
            if self.debug > 0: print('Line:', line)
            pline = r'    \vertex (FHTb{}) at ({}, {});'.format(nl, line.getXn(0), line.getYn(0))
            pline += r' \vertex (FHTe{}) at ({}, {});'.format(nl, line.getXn(1), line.getYn(1))
            fout.write(pline + '\n')
            if line.getProps():
                pline = r'    \draw [{}] (FHTb{}) to (FHTe{})'.format(line.getProps(), nl, nl)
            else:
                pline = r'    \draw (FHTb{}) to (FHTe{})'.format(nl, nl)
            fout.write(pline + ';\n')
            nl += 1

    def write_draw(self, fout, first):
        "Write draw commands (or whatever) to TeX file"
        for draw in self.draws:
            if first and not draw.getFirst(): continue
            if not first and draw.getFirst(): continue
            if self.debug > 0: print('Draw:', draw)
            pline = r'    {}'.format(draw.getDraw())
            fout.write(pline + ';\n')

    def getPropColor(self, vkey):
        "Return the propagator color associated with vertex vkey"

        # See if there is a propagator with this vertex and its colour is set
        # If no color set return default colour
        for prop in self.propagators:
            if vkey == prop.getVertex1() or vkey == prop.getVertex2():
                if prop.getPropColor():
                    return prop.getPropColor()
                else:
                    return self.pcolor
        
        return None
        
