#include <Python.h>

static PyObject* sum(PyObject* self, PyObject* args) {
    long long a;
    long long b;
    if (!PyArg_ParseTuple(args, "LL", &a, &b)) {
        return NULL;
    }

    return PyLong_FromLongLong(a + b);
}

static struct PyMethodDef methods[] = {
    {"sum", (PyCFunction)sum, METH_VARARGS},
    {NULL, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "sum",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_sum(void) {
    return PyModule_Create(&module);
}
#else
PyMODINIT_FUNC initsum(void) {
    Py_InitModule3("sum", methods, NULL);
}
#endif
