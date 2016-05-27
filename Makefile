HEVEA=hevea
VERSION=$(shell grep "\#define CAF_VERSION " ../libcaf_core/caf/config.hpp | awk '{ full=$$3; major=full/10000; minor=(full/100)%100; patch=full%100; printf("%d.%d.%d", int(major), int(minor), int(patch)) }')

variables.tex : variables.tex.in
	sed 's/@CAF_VERSION@/$(VERSION)/g' variables.tex.in > variables.tex

pdf : variables.tex
	pdflatex manual
	pdflatex manual
	pdflatex manual

html : variables.tex
	hevea -fix manual

clean:
	rm -f *.htoc *.haux *.html *.aux *.log variables.tex

.PHONY: clean
