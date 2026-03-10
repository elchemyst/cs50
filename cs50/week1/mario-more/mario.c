#include <cs50.h>
#include <stdio.h>

int main(void)
{
int n = 0;
// loop to take input from 1 to 8
do
{
    n = get_int ("Enter height of pyramid: ");
}while (n < 1 || n > 8);

for (int i = 1; i <= n; i++)
{
    for (int j = 1; j <= n+2+i; j++)
    {
        if (j <= n-i)
        {
            printf (" ");
        }
        else if (j > n-i && j < n+1)
        {
            printf ("#");
        }
        else if (j > n+2)
        {
            printf ("#");
        }
        else
        {
            printf (" ");
        }
    }
    printf("\n");
}

}