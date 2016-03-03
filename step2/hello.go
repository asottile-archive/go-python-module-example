package main

import "C"

//export AddsHello
func AddsHello(s *C.char) string {
	return "Hello, " + C.GoString(s)
}

func main() {}
