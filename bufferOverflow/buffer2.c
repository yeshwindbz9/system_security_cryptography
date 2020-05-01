#include<stdio.h>
void main()
{
	char *name;
	char *command;

    name = (char*)malloc(5);
    command = (char*)malloc(5);

    printf("Address of name = %d\n",name);
    printf("Address of command = %d\n",command);
    printf("Difference is %d characters\n",command - name);
	printf("Enter your Name : ");
	gets(name);
	system(command);
}