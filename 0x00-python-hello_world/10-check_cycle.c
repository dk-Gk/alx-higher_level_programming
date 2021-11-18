#include "lists.h"

/**
 * check_cycle - check if singly linked list is circular
 * @list: pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current->next)
	{
		if (current->next == list)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
