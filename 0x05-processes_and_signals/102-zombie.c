#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - do a while lopp infinitely
 * Return: 0
 */


int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Create 5 child process
 * Return: 0
 */

int main(void)
{
	pid_t pid;
	int childs = 0;

	while (childs < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			childs++;
		}
		else
			exit(0);
	}

	infinite_while();
	return (0);
}