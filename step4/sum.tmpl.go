// asottile: I needed to template this for PYVERSION
package main

// #cgo pkg-config: PYVERSION
// #include <Python.h>
// int PyArg_ParseTuple_LL(PyObject*, long long*, long long*);
import "C"

//export sum
func sum(self *C.PyObject, args *C.PyObject) *C.PyObject {
	var a C.longlong
	var b C.longlong
	if C.PyArg_ParseTuple_LL(args, &a, &b) == 0 {
		return nil
	}
	return C.PyLong_FromLongLong(a + b)
}

func main() {}
