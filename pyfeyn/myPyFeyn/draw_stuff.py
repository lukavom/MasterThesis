from pyfeyn.lines import Fermion
from pyfeyn.lines import Photon
from pyfeyn.lines import Gluon
from pyfeyn.lines import Higgs
from pyfeyn.points import Point, Vertex
from pyfeyn.deco import Label

nfermion = -1
nboson = -1
ngluon = -1
nhiggs = -1
fermions = []
bosons = []
gluons = []
higgs = []


def draw_fermion(pnt1, pnt2, COLOR, label,
    displacement=-0.25, position=0.5, thickness=0, bend=0):
    global nfermion, fermions

    nfermion += 1
    fermions.append(Fermion(pnt1, pnt2).addArrow())
    if label != '':
        if displacement == 0.0 and position == 0.0:
            #print('Not moving fermion label')
            fermions[nfermion].addLabel(label)
        else:
            #print('Moving fermion label by', displacement)
            fermions[nfermion].addLabel(
                label, displace=displacement, pos=position)
    fermions[nfermion].setStyles(COLOR)
    if thickness != 0:
        #print('Changing thickness to', thickness)
        fermions[nfermion].addStyle(thickness)
    if bend != 0:
        #print('Changing bend to', bend)
        fermions[nfermion].bend(bend)


def draw_boson(pnt1, pnt2, COLOR, label,
    displacement=-0.25, position=0.5, thickness=0, bend=0):
    global nboson, bosons

    nboson += 1
    bosons.append(Photon(pnt1, pnt2))
    if label != '':
        if displacement == 0.0 and position == 0.0:
            #print('Not moving boson label')
            bosons[nboson].addLabel(label)
        else:
            #print('Moving boson label by', displacement)
            bosons[nboson].addLabel(label, displace=displacement, pos=position)
    bosons[nboson].setStyles(COLOR)
    if thickness != 0:
        #print('Changing thickness to', thickness)
        bosons[nboson].addStyle(thickness)
    if bend != 0:
        #print('Changing bend to', bend)
        bosons[nboson].bend(bend)


def draw_gluon(pnt1, pnt2, COLOR, label,
    displacement=-0.25, position=0.5, thickness=0, bend=0):
    global ngluon, gluons

    ngluon += 1
    gluons.append(Gluon(pnt1, pnt2))
    if label != '':
        if displacement == 0.0 and position == 0.0:
            #print('Not moving gluon label')
            gluons[ngluon].addLabel(label)
        else:
            #print('Moving gluon label by', displacement)
            gluons[ngluon].addLabel(label, displace=displacement, pos=position)
    gluons[ngluon].setStyles(COLOR)
    if thickness != 0:
        #print('Changing thickness to', thickness)
        gluons[ngluon].addStyle(thickness)
    if bend != 0:
        #print('Changing bend to', bend)
        gluons[ngluon].bend(bend)


def draw_higgs(pnt1, pnt2, COLOR, label,
    displacement=-0.25, position=0.5, thickness=0, bend=0):
    global nhiggs, higgs

    nhiggs += 1
    higgs.append(Higgs(pnt1, pnt2))
    if label != '':
        if displacement == 0.0 and position == 0.0:
            #print('Not moving Higgs label')
            higgs[nhiggs].addLabel(label)
        else:
            #print('Moving Higgs label by', displacement)
            higgs[nhiggs].addLabel(label, displace=displacement, pos=position)
    higgs[nhiggs].setStyles(COLOR)
    if thickness != 0:
        #print('Changing thickness to', thickness)
        higgs[nhiggs].addStyle(thickness)
    if bend != 0:
        #print('Changing bend to', bend)
        higgs[nhiggs].bend(bend)
