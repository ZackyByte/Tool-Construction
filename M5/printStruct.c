#include"printStruct.h"
void printState(char S)
{
    char z = 'z';
    char i = 'i';
    char r = 'r';
    char s = 's';
    if(S == z)
        printf("\tSTATE: Zombie\n");
    if(S == i)
        printf("\tSTATE: Idle\n");
    if(S == r)
        printf("\tSTATE: Running\n");
    if(S == s)
        printf("\tSTATE: Sleeping\n");
}
void printStruct(process myProcess, int childcount, temp myUnion)
{
    char S = myProcess.state;
    printf("This is the fanciest printing you have ever seen\n");
    printf("=====================MYPROCESS===================\n");
    printf("\tNAME: %s\n", myProcess.name);
    printf("\tPID: %d\n", myProcess.pid);
    printf("\tPPID: %d\n", myProcess.ppid);
    printState(S);
    for(int count = 0; count < childcount; count++)
    {
        printf("\t    Child Name: %s\n", myProcess.children[count]);
    }
    printf("=====================MYPROCESS====================\n");
    printf("\n=================== MYUNION ====================\n");
    printf("\tmyUnion: %d %c\n", myUnion.count, myUnion.value);
    printf("\n=================== MYUNION ====================\n");

}