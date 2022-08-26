#include <python.h>

/**
 * print_python_list_info - prints some basic info about python lists.
 * @p: python object
 */
void print_python_list_info(pyObject *p)
{
	pyObject *obj;
	pyListObject *list_obj;
	int list_size, i = 0;
	list_size = pyList_Size(p);
	list_obj = (pyListObject *p)p;
	printf("[*] size of the python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", (int)(list_obj->allocated));

	while (i < list_size)
	{
		obj = pyList_GetItem(p. i);
		printf("Element %d: %s\n", i, py_TYPE(obj)->ty_name);
		i++;
	}
}
