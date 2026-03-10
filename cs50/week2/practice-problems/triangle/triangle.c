#include <cs50.h>
#include <stdio.h>

bool check (float a, float b, float c);
int main (void)
{
    float a, b, c;
    printf("Enter 3 sides of triangle\n");
    a = get_float("");
    b = get_float("");
    c = get_float("");
    printf("%s\n", check(a, b, c));
}

bool check (float a, float b, float c)
{
    if ((a + b > c) && (a + c > b) && (b + c > a) && a > 0 && b > 0 && c > 0)
    {
       // printf("true\n");
       return true;
    }
    else
    {
      //  printf("false\n");
      return false;
    }
}