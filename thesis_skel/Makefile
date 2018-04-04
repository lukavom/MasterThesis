# Makefile to run latex, dvips, and pdflatex on a thesis
# Can also run feynmf/feynmp/tikz on files in a directory

THESIS = mythesis
# EXTRACMD = --shell-escape
FEYNDIR = feynmf
FEYNFILES = $(wildcard $(FEYNDIR)/*.tex)
TIKZDIR = tikz
TIKZFILES = $(wildcard $(TIKZDIR)/*.tex)
PYFEYNDIR = pyfeyn
PYFEYNFILES = $(wildcard $(PYFEYNDIR)/*.py)
ifdef file
FEYNFILES = $(FEYNDIR)/$(file).tex
TIKZFILES = $(TIKZDIR)/$(file).tex
PYFEYNFILES = $(PYFEYNDIR)/$(file).py
endif
BIBTEX = biber
AWKDIR=..

.PHONY: cover \
	feynmf feynmp tikz pyfeyn \
	cleanthesis cleancover \
	cleanfeynmf cleanfeynmp cleantikz cleanpyfeyn cleanpictpdf \
	cleanblx cleanbbl \
	cleanglo cleanlatexmk\
	help test

thesis: run_latexmk

# Use latexmk to compile thesis
run_latexmk:  $(THESIS).tex *.tex bib/*.bib
	latexmk -pdf $(THESIS)
	# LATEXMK = latexmk -e '$$pdflatex=q/pdflatex %O -shell-escape %S/' -pdf $(THESIS)

# - in front of bibtex means compilation continues even if there is an error
thesis09: $(THESIS).tex *.tex bib/*.bib
	pdflatex   $(EXTRACMD) $(THESIS)
	-bibtex $(THESIS)
	# makeglossaries $(THESIS)
	pdflatex   $(EXTRACMD) $(THESIS)
	pdflatex   $(EXTRACMD) $(THESIS)

thesis11: $(THESIS).tex *.tex bib/*.bib
	pdflatex   $(EXTRACMD) $(THESIS)
	$(BIBTEX)  $(THESIS)
	# makeglossaries $(THESIS)
	pdflatex   $(EXTRACMD) $(THESIS)
	pdflatex   $(EXTRACMD) $(THESIS)

cover:
	pdflatex   $(EXTRACMD) cover_only
	pdflatex   $(EXTRACMD) cover_only

feynmf:
	make -f ../Makefile FEYNDIR=$(FEYNDIR) FEYNFILES="$(FEYNFILES)" \
	 AWKDIR=$(AWKDIR) feynmf

feynmp:
	make -f ../Makefile FEYNDIR=$(FEYNDIR) FEYNFILES="$(FEYNFILES)" \
	 AWKDIR=$(AWKDIR) feynmp

tikz:
	make -f ../Makefile TIKZDIR=$(TIKZDIR) TIKZFILES="$(TIKZFILES)" tikz

pyfeyn:
	make -f ../Makefile PYFEYNDIR=$(PYFEYNDIR) PYFEYNFILES="$(PYFEYNFILES)" pyfeyn

thesis_feynmf:
	feynmf $(THESIS)

cleanall: clean cleanbbl cleanpictpdf

clean: cleanthesis cleancover \
	cleanfeynmf cleanfeynmp cleantikz \
	cleanblx cleanglo cleanlatexmk

cleanthesis:
	-rm $(THESIS).log $(THESIS).aux $(THESIS).toc
	-rm $(THESIS).lof $(THESIS).lot $(THESIS).out
	-rm $(THESIS).blg $(THESIS).bbl $(THESIS).pdf
	-rm $(THESIS).fdb_latexmk .$(THESIS).lb $(THESIS).synctex.gz
	-rm *.aux

cleancover:
	-rm cover_only.log cover_only.aux cover_only.out
	-rm cover_only.pdf

cleanfeynmf:
	-rm *.mf *.tfm *.t1 *.600gf *.600pk *.log
	-rm feynmf_all.* feynmf_files.inp

cleanfeynmp:
	-rm *.1 *.log *.mp *.t1
	-rm feynmf_all.* feynmf_files.inp

cleantikz:
	-rm $(TIKZDIR)/*.log $(TIKZDIR)/*.aux

cleanpyfeyn:
	-rm $(PYFEYNDIR)/*.pdf

cleanpictpdf:
	-rm $(FEYNDIR)/*.pdf
	-rm $(TIKZDIR)/*.pdf
	-rm $(PYFEYNFDIR)/*.pdf

cleanblx:
	-rm *-blx.bib
	-rm *.bcf
	-rm *.run.xml

cleanbbl:
	-rm *.bbl

cleanglo:
	-rm *.acn *.acr *.alg
	-rm *.glg *.glo *.gls
	-rm *.ist

cleanlatexmk:
	-rm *.fdb_latexmk *.fls

help:
	@echo "Possible commands:"
	@echo "new [THESIS=dirname]: Set up a new thesis"
	@echo "thesis: Compile complete thesis (latexmk)"
	@echo "run_latexmk: Compile complete thesis using latexmk"
	@echo "thesis11: Compile complete thesis - texlive >=2011 + biber"
	@echo "thesis09: Compile complete thesis - texlive 2009 + bibtex"
	@echo "feynmf: Run feynmf for all .tex files in $(FEYNDIR)"
	@echo "feynmp: Run feynmp for all .tex files in $(FEYNDIR)"
	@echo "tikz:   Run tikz for all .tex files in $(TIKZDIR)"
	@echo "clean:         Clean up most auxiliary files (leaves bbl and picture PDF files)"
	@echo "cleanall:      Clean up all auxiliary files"
	@echo "cleanthesis:   Clean up thesis LaTeX output files"
	@echo "cleanbbl:      Clean up thesis bbl files"
	@echo "cleanblx:      Clean up thesis biber files"
	@echo "cleanfeynmf:   Clean up feynmf output files"
	@echo "cleantikz:     Clean up tikz temparary files"
	@echo "cleanpyfeyn:   Clean up pyfeyn PDF files"
	@echo "cleanpictpdf:  Clean up picture output in $(FEYNDIR), $(TIKZDIR) and $(PYFEYNDIR)"
	@echo "cleanglo:      Clean up glossary output files"
	@echo "cleanlatexmk:  Clean up latexmk files"

test:
	@echo "Thesis $(THESIS)"
	@echo "Feynmf Feynman graphs dir: $(FEYNDIRNAME)"
	@echo "Feynmf Feynman graphs files: $(FEYNFILES)"
	@echo "TikZ   Feynman graphs dir: $(TIKZDIRNAME)"
	@echo "TikZ   Feynman graphs files: $(TIKZFILES)"
	@echo "PyFeyn Feynman graphs dir: $(PYFEYNDIRNAME)"
	@echo "PyFeyn Feynman graphs files: $(PYFEYNFILES)"
