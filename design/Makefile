# Coq Design Makefile
# Tenet 9: Finetune the compiler, do not polish the code

COQC = coqc
COQFLAGS = -Q . VibeCoder
COQDOC = coqdoc
COQDOCFLAGS = --html --interpolate --utf8

SOURCES = VibeCoder.v
OBJECTS = $(SOURCES:.v=.vo)
HTML_DOCS = $(SOURCES:.v=.html)

.PHONY: all clean verify doc test

all: verify doc

verify: $(OBJECTS)

%.vo: %.v
	$(COQC) $(COQFLAGS) $<

doc: $(HTML_DOCS)

%.html: %.v
	$(COQDOC) $(COQDOCFLAGS) $<

test: verify
	@echo "Running Coq tests..."
	@python ../.github/scripts/verify_coq_properties.py

clean:
	rm -f *.vo *.glob *.aux
	rm -f html/*.html
	rm -f *.html

# Dependency tracking
VibeCoder.vo: VibeCoder.v

# CI integration
ci: verify test
	@echo "✅ Coq CI verification passed"

.PHONY: ci