#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
int i, mem;
PyObject *obj;
mem = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
printf("[*] Allocated = %d\n", mem);
for (i = 0; i < Py_SIZE(p); i++)
{
obj = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(onj)->tp_name);
}
}
