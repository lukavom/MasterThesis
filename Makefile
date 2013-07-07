#
# Makefile to run latex, dvips, and pdflatex on a thesis
# Can also run feynmf on files in a directory
#
THESIS = mythesis
# EXTRACMD = --shell-escape
FEYNDIRNAME = ./feynmf
FEYNFILES = $(wildcard $(FEYNDIRNAME)/*.tex)
ifdef file
FEYNFILES = ./feynmf/$(file).tex
endif
TIKZDIRNAME = ./tikz
TIKZFILES = $(wildcard $(TIKZDIRNAME)/*.tex)

.PHONY: all new thesis thesis09 thesis11 \
	feynmf feynmp tikz \
	phdsubmit \
	cleanthesis cleancover \
	cleanfeynmf cleanfeynmp cleantikz cleanpictpdf \
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

feynmf: $(FEYNFILES)
	@echo "Feymf Feynman graph files: $^"
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
	@echo "Feynmp Feynman graph files: $^"
	$(foreach feynfile, $^, ./run_mp $(feynfile);)

tikz: $(TIKZFILES)
	@echo "TikZ Feynman graph files: $^"
	(cd tikz; $(foreach tikzfile, $^, pdflatex $(notdir $(tikzfile));))

thesis_feynmf:
	feynmf $(THESIS)

phdsubmit:
	pdflatex  PhD_submit
	pdflatex  PhD_submit

cleanall: clean cleanbbl cleanpictpdf

clean: cleanthesis cleancover cleanfeynmf cleanfeynmp cleantikz cleanphd cleanblx cleanglo

cleanthesis:
	-rm $(THESIS).log $(THESIS).aux $(THESIS).toc
	-rm $(THESIS).lof $(THESIS).lot $(THESIS).out
	-rm $(THESIS).blg $(THESIS).bbl $(THESIS).pdf
	-rm cover/*.aux $(THESIS)/*.aux

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

cleantikz:
	-rm tikz/*.log tikz/*.aux

cleanpictpdf:
	-rm feynmf/*.pdf
	-rm tikz/*.pdf

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
	@echo "feynmf: Run feynmf for all .tex files in $(FEYNDIRNAME)"
	@echo "feynmp: Run feynmp for all .tex files in $(FEYNDIRNAME)"
	@echo "cleanthesis: Clean up thesis LaTeX output files"
	@echo "cleanfeynmf: Clean up feynmf output files"

test:
	@echo "Thesis $(THESIS)"
	@echo "Feynmf Feynman graphs dir: $(FEYNDIRNAME)"
	@echo "Feynmf Feynman graphs files: $(FEYNFILES)"
	@echo "TikZ   Feynman graphs dir: $(TIKZDIRNAME)"
	@echo "TikZ   Feynman graphs files: $(TIKZFILES)"
