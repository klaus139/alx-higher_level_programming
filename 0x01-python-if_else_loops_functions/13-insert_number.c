#include "lists.h"

/**
 * insert_node - inserts a number into a sorted sigly linked list
 * @head: pointer to the first element of the list
 * @number: int to the set in the new node
 * Return: address of the new element, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new-> = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
