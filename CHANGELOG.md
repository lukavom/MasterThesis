# Changelog

All notable changes to the University of Bonn thesis style are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

Changes are sorted into the following categories:
Added, Changed, Deprecated, Removed, Fixed, Security.

## [Unreleased] - 2021-06-15

### Added

- Add option `twoside` to be used for printed and PDF versions of theses.
- Add options for the `diffcoeff` and `derivative` packages.
- Add `scrhack` package to get rid of some KOMA-Script warnings.
- Add some discussion on "fluff".
- Add some instructions for Fedora 33.

### Changed

- TeX Live 2017 is now the default.
- Table captions moved to above the table by default - steer caption spacing with option `tableheading`.
- Replace `amsmath` by `mathtools`.
- Switched from `xtab` to `longtable` as default package for long tables, as `longtable` and `supertabular` seem to be more actively maintained.
- Turn on use of `cleveref` package by default.
- Turn off `dcolumn` by default, as there are (better) alternatives.
- Latest version of `PyFeynHand` scripts.
- `backref`, `maxbibnames` and `block` options actually work and should be passed to `ubonn-biblatex.sty`.
- Shuffle instructions on compiling guide.
- Several tweaks and improvements to usage of LuaLaTeX and XeLaTeX.
- Use filenames instead of font names for LuaLasTeX and XeLaTeX fonts.
- Use `\ifthenelse` instead of standard `if` in many places.

### Deprecated

- Deprecate the usage of `physics`.

### Removed

- Remove support and documentation for TeX Live versions older than 2013.
- `firstinits` option removed, as steering is done by TeX Live version.
- Remove definition of `\dif`, as it is better to use a package such as `diffcoeff` for derivatives.
- Remove lots of commented out code for older TeX Live versions.
- Remove `thesis-2009-skel.tex` file, as support has been dropped for such old versions.
- Remove old `biblatex` directory and the style files in there, as they are superseded by `ubonn-biblatex.sty`.

## [7.0.0] - 2020-06-19

### Added

- Thesis skeleton and guide can also be compiled using LuaLaTeX and XeLaTeX.
- Add some documentation on making Feynman graphs using TikZ packages.
- Add usage of `tcolorbox` to thesis guide for listings.
- Add `bookmark` package to improve bookmarking of appendices in PDF files.

### Changed

- Tweak `hyperref` settings a bit.

### Deprecated

- Deprecate the usage of `PyFeyn`.

### Removed

- Remove support and documentation for TeX Live versions older than 2011.

## [6.0] - 2018-12-05

### Added

- Add a command `make update` to update to a newer version of the style files.
- Add a section on "Typical English mistakes".
- Add documentation on `todonotes` and `cleveref` packages.
- Add information on how to handle errata.

### Changed

- TeX Live 2016 is now the default.
- After a `make new` the `mythesis` directory should now be standalone. This make it easier to use Git etc.
- Bibliography files now go in the `bib` subdirectory.
- Use `latexmk` by default to compile.
- Switch to `newtx` as the default font.
- Switch from `scrpage2` to `scrlayer-scrpage` package.
- Improve bar width in `heppennames` and `hepnicenames`.
- Switch to version 4 of `mhchem`.

### Deprecated

- The thesis guide no longer compiles using TeX Live versions earlier than 2011, as it uses some packages that were not available then.
  
## [5.1] - 2016-06-30

### Added

- Add `hepnicenames` and `heppennames` packages.
- Add a bit more documentation on particle definitions.
- Add some more information and updated the guidelines on positioning of figures.

### Changed

- Month and address/location are not included in references by default.

## [5.0] - 2016-03-15

### Added

- Add a workaround for conflicts involving `refcheck`, `subcaption` and `refcheck`.

### Changed

- Move from SVN to Git repository. Update documentation accordingly.
- Small fix so comma is not part of link from journal entry to DOI.

## [4.0] - 2015-08-27

### Added

- Add options for thesis type and stage.
- This simplifies and improves how the different cover and title pages are included.
- Add a skeleton that compiles with TeX Live 2009 - `make new09` command.
- Add ATLAS bibliography style files.

### Changed

- Put bibliography before appendix (this seems to be more standard).
- With this the bibliography moves into \Macro{mainmatter}.
- Use KOMA-Script options to add lines around chapter headings - small change to the style.
- The 2009 version of the skeleton now uses traditional BibTeX.
- Small updates to submission instructions and operating systems.

### Removed

- Remove most advice and switches to use `bibtex8`.
  
## [3.0] - 2015-02-02

### Added

- Add ability to pass options to `ubonn-thesis.sty` using the `keyval` package.
- Add options for different fonts. Stick with `txfonts` as default, but encourage use of `newtx` if it is available.
- Add inclusion of `biblatex` package into style file.
- Add options so that bibliography in standard astronomy style can be produced.
- Add `boldmath` command to bold font by default.

### Changed

- TeX Live 2014 is now the default.
- The TeX Live version can be passed as an option. Improve its handling.
- Change a few default packages:
  - `longtable` -> `xtab`;
  - `subfig` -> `subcaption` (for TeX Live 2012 and later).
- Put `biblatex` fine tuning into a new style file `ubonn-biblatex.sty`.

### Removed

- Remove inclusion of `feynmf/feynmp` by default.

## [2.1] - 2013-07-10

### Added

- Add commented out code to `feynmp` figures to show how to use `standalone` for them as well.
- Add a few examples of using the `tikz` package.
- Add `write18` statements for Feynman graphs with `feynmp` and adapt `Makefile`.
- Add some information on the `refcheck` package and back-referencing with `biblatex`.

### Changed

- Move thesis main file to `mythesis` subdirectory.
- Also put `Makefile` and copy `ubonn-thesis.sty` into `mythesis` subdirectory.
- Split main `Makefile` into several files, one for thesis, one for the guide an done for pictures and Feynman graphs.
- Use the `standalone` package in the TikZ figures.
- Move the guide main file to the `guide` subdirectory so that this works properly.
- Switch to using `feynmp` rather than `feynmf` by default (as of TeX Live 2011).
  
## [2.0] - 2013-04-23

### Changed

- Rename `pibonn-thesis` to `ubonn-thesis`.
- Make thesis submission a separate chapter (so that PhD submission can also be a separate document).
- Make TeX Live 2011 the default.
- Make Inspire rather than Spires default.

## [1.0] - [1.0]

The following changes are ordered by date and do not have a version number associated with them.

- 31 Mar 2013: Add instructions on how to use LaTeX backport under Ubuntu variants.
- 28 Mar 2013: Updated and hopefully complete and correct instructions on thesis submission.
    Move to `USenglish` and `UKenglish` as languages rather than `american` and `british`.
- 14 Mar 2013: Change the style of the chapter heading. Add some more instructions which cover pages are needed when.
- 24 Jan 2013: Add watermark possibility with `background` package.
- 14 Dec 2012: Added a glossary and a list of acronyms as well as instructions on how to make them.
    Skeleton CV for PhD thesis added; this still has to be cross-checked with the Promotionsbüro.
- 04 Dec 2012: Add some hints on what title pages to use when and what you have to worry about when printing and submitting your thesis.
- 02 Dec 2012: Use American-style quotation marks by default with the `csquotes` package. This means outer "double quote and inner 'single quote'", which seems to be quite common, even in British (UK) English publications such as CERN Courier.
- 22 Oct 2012: Replace `color` by `xcolor` so that one can colour boxes around links.
- 12 Oct 2012: Add some more information on installing TeX Live 2011.
    Add some thesis examples. Add some hints on using Kile.
    Sorting of references turned off for TeX Live 2011.
    Some more information on which reference types to use added.
- 24 Aug 2012: Update SVN information due to PI changes.
- 19 Jun 2012: Make a separate file for cover so that page numbering starts properly.
- 18 Jun 2012: Add instructions for TeX Live under Windows.
- 05 Jun 2012: Move current version into the trunk subdirectory to conform to usual SVN structure.
- 24 May 2012: Made the guide more generic so that it can be sent to other institutes.
    Used `ifthenelse` everywhere rather than having separate files for different TeX Live versions.
- 15 May 2012: Reorganised switching between TeX Live 2009 and 2011.
    The version should be set first before loading the style file.
    Without the option TeX Live 2009 is assumed.
    Some changes to adapt to stricter `siunitx` version 2 requirements and new options.
    Added some comments on ways of writing axis names for coordinates.
    Added some information on using `feynmp` rather than `feynmf`.
- 14 May 2012: Only include one title page for Bachelor theses.
    Add some more sources of information.
    Reorganise and improve a bit the references chapter.
    Reorganise information on installing a TeX setup.
    Move Windows XP to a separate subsection. Add a bit of information for macOS.
    Add a bit of information on the `subfiles` package.
- 06 Mar 2012: Add more information on formatting footnotes.
- 23 Jan 2012: Added more and better examples of using the `S` column format in tables.
- 20 Jan 2012: Add more information on `biblatex` and make this the default (unsorted, numeric) for a thesis.
- 11 Jul 2011: Removed dot after chapter and figure/table numbers.
- 17 Jun 2011: Added discussion of `siunitx` package.
    Added some extra tables that also use this package.
    Added `booktabs` package which includes `\toprule`, `\midrule` and `\bottomrule` to get better looking tables.
    Also switched from `\usepackage` to `\RequirePackage` in `ubonn-thesis.sty.
- 23 May 2011: Changed default font to `txfonts`. Added more font options and explanation.

## [Unreleased] - 2021-11-XX

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security
