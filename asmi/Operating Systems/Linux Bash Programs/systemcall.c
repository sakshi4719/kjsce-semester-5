#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
void main()
{
	pid_t process_id;

	printf("pid of main program:\t%d\n", getpid());
	process_id = fork();

	if(process_id == 0)
	{
		printf("\nIn child process,\npid:\t%d,\nppid:\t%d\n", getpid(), getppid());
		FILE *file_ptr;
        	file_ptr = fopen("file1.txt", "r");
        	if (file_ptr == NULL)
        	{
            		printf("Cannot open given file \n");
            		exit(0);
        	}	
        	printf("\nContents of file:\n");
        	char ch = fgetc(file_ptr);
        	while (ch != EOF)
        	{
            		printf("%c", ch);
            		ch = fgetc(file_ptr);
        	}
        	fclose(file_ptr);
	}
	else
	{
		printf("\nIn parent,\npid:\t\t%d,\nfork returned:\t%d\n", getpid(), process_id);
	}
}
