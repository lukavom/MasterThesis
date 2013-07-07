#
# Makefile to run latex, dvips, and pdflatex on a thesis
# Can also run feynmf on files in a directory
#
GUIDE = thesis_guide
GUIDEDIR = ./
# EXTRACMD = --shell-escape
FEYNDIRNAME = ../feynmf
FEYNFILES = $(wildcard $(FEYNDIRNAME)/*.tex)
ifdef file
FEYNFILES = ../feynmf/$(file).tex
endif
TIKZDIRNAME = ../tikz
TIKZFILES = $(wildcard $(TIKZDIRNAME)/*.tex)

.PHONY: all guide guide09 guide11 \
	feynmf feynmp tikz \
	cleanguide \
	cleanfeynmf cleanfeynmp  cleantikz cleanpictpdf \
	cleanblx cleanbbl \
	cleanglo \
	help test

guide: guide11

guide09:
	pdflatex  $(EXTRACMD) $(GUIDE)
	bibtex    $(GUIDE)
	pdflatex  $(EXTRACMD) $(GUIDE)
	bibtex    $(GUIDE)
	makeindex $(GUIDE)
	makeglossaries $(GUIDE)
	pdflatex  $(GUIDE)
	pdflatex  $(GUIDE)

guide11:
	pdflatex  $(EXTRACMD) $(GUIDE)
	biber     $(GUIDE)
	makeindex $(GUIDE)
	makeglossaries $(GUIDE)
	pdflatex  $(EXTRACMD) $(GUIDE)
	pdflatex  $(GUIDE)

feynmf: $(FEYNFILES)
	@echo "Feynmf Feynman graph files: $^"
	-rm feynmf_files.inp
	touch feynmf_files.inp
	# $(foreach feynfile, $^, echo $(notdir $(feynfile)) >>feynmf_files.inp;)
	$(foreach feynfile, $^, echo $(feynfile) >>feynmf_files.inp;)
	cat feynmf_files.inp
	cat feynmf_files.inp | awk -f ../awk_feynmf >feynmf_all.tex
	# latex feynmf_all; feynmf feynmf_all; latex feynmf_all; latex feynmf_all
	-pdflatex feynmf_all
	$(foreach feynfile, $^, ../run_mf $(feynfile);)
	pdflatex feynmf_all; pdflatex feynmf_all; pdflatex feynmf_all

feynmp: $(FEYNFILES)
	@echo "Feynmp Feynman graph files: $^"
	$(foreach feynfile, $^, ../run_mp $(feynfile);)

tikz: $(TIKZFILES)
	@echo "TikZ Feynman graph files: $^"
	(cd ../tikz; $(foreach tikzfile, $^, pdflatex $(notdir $(tikzfile));))

cleanall: clean cleanbbl cleanpictpdf

clean: cleanguide cleanfeynmf cleanfeynmp cleantikz cleanblx cleanglo

cleanguide:
	-rm $(GUIDEDIR)$(GUIDE).log $(GUIDEDIR)$(GUIDE).aux $(GUIDEDIR)$(GUIDE).toc
	-rm $(GUIDEDIR)$(GUIDE).lof $(GUIDEDIR)$(GUIDE).lot $(GUIDEDIR)$(GUIDE).out
	-rm $(GUIDEDIR)$(GUIDE).blg $(GUIDEDIR)$(GUIDE).bbl $(GUIDEDIR)$(GUIDE).pdf
	-rm $(GUIDEDIR)$(GUIDE)-blx.bib $(GUIDEDIR)$(GUIDE).bcf $(GUIDEDIR)$(GUIDE).run.xml
	-rm $(GUIDEDIR)$(GUIDE).ind $(GUIDEDIR)$(GUIDE).idx $(GUIDEDIR)$(GUIDE).ilg
	-rm $(GUIDEDIR)$(GUIDE).acn $(GUIDEDIR)$(GUIDE).acr $(GUIDEDIR)$(GUIDE).alg
	-rm $(GUIDEDIR)$(GUIDE).glg $(GUIDEDIR)$(GUIDE).glo $(GUIDEDIR)$(GUIDE).gls
	-rm $(GUIDEDIR)$(GUIDE).ist
	-rm $(GUIDEDIR)/*.aux

cleanfeynmf:
	-rm *.mf *.tfm *.t1 *.600gf *.600pk *.log
	-rm feynmf_all.* feynmf_files.inp

cleanfeynmp:
	-rm *.1 *.log *.mp *.t1
	-rm feynmf_all.* feynmf_files.inp

cleantikz:
	-rm ../tikz/*.log ../tikz/*.aux

cleanpictpdf:
	-rm ../feynmf/*.pdf
	-rm ../tikz/*.pdf

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

help:
	@echo "Possible commands:"
	@echo "guide: Compile thesis guide (guide11)"
	@echo "guide09: Compile thesis guide - texlive 2009 + bibtex"
	@echo "guide11: Compile thesis guide - texlive >=2011 + biber"
	@echo "feynmf: Run feynmf for all .tex files in $(FEYNDIRNAME)"
	@echo "feynmp: Run feynmp for all .tex files in $(FEYNDIRNAME)"
	@echo "cleanguide:  Clean up guide  LaTeX output files"
	@echo "cleanfeynmf: Clean up feynmf output files"
	@echo "cleanfeynmp: Clean up feynmp output files"

test:
	@echo "Guide $(GUIDE)"
	@echo "Feynman graphs dir: $(FEYNDIRNAME)"
