#include<stdio.h>

float Divide(float a, int b)
{
    float result;
    result = a / b;
    printf("result in function is %f", result);
    printf("\nthe float is in the function");
    return result;
}
int main()
{
    float a = 33.4;
    int b= 5;
    float result = Divide(a,b);
    
    printf("\nresult is %f", result);
    printf("\nint was returned as int to main because the parameters are type int");
}