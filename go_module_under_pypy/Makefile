SHELL = /bin/bash

.PHONY: all
all: make-pypy-so

.PHONY: make-pypy-so
make-pypy-so: sum.so
	cp sum.so sum.pypy-$$(pypy -c 'import sys; print("".join(str(x) for x in sys.pypy_version_info[:2]))').so

sum.so: build/sum.so
	cp build/sum.so ./

build:
	mkdir -p build

build/sum.c: sum.c build
	cp $< $@

build/sum.go: sum.tmpl.go build
	sed s/PYVERSION/pypy/ $< > $@

build/pypy.pc: make-pypy-pc.py build
	./make-pypy-pc.py $@

build/sum.so: build/sum.c build/sum.go build/pypy.pc
	cd build && PKG_CONFIG_PATH=. go build -buildmode=c-shared -o $(notdir $@)

.PHONY: clean
clean:
	rm -rf sum.so build

.SECONDARY:
