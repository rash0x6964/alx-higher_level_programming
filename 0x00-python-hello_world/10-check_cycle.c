#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: the first element
 * Return: 1 SUCCESS, if not 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
