#include<stdio.h>

typedef struct{
    int ppid;
    int pid;
    char name[30];
    char children[10][30];
}process;

typedef union
{
    int count;
    char value;
}temp;

int main()
{
    process myproc = {10, 30, "gary", {"test1", "test2", "test3"}};
    temp t;
    t.value = 0x44;
    t.count = 0x7A;

    printf("%d %c\n", t.count, t.value);
    printf("%d %d %s\n", myproc.ppid, myproc.pid, myproc.name);

    for(int count = 0; count < 3; count++)
    {
        printf("%s ", myproc.children[count]);
    }
}

