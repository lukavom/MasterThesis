#
# Makefile to run latex, dvips, and pdflatex on a thesis
# Can also run feynmf on files in a directory
#
THESIS = mythesis
GUIDE = thesis_guide
# EXTRACMD = --shell-escape
FEYNDIRNAME = ./feynmf
FEYNFILES = $(wildcard $(FEYNDIRNAME)/*.tex)
ifdef file
FEYNFILES = ./feynmf/$(file).tex
endif


.PHONY: all thesis thesis09 thesis11 guide guide09 guide11 feynmf new \
	phdsubmit \
	cleanthesis cleanguide cleancover cleanfeynmf cleanfeynmp \
	cleanphd cleanblx cleanbbl \
	cleanglo \
	help test

new:
	mkdir $(THESIS)
	cp thesis_skel/thesis_defs.sty        $(THESIS)/
	cp thesis_skel/thesis_refs.bib        $(THESIS)/
	cp thesis_skel/thesis_intro.tex       $(THESIS)/
	cp thesis_skel/thesis_appendix.tex    $(THESIS)/
	cp thesis_skel/thesis_acknowledge.tex $(THESIS)/
	cp thesis_skel/thesis_cv.tex $(THESIS)/
	cp thesis_skel.tex $(THESIS).tex

thesis: thesis11

thesis09:
	pdflatex  $(EXTRACMD) $(THESIS)
	bibtex    $(THESIS)
	# makeglossaries $(THESIS)
	pdflatex  $(EXTRACMD) $(THESIS)
	pdflatex  $(EXTRACMD) $(THESIS)

thesis11:
	pdflatex  $(EXTRACMD) $(THESIS)
	biber     $(THESIS)
	# makeglossaries $(THESIS)
	pdflatex  $(EXTRACMD) $(THESIS)
	pdflatex  $(EXTRACMD) $(THESIS)

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
	@echo "Feynman graph files: $^"
	-rm feynmf_files.inp
	touch feynmf_files.inp
	# $(foreach feynfile, $^, echo $(notdir $(feynfile)) >>feynmf_files.inp;)
	$(foreach feynfile, $^, echo $(feynfile) >>feynmf_files.inp;)
	cat feynmf_files.inp
	cat feynmf_files.inp | awk -f awk_feynmf >feynmf_all.tex
	# latex feynmf_all; feynmf feynmf_all; latex feynmf_all; latex feynmf_all
	-pdflatex feynmf_all
	$(foreach feynfile, $^, ./run_mf $(feynfile);)
	pdflatex feynmf_all; pdflatex feynmf_all; pdflatex feynmf_all

feynmp: $(FEYNFILES)
	@echo "Feynman graph files: $^"
	$(foreach feynfile, $^, ./run_mp $(feynfile);)

thesis_feynmf:
	feynmf $(THESIS)

phdsubmit:
	pdflatex  PhD_submit
	pdflatex  PhD_submit

cleanall: clean cleanbbl

clean: cleanthesis cleanguide cleancover cleanfeynmf cleanfeynmp cleanphd cleanblx cleanglo

cleanthesis:
	-rm $(THESIS).log $(THESIS).aux $(THESIS).toc
	-rm $(THESIS).lof $(THESIS).lot $(THESIS).out
	-rm $(THESIS).blg $(THESIS).bbl $(THESIS).pdf
	-rm cover/*.aux $(THESIS)/*.aux

cleanguide:
	-rm $(GUIDE).log $(GUIDE).aux $(GUIDE).toc
	-rm $(GUIDE).lof $(GUIDE).lot $(GUIDE).out
	-rm $(GUIDE).blg $(GUIDE).bbl $(GUIDE).pdf
	-rm $(GUIDE)-blx.bib $(GUIDE).bcf $(GUIDE).run.xml
	-rm $(GUIDE).ind $(GUIDE).idx $(GUIDE).ilg
	-rm $(GUIDE).acn $(GUIDE).acr $(GUIDE).alg
	-rm $(GUIDE).glg $(GUIDE).glo $(GUIDE).gls
	-rm $(GUIDE).ist
	-rm guide/*.aux

cleancover:
	-rm cover_only.log cover_only.aux cover_only.out
	-rm cover_only.pdf
	-rm cover_test.log cover_test.aux cover_test.toc
	-rm cover_test.lof cover_test.lot cover_test.out
	-rm cover_test.blg cover_test.bbl cover_test.pdf

cleanphd:
	-rm PhD_submit.log PhD_submit.aux PhD_submit.out
	-rm PhD_submit.pdf

cleanfeynmf:
	-rm *.mf *.tfm *.t1 *.600gf *.600pk *.log
	-rm feynmf_all.* feynmf_files.inp

cleanfeynmp:
	-rm *.1 *.log *.mp *.t1
	-rm feynmf_all.* feynmf_files.inp

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
	@echo "new [THESIS=dirname]: Set up a new thesis"
	@echo "thesis: Compile complete thesis (thesis11)"
	@echo "thesis09: Compile complete thesis - texlive 2009 + bibtex"
	@echo "thesis11: Compile complete thesis - texlive >=2011 + biber"
	@echo "guide: Compile thesis guide (guide11)"
	@echo "guide09: Compile thesis guide - texlive 2009 + bibtex"
	@echo "guide11: Compile thesis guide - texlive >=2011 + biber"
	@echo "feynmf: Run feynmf for all .tex files in $(FEYNDIRNAME)"
	@echo "feynmp: Run feynmp for all .tex files in $(FEYNDIRNAME)"
	@echo "cleanthesis: Clean up thesis LaTeX output files"
	@echo "cleanguide:  Clean up guide  LaTeX output files"
	@echo "cleanfeynmf: Clean up feynmf output files"

test:
	@echo "Thesis $(THESIS)"
	@echo "Feynman graphs dir: $(FEYNDIRNAME)"
