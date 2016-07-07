HEVEA=hevea

SOURCES=Actors.tex Brokers.tex CommonPitfalls.tex ConfiguringActorApplications.tex Error.tex FAQ.tex FirstSteps.tex GroupCommunication.tex Introduction.tex ManagingGroupsOfWorkers.tex MessageHandlers.tex MessagePassing.tex Messages.tex MigrationGuides.tex NetworkTransparency.tex ReferenceCounting.tex Registry.tex Scheduler.tex UsingAout.tex Utility.tex TypeInspection.tex
RST_FILES=$(SOURCES:.tex=.rst)

# prevent make from building something without target
none:

manual.pdf: $(SOURCES) variables.tex
	pdflatex manual
	pdflatex manual
	pdflatex manual

pdf: manual.pdf

manual.html: $(SOURCES) variables.tex
	hevea -fix manual

html: manual.html

%.rst: %.tex variables.tex explode_lstinputlisting.py filter.py
	cat colors.tex variables.tex newcommands.tex $< | ./explode_lstinputlisting.py | pandoc --filter=./filter.py --wrap=none --listings -f latex -o $@

rst : $(RST_FILES)

sphinx: conf.py rst
	sphinx-build -b html . html

all: pdf html sphinx

clean:
	rm -rf *.htoc *.haux manual.html manual.pdf *.aux *.log $(RST_FILES) html/ _build _static _templates

.PHONY: none all pdf html rst clean

