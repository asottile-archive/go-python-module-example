// asottile: this has to be named main?
package main

import "C"

// asottile:
// The comment below is necessary for "exporting" a function to C
// comments as code +-
// Also it cannot be "// export Sum". yay.

//export Sum
func Sum(a, b int) int {
	return a + b
}

// asottile: this is required otherwise you get an error
// go build -buildmode=c-shared -o sum.so sum.go
// # command-line-arguments
// runtime.main: call to external function main.main
// runtime.main: main.main: not defined
func main() {}
