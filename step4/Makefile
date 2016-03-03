SHELL = /bin/bash

.PHONY: all
all: python2.7/venv python2.7/sum.so
all: python3.5/venv python3.5/sum.so

%/venv:
	set -ex; \
	mkdir -p $(dir $@); \
	PYTHON=$$(grep -Eo '^[^/]+' <<< $@); \
	virtualenv $@ -p $$PYTHON

%/sum.c: sum.c
	mkdir -p $(dir $@)
	cp $< $@

%/sum.go: sum.tmpl.go
	set -ex; \
	mkdir -p $(dir $@); \
	PYTHON=$$(grep -Eo '^[^/]+' <<< $@ |sed s/python/python-/); \
	sed s/PYVERSION/$$PYTHON/ $< > $@

%/sum.so: %/sum.go %/sum.c
	cd $(dir $@) && go build -buildmode=c-shared -o $(notdir $@)

.PHONY: clean
clean:
	rm -rf python2.7 python3.5

.SECONDARY:
