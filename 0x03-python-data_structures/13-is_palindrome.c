#include "lists.h"

/**
 * isPalindromeRec - Move right and left using recursion
 * and check for following in each recursive call.
 * @left: node form the left
 * @right: node form the right
 * Return: True or False
 */

int isPalindromeUtil(listint_t **left, listint_t* right) 
{
	int is_palind, is_equal;

	if (right == NULL) 
        	return (1);

	is_palind = isPalindromeUtil(left, right->next); 
	if (is_palind == 0)
		return (0);
	is_equal = (right->n == (*left)->n);
	*left = (*left)->next;
	
	return (is_equal); 
} 

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	return (isPalindromeUtil(head, *head));
}
