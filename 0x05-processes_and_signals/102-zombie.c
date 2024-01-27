#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - a program that creates 5 zombie processes.
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	pid_t i, pid;

	for (i = 0; i < 5; ++i)
	{
		pid = fork();
		if (pid == 0)
			return (0);

		printf("Zombie process created, PID: %d\n", pid);
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - a function that loops forever.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
