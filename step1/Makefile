.PHONY: all
all: sum

sum.h sum.so: sum.go
	go build -buildmode=c-shared -o sum.so sum.go

sum: sum.so sum.h sum.c
	gcc -Wall -o sum sum.c ./sum.so

.PHONY: clean
clean:
	rm -rf sum.so sum.h
