Version 7.0 29/05/2020

The idea with this package is that you also look at the LaTeX that
is used to create it, in order to find out how things are done.

The files that make up this package are available in a Git
repository and as a tar file. To get the latest version
give the command:
```
git clone https://bitbucket.team.uni-bonn.de/scm/uni/ubonn-thesis.git
```

If you want a particular release use the command:
```
git clone --branch v6.0 https://bitbucket.team.uni-bonn.de/scm/uni/ubonn-thesis.git
```

The tar file also includes the guide as a PDF file: guide/thesis_guide.pdf.
It can be obtained from:

https://www.pi.uni-bonn.de/lehre/uni-bonn-thesis

You can give the command:
```
make new [THESIS=dirname] [TEXLIVE=YYYY]
```
to create a new directory with a few files to help you get
started. By default the directory name will be mythesis.
To compile your thesis try:
```
cd mythesis [or dirname]
make thesis
```

All packages that are needed should be part of your TeX
installation. If not you may have to install them or ask your system
administrator to do so.

My original idea was that the style file should work for all recent
TeX installations.  However, some of the packages I recommend have
been changing quite a lot over the past few years, particularly
biblatex and siunitx.  It may therefore be necessary to make a few
changes in order to get the thesis to compile on your machine. The
default version assumes that you have TeX Live 2013 or later.  If you
have an older version pass the option 'texlive=YYYY' to the document class
or ubonn-thesis package in mythesis.tex.
If you make a new document, you can do this by passing the argument 
`TEXLIVE=YYYY` when giving the command `make new`.

If you just want to make the cover pages, use the file cover_only.tex.
Be sure to adapt the font selected in ubonn-thesis.sty to the font
you actually used in your thesis. Be aware that not all font sizes are
available in all font collections. If you used the default LaTeX font
in your thesis, then choose lmodern in the style file.

The main file for this guide is `guide/thesis_guide.tex` and it
includes the LaTeX files in the directory `./guide` and the
Feynman graphs in the directories `./feynmf` and `./tikz`.

You can create your own copy of the guide using the commands:
```
cd guide
make guide
```

If you have a version of TeX Live older than 2016, you should set 
\texlive appropriately thesis_guide.tex and
should not pass the newtx option to ubonn-thesis.
Support for TeX Live versions older than 2011 has been removed in Version 7.0.

The guide also includes a description of how to use the package under
Windows.