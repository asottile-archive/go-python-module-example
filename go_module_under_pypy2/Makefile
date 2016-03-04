.PHONY: all
all: make-pypy-so

.PHONY:
make-pypy-so: sum.so
	cp sum.so sum.pypy-$$(pypy -c 'import sys; print("".join(str(x) for x in sys.pypy_version_info[:2]))').so

sum.so: libgo-sum.so sum.o
	gcc -shared sum.o -L./ -lgo-sum -o $@

sum.o: sum.c libgo-sum.h
	gcc -fPIC -c sum.c -o sum.o -I./ -I$$(pypy -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())')

libgo-sum.h libgo-sum.so: libgo-sum.go
	go build -buildmode=c-shared -o libgo-sum.so libgo-sum.go

.PHONY: clean
clean:
	rm -f sum.o libgo-sum.h *.so
