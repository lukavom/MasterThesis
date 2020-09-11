# PyFeynHand

Author: Ian C. Brock (ian.brock@cern.ch)

Single top (and more) Feynman diagrams using LaTeX TikZ-FeynHand package with a Python wrapper.

This package provides a wrapper around the LaTeX package TikZ-FeynHand for drawing Feynman graphs.
It creates a LaTeX file and optionally runs `pdflatex` on the file.
The TikZ-FeynHand package is available as of TeX Live 2017.

The advantages of `PyFeynHand` are:
* You can use Python to script Feynman graphs, while making direct use of LaTeX.
* You can use the same fonts as are used in ATLAS documents.
* You can use particle names defined by the `hepparticle`, `heppennames` and/or `hepnicenames` packages.
* You have the full power of `TikZ` behind you to do fancy things!
* You can either `\input` the LaTeX file or the resulting PDF files in your document.
* You can add text, lines, arrows and extra LaTeX code before and after the graph has been created.

The LaTeX file uses the `standalone` document class,
so can be `\input` directly into another LaTeX file.
You just have to include the `standalone` package in your document.
You can of course input the PDF file instead using `\includegraphics`.

Have a look at the `examples` directory for illustrations of what features are available.

This package supersedes the PyFeyn package, as this does not appear to be properly supported.
The graphs available in PyFeyn have been adapted for use with PyFeynHand.

## Feynman graph directories

The following directories exist:
* `example`: `tdecay.py` contains a colourful top-quark decay to illustrate how to change colours. It also includes extra text and lines.
* `Higgs`: Higgs boson production
* `s-channel`: single top-quark s-channel production
* `t-channel`: single top-quark t-channel production
* `tW`: single top-quark tW production
* `tdecay`: top-quark decay
* `ttbar`: top-antitop production
* `tgamq` Single top-quark production with a photon
* `tZq`: tZq t-channel production
* `FCNC-tZq`: tZ production via FCNC
* `WWscat`: WW scattering

These directories contain the Python scripts, as well as the resulting `tex` and `pdf` files.

## Feynman graph objects

Each graph should be created as an object using the `FeynHandTeX` constructor.
Vertices, propagators, text, lines, arrows and more can be added to the object
using the `Vertex`, `Propagator`, `Text`, `Line`, `Arrow` or `Draw` methods.

Write the graph to a `tex` (and optionally PDF) files using the `write` method.

## Colours

You can control the colours of both labels and lines.
By default the label colours will be the same as the external line or propagator colour.
Create the Feynman graph object `FeynHandTeX` with the option `lcolor='Black'` if you want black labels.

When you initialise the `FeynHandTeX` object you can specify:
* `font`: font package to use (default is newtx);
* `linewidth`: set the line width (and also the amplitude and width for photons and gluons). Default is `1pt`;
* `lcolor`: colour of vertex and propagator labels;
* `pcolor`: colour of propagator line;
* `vcolor`: colour of vertex dot;
* `debug`: debug level (default is 0).

When you create a vertex or propagator, you can also specify the colours of these three elements.
These override the default colours.

In the scripts I define a series of colours that are used:
* `iCOLOR`: incoming lines
* `oCOLOR`: outgoing lines
* `pCOLOR`: propagators
* `vCOLOR`: vertices
* `dCOLOR`: decay products, e.g. lepton from Z->ll decay

The defaults are set in `PyFeynHand/FeynHandUtils.py`.
You can adjust these colours if you want different ones and also use them for whatever purpose you like.

## Vertices

Vertices are points with names.
They are created using the `Vertex` method.
You have to give a coordinate a name and it can then be used in other objects,
such as propagators.

If you want to add a label to a vertex, which is a `dot` or a `blob`, just use `label='text'`.
If you want to change the position of the label, you can use the syntax `label='left:text'` etc.
Possible positions are `left`, `right`, `above`, `below`.
If you want to control the position and the colour of the label you can either specify everything in the label,
e.g. `label=below:\color{Green}\Pqt` or use the `lcolor` and `lpos` arguments together with `label=\Pqt`.

Vertex names cannot be used in extra text, lines and arrows at the moment.

## Propagators

The class is defined in `FeynHandPropagator.py`. Options that you might want to set:
* `reverse` to draw a fermion line on the opposite direction
* `labelRight` to put the label on a propagator on the right side instead of the left side of the line

You should first define vertices using the `Vertex` method.

## Text

The class is defined in `FeynHandText.py`.
You can add arbitrary text to the graph using the `Text` method of the `FeynHandTeX` class.
The text will be centred on the given coordinate.
Text, lines, arrow and extra draw commands will be default be added after the graph.
Pass the option `first=True` if you want to draw them before the graph.

## Lines

The class is defined in `FeynHandDraw.py`.
You can add a line to the graph using the `Line` method of the `FeynHandTeX` class.
If you want to add a label to a line, just use a propagator with style `plain`.

## Arrows

The class is defined in `FeynHandDraw.py` and inherits from `Line`.
You can add an arrow to the graph using the `Arrow` method of the `FeynHandTeX` class.

See the TikZ-FeynHand manual for details on how to draw fancy arrows.

## Draw

Add arbitrary LaTeX text and drawing commands to your graph.

## Further information

There is a `Makefile` in the main directory, which allows you to make some or all of the graphs.
Just type `make` in the top-level directory.
If you want to make all the graphs in a directory use a command like:
```
cd tZq; make -f ../Makefile tZq
```
You can use commands like `make -f ../Makefile cleandir`, 
`make -f ../Makefile cleandirpdf` to remove temporary files or PDF files in a directory.

Some of the graphs are available for both the four-flavour (4FS) and the five-flavour (5FS) schemes.
Versions of some graphs exist that include the decays of the top quark and the W and Z bosons.
The filenames contain `decay`.

If you want black and white versions of the graphs, pass the option `--BW` or `-b` to the script.
The filenames then get `BW` appended.
If you want the PDF file to be created. pass the option `--pdf` to the script.
If you need to do some debugging, pass the option `--debug=N`, where `N` is a number.
Some graphs include an (optional) title. You can get the title by passing the `--title` option to the script.

If you want to use the package to make your own Feynman graphs, note that
the `PyFeynHand` directory has to be linked from the directory with the Feynman graphs.

The default setting uses the `newtx` fonts, which are the default fonts for ATLAS documents.
Other fonts can be used by passing the package name you want to use to the `FeynHandTeX` object,
e.g. `font='txfonts'`.

The default line thickness can be changed by passing `linewidth` to the `FeynHandTeX` object.
The default setting in PyFeynHand is `linewidth=1.0pt`.
The TikZ-FeynHand uses as default to `0.5pt`, which I find very thin.
It may be better to use an even larger value for slides.
However, changing the line width also changes the amplitude and frequency of photon and gluon oscillations.

