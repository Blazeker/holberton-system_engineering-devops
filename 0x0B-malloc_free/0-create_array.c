#include "holberton.h"
#include <stdlib.h>

/**
 * create_array - create an array of n size
 * @size : size of the array
 * @c : A character
 * Return: an array
 */

char *create_array(unsigned int size, char c)
{
	unsigned int i = 0;
	char *s;

	s = malloc(size * sizeof(char));
	if (s == NULL)
		return (NULL);
	if (size == 0)
		return (NULL);
	while (i < size)
	{
		s[i] = c;
		i++;
	}

	return (s);
}
