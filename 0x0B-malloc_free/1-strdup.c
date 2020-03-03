#include "holberton.h"
#include <stdlib.h>

/**
 * _strdup - Duplicate a string
 * @str : an array
 * Return: 0
 */



char *_strdup(char *str)
{
	int i = 0;
	char *s;

	if (str == NULL)
	{
		return (NULL);
	}
	for (i = 0; str[i] != '\0'; i++)
	{
	}
	s = malloc(i * sizeof(char));
	if (s == NULL)
		return (NULL);
	i = 0;

	while (str[i] != '\0')
	{
		s[i] = str[i];
		i++;
	}

	return (s);
}
