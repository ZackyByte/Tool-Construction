#include"printStruct.h"

int main()
{

    process myProc = {10, 30, "Gary", {"test1","test2","test3"}};
    temp t;
    t.count = 0x7A;
    t.value = 0x44;

    printStruct(myProc, 3, t);
    printUnion(t);
}


