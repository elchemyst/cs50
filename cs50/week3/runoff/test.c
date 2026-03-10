#include <cs50.h>
#include <stdio.h>

int main (void)
{
    string array[1][2];
    string test = "testing";
    printf("%s\n", test);
    array[0][0] = test;
    printf("%s\n", array[0][0]);
}
