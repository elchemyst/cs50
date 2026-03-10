#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
   string lowercase = get_string("Enter string: ");
   int n = strlen(lowercase);
   for (int i = 1; i < n - 1; i++)
   {
        if (lowercase[i] > lowercase[i+1])
        {
            printf("Not in order\n");
            return 0;
        }
   }
   printf("In order\n");
   return 0;
}