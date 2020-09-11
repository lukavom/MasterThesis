#! /usr/bin/env python3

# Multi-coloured Feynman graph for top-quark decay
# This has way more colors than are sensible or useful,
# but should illustrate how to set them

from PyFeynHand import FeynHandTeX
from PyFeynHand import FeynHandArgs, FeynHandColors

args = FeynHandArgs()

iCOLOR, oCOLOR, pCOLOR, vCOLOR, dCOLOR = FeynHandColors(args.BW)
if args.BW:
    oextra = '-BW'
else:
    oextra = ''

#------------------------------------------------------------------------------
# Top semileptonic decay
# Set generic colors for vertices (dots and text) and propagators
# Set lcolor='Black' to get black labels
# Set a thicker line width for illustration
fd1 = FeynHandTeX(pcolor=pCOLOR, vcolor=vCOLOR, linewidth='2.0pt', debug=args.debug)
fd1.Text(r'\textcolor{Blue}{\Large Top-quark decay}', 0, 4.0, first=True)
fd1.Text('Semileptonic channel', 0, 3.5, color='Green')
fd1.Line((-1.7, 3.8), (1.7, 3.8))
fd1.Line((-2.0, 4.3), (-2.0, 3.3), 'Red, line width = 2pt')
fd1.Line((-2.1, 4.3), (-2.1, 3.3), color='Brown')
fd1.Arrow((-3, 4), (-2.2,4), '{Circle[Red, width=5pt, length=5pt]}->', color='Magenta')
fd1.Draw(r'\filldraw[fill=Yellow, draw=Red] (-2.1,2.4) circle [radius=0.5cm]')

# For external lines label the vertices - default type is particle
fd1.Vertex('t', -3, 1, label=r'\Ptop')
fd1.Vertex('b', 3, 0, label=r'\Pbottom')
# Set colour of lepton text to vertex colour
fd1.Vertex('l', 3, 2, label=r'\Plepton', lcolor=vCOLOR)
fd1.Vertex('nu', 3, 4, label=r'\APnulepton')

# Set colour of dot

fd1.Vertex('tb', -0.5, 1, vtype='dot', vcolor=vCOLOR, label='\(V_{\Pqt{}\Pqb}\)', \
    lcolor=vCOLOR, lpos='below')
fd1.Vertex('Wlnu', 1, 3, vtype='dot')

# Propagators (including external lines)
fd1.Propagator('fermion', 't', 'tb', iCOLOR)
# Use default propagator colour
fd1.Propagator('fermion', 'tb', 'b')#, oCOLOR)
# Add a label to the propagator
fd1.Propagator('boson', 'tb', 'Wlnu', pCOLOR, r'\PW')
fd1.Propagator('fermion', 'Wlnu', 'l', dCOLOR)
fd1.Propagator('fermion', 'Wlnu', 'nu', dCOLOR, reverse=True)
print(fd1)

fd1.write('tdecay' + oextra, compile=args.pdf)
