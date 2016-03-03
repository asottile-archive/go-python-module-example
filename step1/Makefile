.PHONY: all
all: main

sum.h sum.so: sum.go
	go build -buildmode=c-shared -o sum.so sum.go

main: sum.so sum.h main.c
	gcc -Wall -o main main.c ./sum.so

.PHONY: clean
clean:
	rm -rf sum.so sum.h
