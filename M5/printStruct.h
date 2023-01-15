#ifndef STRUCTPRINT_H
#define STRUCTPRINT_H

#include<stdio.h>



typedef struct{
    int ppid;
    int pid;
    char name[30];
    char children[10][30];
    char state;
}process;

typedef union
{
    int count;
    char value;
}temp;

void printStruct(process myProcess, int childcount, temp myUnion);
void printUnion(temp myUnion);

#endif