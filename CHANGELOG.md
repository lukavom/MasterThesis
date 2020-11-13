# Changelog
All notable changes to the University of Bonn thesis style are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

Changes are sorted into the following categories:
Added, Changed, Deprecated, Removed, Fixed, Security.

## [Unreleased] - 2020-11-13
### Added
- Add some instructions for Fedora 33.
### Changed
- Latest version of `PyFeynHand` scripts.
- `backref`, `maxbibnames` and `block` options actually work and should be passed to `ubonn-biblatex.sty`.
- Shuffle instructions on compiling guide.

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
