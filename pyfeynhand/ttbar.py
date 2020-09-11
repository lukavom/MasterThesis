#! /usr/bin/env python3

from PyFeynHand import FeynHandTeX
from PyFeynHand import FeynHandArgs, FeynHandColors

args = FeynHandArgs()

iCOLOR, oCOLOR, pCOLOR, vCOLOR, dCOLOR = FeynHandColors(args.BW)
if args.BW:
    oextra = '-BW'
else:
    oextra = ''

#------------------------------------------------------------------------------
# s-channel gg->tt
fd1 = FeynHandTeX(vcolor=vCOLOR, debug=args.debug)
if args.title: fd1.Text(r'$\Pg{}\Pg \to \Pqt\Paqt', 0, 2)

fd1.Vertex('g1', -3, +2,label=r'\Pg')
fd1.Vertex('g2', -3, -2, label=r'\Pg')
fd1.Vertex('t1', +3, +2, label=r'\Pqt')
fd1.Vertex('t2', +3, -2, label=r'\Paqt')

fd1.Vertex('gg', -1, 0, vtype='dot')
fd1.Vertex('gt', +1, 0, vtype='dot')

fd1.Propagator('gluon', 'g1', 'gg', iCOLOR)
fd1.Propagator('gluon', 'g2', 'gg', iCOLOR)
fd1.Propagator('gluon', 'gg', 'gt', pCOLOR, r'\Pg')
fd1.Propagator('fermion', 'gt', 't1', oCOLOR)
fd1.Propagator('fermion', 'gt', 't2', oCOLOR, reverse=True)

fd1.write('gg_ttbar_1' + oextra, compile=args.pdf)

#------------------------------------------------------------------------------
# t-channel gg->tt
fd2 = FeynHandTeX(vcolor=vCOLOR, debug=args.debug)
if args.title: fd2.Text(r'$\Pg{}\Pg \to \Pqt\Paqt', 0, 2)

pntIn = dict()
pntOut = dict()
fd2.Vertex('g1', -2, +1.5, label=r'\Pg')
fd2.Vertex('g2', -2, -1.5, label=r'\Pg')
fd2.Vertex('t1', +2, +1.5, label=r'\Pqt')
fd2.Vertex('t2', +2, -1.5, label=r'\Paqt')

vtx = dict()
fd2.Vertex('gt1', 0, +1.5, vtype='dot')
fd2.Vertex('gt2', 0, -1.5, vtype='dot')

fd2.Propagator('gluon', 'g1', 'gt1', iCOLOR)
fd2.Propagator('gluon', 'g2', 'gt2', iCOLOR)
fd2.Propagator('fermion', 'gt1', 't1', oCOLOR)
fd2.Propagator('fermion', 'gt2', 'gt1', pCOLOR, r'\Pqt')
fd2.Propagator('fermion', 'gt2', 't2', oCOLOR, reverse=True)

fd2.write('gg_ttbar_2' + oextra, compile=args.pdf)

#------------------------------------------------------------------------------
# u-channel gg->tt
fd3 = FeynHandTeX(vcolor=vCOLOR)
#l3 = Label(r'$\Pg{}\Pg \to \Pqt\Paqt', x=0, y=2)

fd3 = FeynHandTeX(vcolor=vCOLOR, debug=args.debug)
if args.title: fd3.Text(r'$\Pg{}\Pg \to \Pqt\Paqt', 0, 2)

fd3.Vertex('g1', -2, +1.5, label=r'\Pg')
fd3.Vertex('g2', -2, -1.5, label=r'\Pg')
fd3.Vertex('t1', +2, +1.5, label=r'\Pqt')
fd3.Vertex('t2', +2, -1.5, label=r'\Paqt')

fd3.Vertex('gt1', 0, +1.5, vtype='dot')
fd3.Vertex('gt2', 0, -1.5, vtype='dot')

fd3.Propagator('gluon', 'g1', 'gt1', iCOLOR)
fd3.Propagator('gluon', 'g2', 'gt2', iCOLOR)
fd3.Propagator('fermion', 'gt2', 't1', oCOLOR)
fd3.Propagator('fermion', 'gt1', 'gt2', pCOLOR, r'\Pqt')
fd3.Propagator('fermion', 'gt1', 't2', oCOLOR, reverse=True)

fd3.write('gg_ttbar_3' + oextra, compile=args.pdf)

#------------------------------------------------------------------------------
# qq->tt
fd4 = FeynHandTeX(vcolor=vCOLOR, debug=args.debug)
if args.title: fd4.Text(r'\Pep{}\Pem scattering', 0, 2)

fd4.Vertex('q1', -3, +2, label=r'\Pq')
fd4.Vertex('q2', -3, -2, label=r'\Paq')
fd4.Vertex('t1', +3, +2, label=r'\Pqt')
fd4.Vertex('t2', +3, -2, label=r'\Paqt')

fd4.Vertex('qg', -1, 0, vtype='dot')
fd4.Vertex('gt', +1, 0, vtype='dot')

fd4.Propagator('fermion', 'q1', 'qg', iCOLOR)
fd4.Propagator('fermion', 'q2', 'qg', iCOLOR, reverse=True)
fd4.Propagator('gluon', 'qg', 'gt', pCOLOR, r'\Pg')
fd4.Propagator('fermion', 'gt', 't1', oCOLOR)
fd4.Propagator('fermion', 'gt', 't2', oCOLOR, reverse=True)

fd4.write('qq_ttbar' + oextra, compile=args.pdf)
