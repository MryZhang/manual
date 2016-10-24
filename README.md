# CAF Manual

This repository contains the LaTeX sources for the CAF user manual. To build
the manual, first check out the main repository and then this repository as sub
directory:

```
git clone https://github.com/actor-framework/actor-framework.git
cd actor-framework
git clone https://github.com/actor-framework/manual.git
./configure
cd manual
# build individual targets:
make pdf
make html
make sphinx
# build all three targets:
make all
```

The `pdf` target creates the file `manual.pdf` using `pdflatex`.

The single-page HTML version for the `html` target requires
[HeVeA](http://hevea.inria.fr).

The multi-page [Read the Docs](https://readthedocs.org) HTML version for the
`sphinx` target requires Python, Pandoc, the pandocfilters Python module, and Sphinx.
