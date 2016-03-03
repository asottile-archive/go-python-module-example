.PHONY: all
all: hello

hello.h hello.a: hello.go
	go build -buildmode=c-archive -o hello.a hello.go

hello: hello.a hello.h hello.c
	# asottile: needed -lpthread to link against go generated .a
	gcc -Wall -o hello hello.c ./hello.a -lpthread

.PHONY: clean
clean:
	rm -rf hello.a hello.h
