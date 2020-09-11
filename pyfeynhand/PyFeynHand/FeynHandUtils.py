# Utilities including class for storing and getting points
import argparse

def FeynHandColors(BW):
    """Define standard colors"""

    if BW:
        iCOLOR = oCOLOR = pCOLOR = vCOLOR = dCOLOR = 'Black'
    else:
        iCOLOR = 'Blue'
        oCOLOR = 'IndianRed'
        pCOLOR = 'ForestGreen'
        vCOLOR = 'Crimson'
        dCOLOR = 'DarkCyan'

    return (iCOLOR, oCOLOR, pCOLOR, vCOLOR, dCOLOR)

def FeynHandArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--BW', dest='BW', action='store_true', help='B&W output')
    parser.add_argument('-c', '--color', dest='BW', action='store_false', help='colour output')
    parser.add_argument('--colour', dest='BW', action='store_false', help='colour output')
    parser.add_argument('--pdf', action='store_true', help='run pdflatex')
    parser.add_argument('-t', '--title', action='store_true', help='include title')
    parser.add_argument('--debug', type=int, default=0)
    parser.set_defaults(BW=False)
    args = parser.parse_args()

    return args
