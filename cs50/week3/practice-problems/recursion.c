#include <cs50.h>
#include <stdio.h>

void print(int n);

int main(void)
{
    print(5);
    printf("\n");
}

void print(int n)
{
    if (n > 0)
    {
    print(n - 1);
    printf("%i ", n);
    }
    return;
}