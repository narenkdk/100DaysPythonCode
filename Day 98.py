#Day 98: C API


#Study Python's C API and extension modules.

#This script defines a simple Python C extension that adds two numbers:

#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Function: Adds two integers
static PyObject* add(PyObject* self, PyObject* args) {
    int x, y;
    
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;
    }

    return PyLong_FromLong(x + y);
}

// Method definitions
static PyMethodDef MyMethods[] = {
    {"add", add, METH_VARARGS, "Adds two numbers"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef myextension = {
    PyModuleDef_HEAD_INIT,
    "myextension",
    "A simple Python C extension",
    -1,
    MyMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_myextension(void) {
    return PyModule_Create(&myextension);
}



#Use this script to compile and install the module:
from setuptools import setup, Extension

module = Extension("myextension", sources=["myextension.c"])

setup(
    name="myextension",
    version="1.0",
    description="A simple Python C extension",
    ext_modules=[module]
)


#How to Compile & Test
#Build and install the module

python setup.py build
python setup.py install


#Test in Python

import myextension
print(myextension.add(10, 20))  # Output: 30


