#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list : the first element
 * Return : 1 SUCCESS, if not 0
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
		return (0);

	tmp = list->next;
	while (tmp)
	{
		if (list == tmp)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
