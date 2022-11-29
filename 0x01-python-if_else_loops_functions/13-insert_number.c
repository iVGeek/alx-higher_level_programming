#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - a function
 * @head: the list head
 * @number: the number
 *
 * Return: adresse or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1, *ptr2, *nouveau;

	nouveau = malloc(sizeof(listint_t));

	if (nouveau == NULL)
		return (NULL);
	nouveau->n = number;

	if (head == NULL)
		return (nouveau);

	ptr1 = *head;
	while ((ptr1->n < number) && ptr1->next != NULL)
	{
		ptr2 = ptr1;
		ptr1 = ptr1->next;
	}

	if (ptr1->next == NULL)
		ptr1->next = nouveau;
	else if (ptr2 == *head)
	{
		if (ptr2->n < nouveau->n)
			ptr2->next = nouveau;
		else
			nouveau->next = ptr2;
	}
	else
	{
		ptr2->next = nouveau;
		nouveau->next = ptr1;
	}

	return (nouveau);
}
