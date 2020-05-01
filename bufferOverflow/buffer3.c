#include<stdio.h>
void main()
{
    char *password;
	char *isValidUser;
    int flag;

    password = (char*)malloc(5);
    isValidUser = (char*)malloc(1);
    *isValidUser = NULL;

    printf("Address of password = %d\n",password);
    printf("Address of is isValidUser = %d\n",isValidUser);
    printf("Difference is %d characters\n",isValidUser - password);
	printf("Enter Password : ");
	gets(password);
    int x = strcmp(password,"xavier");
    if(x == 0){
        printf("Correct password\n");
        *isValidUser = &flag;
    }
    else{
        printf("Wrong password\n");
    }
    if(*isValidUser){
        printf("Root privilages are assigned\n");
    }
    else{
        printf("Root privilages are not assigned\n");
    }
}