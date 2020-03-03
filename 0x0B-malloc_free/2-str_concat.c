#include "holberton.h"
#include <stdlib.h>

/**
 * str_concat - concat 2 strings
 * @s1 : an array
 * @s2 : an array
 * Return: an array
 */

char *str_concat(char *s1, char *s2)
{
	int i = 0, j = 0, cont = 0;
	char *s;

	if (s1 == NULL && s2 == NULL)
	{
		return (NULL);
	}

	for (i = 0; s1[i] != '\0'; i++)
	{
	}

	for (j = 0; s2[j] != '\0'; j++)
	{
	}

	cont = i + j;
	s = malloc(cont * sizeof(char));
	if (s == NULL)
		return (NULL);
	i = 0;
	while (s1[i] != '\0')
	{
		s[i] = s1[i];
		i++;
	}

	j = 0;

	while (s2[j] != '\0')
	{
		s[i + j] = s2[j];
		j++;
	}
	return (s);
}
