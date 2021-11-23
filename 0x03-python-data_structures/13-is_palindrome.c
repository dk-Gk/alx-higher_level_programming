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

listint_t *temp2;
temp2 = *head;
int arr[9999];
int i = 0, count = 0, j;
if ((!*head) || (!head))
{
return (1);
}
if (!temp2->next)
{
return (1);
}

while (temp2->next != NULL)
{
arr[i] = temp2->n;
temp2 = temp2->next;
i++;
count++;
}
arr[i] = temp2->n;
count++;
j = count - 1;
for (i = 0; i < count; i++)
{
if (arr[i] != arr[j])
{
return (0);
}
j--;
}
return (1);
}
