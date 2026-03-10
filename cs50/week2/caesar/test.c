#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (int argc, string argv[])
{
    int n = strlen(argv[1]);
    for (int i = 0; i < n; i++)
    {
        printf("%c\n", argv[1][i]);
    }
}