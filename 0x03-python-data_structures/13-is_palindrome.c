#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - check if a linked list is palindrome or not
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{

listint_t *h, *temp2, *p;
temp2 = *head;
h = *head;
p = *head;
if (*head == NULL)
{
return (1);
}
while (temp2->next != NULL)
{
temp2 = temp2->next;
}
while (h != temp2)
{
if (h->n != temp2->n)
{
return (0);
}
else
{
while (p->next != temp2 && p != temp2)
{
p = p->next;
}
h = h->next;
temp2 = p;
p = h->next;
}
}
return (1);
}
