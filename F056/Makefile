DOC = relatorio

AUX_FILES = $(wildcard *.aux *.log *.bbl *.blg *.out)

all:
	pdflatex $(DOC).tex
	bibtex $(DOC)
	pdflatex $(DOC).tex
	pdflatex $(DOC).tex

clean:
	rm -f $(AUX_FILES)
