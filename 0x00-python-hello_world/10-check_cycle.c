#include "lists.h"

/**
 * check_cycle - check if singly linked list is circular
 * @list: pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list->next;
	temp = list;
	while (current && temp && current->next)
	{
		if (current == temp)
		{
			return (1);
		}
		temp = temp->next;
		current = current->next->next;
	}
	return (0);
}
