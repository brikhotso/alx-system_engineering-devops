#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Function that runs an infinite loop
 *
 * Return: Always returns 0
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
 * main - Entry point of the program
 *
 * Return: Always returns 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();

		if (child_pid == -1)
		{
			perror("Fork error");
			exit(EXIT_FAILURE);
		}

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
		else
		{
			sleep(1);
		}
	}

	infinite_while();
	return (0);
}
