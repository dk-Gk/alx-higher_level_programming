#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in linked list
 * @head: the head of the list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current;
listint_t *temp;
current = *head;
temp = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL)
{
*head = new;
new->next = NULL;
}
else
{
while (current->next != NULL)
{
if (current->n > new->n)
{
if (current == *head)
{
new->next = current;
*head = new;
}
while (temp->next != current)
temp = temp->next;
temp->next = new;
new->next = current;
return (new);
}
current = current->next;
}
current->next = new;
new->next = NULL;
}
return (new);
}
