import pyx

# Get my extra functions
from .draw_stuff import draw_fermion, draw_boson, draw_gluon, draw_higgs

__all__ = ['draw_fermion', 'draw_boson', 'draw_gluon', 'draw_higgs']

# Define font and colours for LaTeX
pyx.text.defaulttexrunner.preamble(r"\usepackage[T1]{fontenc}")
# pyx.text.defaulttexrunner.preamble(r"\usepackage[varg]{txfonts}")
pyx.text.defaulttexrunner.preamble(r"\usepackage{newtxtext}")
pyx.text.defaulttexrunner.preamble(r"\usepackage{newtxmath}")
# pyx.text.defaulttexrunner.preamble(r"\usepackage{mathpazo}")
# pyx.text.defaulttexrunner.preamble(r"\usepackage[scaled]{helvet}")
pyx.text.defaulttexrunner.preamble(r"\usepackage[dvipsnames]{xcolor}")
# pyx.text.defaulttexrunner.preamble(r"\usepackage[italic]{hepnicenames}")
