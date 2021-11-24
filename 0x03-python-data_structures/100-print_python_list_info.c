#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
int i, mem;
PyObject *obj;
mem = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
printf("[*] Allocated = %ld\n", mem);
for (i = 0; i < Py_SIZE(p); i++)
{
obj = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
}
}
