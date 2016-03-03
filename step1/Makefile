.PHONY: all
all: sum.so

sum.h sum.so: sum.go
	go build -buildmode=c-shared -o sum.so sum.go

.PHONY: clean
clean:
	rm -rf sum.so sum.h
