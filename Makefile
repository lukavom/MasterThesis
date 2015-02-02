#
# Makefile to create a new thesis skeleton
# Can also run feynmf/feynmp/tikz on files in a directory
#
THESIS = mythesis
# EXTRACMD = --shell-escape
ifndef FEYNDIR
FEYNDIR = ./feynmf
endif
ifndef FEYNFILES
FEYNFILES = $(wildcard $(FEYNDIR)/*.tex)
endif
ifndef TIKZDIR
TIKZDIR = ./tikz
endif
ifndef TIKZFILES
TIKZFILES = $(wildcard $(TIKZDIR)/*.tex)
endif
ifdef file
FEYNFILES = $(FEYNDIR)/$(file).tex
TIKZFILES = $(TIKZDIR)/$(file).tex
endif
ifndef AWKDIR
AWKDIR = .
endif
ifndef MPOSTDIR
MPOSTDIR = ./mpost_tmp
endif

.PHONY: new astro \
	feynmf feynmp tikz \
	cleanfeynmf cleanfeynmp cleantikz cleanpictpdf \
	help test

new:
	mkdir $(THESIS)
	cp thesis_skel/thesis_skel.tex        $(THESIS)/$(THESIS).tex
	cp thesis_skel/thesis_defs.sty        $(THESIS)/
	cp thesis_skel/thesis_refs.bib        $(THESIS)/
	cp thesis_skel/thesis_intro.tex       $(THESIS)/
	cp thesis_skel/thesis_appendix.tex    $(THESIS)/
	cp thesis_skel/thesis_acknowledge.tex $(THESIS)/
	cp thesis_skel/thesis_cv.tex          $(THESIS)/
	cp thesis_skel/cover_only.tex         $(THESIS)/
	cp ubonn-thesis.sty                   $(THESIS)/
	cp ubonn-biblatex.sty                 $(THESIS)/
	cp thesis_skel/Makefile               $(THESIS)/

astro:
	mkdir $(THESIS)
	cp thesis_skel/thesis_astro_skel.tex  $(THESIS)/$(THESIS).tex
	cp thesis_skel/thesis_defs.sty        $(THESIS)/
	cp thesis_skel/thesis_refs.bib        $(THESIS)/
	cp thesis_skel/thesis_astro_intro.tex $(THESIS)/thesis_intro.tex
	cp thesis_skel/thesis_appendix.tex    $(THESIS)/
	cp thesis_skel/thesis_acknowledge.tex $(THESIS)/
	cp thesis_skel/thesis_cv.tex          $(THESIS)/
	cp thesis_skel/cover_only.tex         $(THESIS)/
	cp ubonn-thesis.sty                   $(THESIS)/
	cp ubonn-biblatex.sty                 $(THESIS)/
	cp thesis_skel/Makefile               $(THESIS)/

feynmf: $(FEYNFILES)
	@echo "Feymf Feynman graph files: $^"
	-rm feynmf_files.inp
	touch feynmf_files.inp
	$(foreach feynfile, $^, echo $(feynfile) >>feynmf_files.inp;)
	cat feynmf_files.inp
	cat feynmf_files.inp | awk -f $(AWKDIR)/awk_feynmf >feynmf_all.tex
	-pdflatex feynmf_all
	$(foreach feynfile, $^, $(AWKDIR)/run_mf $(feynfile);)
	pdflatex feynmf_all; pdflatex feynmf_all; pdflatex feynmf_all

feynmp: $(FEYNFILES)
	@echo "Feynmp Feynman graph files: $^"
	$(foreach feynfile, $^, $(AWKDIR)/run_mp $(feynfile);)

tikz: $(TIKZFILES)
	@echo "TikZ Feynman graph files: $^"
	(cd $(TIKZDIR); $(foreach tikzfile, $^, pdflatex $(notdir $(tikzfile));))

cleanall: clean cleanpictpdf

clean: cleanfeynmf cleanfeynmp cleantikz

cleanfeynmf:
	-rm *.mf *.tfm *.t1 *.600gf *.600pk *.log
	-rm feynmf_all.* feynmf_files.inp

cleanfeynmp:
	-rm $(MPOSTDIR)/*.1   $(MPOSTDIR)/*.log
	-rm $(MPOSTDIR)/*.mp  $(MPOSTDIR)/*.t1
	-rm $(MPOSTDIR)/*.aux
	-rm $(MPOSTDIR)/*_mp.tex $(MPOSTDIR)/*_mp.pdf
	-rmdir $(MPOSTDIR)

cleantikz:
	-rm $(TIKZDIR)/*.log $(TIKZDIR)/*.aux

cleanpictpdf:
	-rm $(FEYNDIR)/*.pdf
	-rm $(TIKZDIR)/*.pdf

help:
	@echo "Possible commands:"
	@echo "new [THESIS=dirname]: Create a new thesis skeleton"
	@echo "feynmf: Run feynmf for all .tex files in $(FEYNDIR)"
	@echo "feynmp: Run feynmp for all .tex files in $(FEYNDIR)"
	@echo "tikz:   Run tikz for all .tex files in $(TIKZDIR)"
	@echo "cleanfeynmf: Clean up feynmf output files"
	@echo "cleanfeynmp: Clean up feynmp output files"
	@echo "cleantikz:   Clean up tikz   output files"

test:
	@echo "Feynmf Feynman graphs dir: $(FEYNDIR)"
	@echo "Feynmf Feynman graphs files: $(FEYNFILES)"
	@echo "TikZ   Feynman graphs dir: $(TIKZDIR)"
	@echo "TikZ   Feynman graphs files: $(TIKZFILES)"
