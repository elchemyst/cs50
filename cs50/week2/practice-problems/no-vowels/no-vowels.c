// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

void replace(string input);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Enter 1 argument\n");
        return 1;
    }

    replace(argv[1]);
}

void replace(string input)
{
    int n = strlen(input);
    for (int i = 0; i < n; i++)
    {
        switch (input[i])
        {
            case 'a':
                input[i] = '6';
                break;
            case 'e':
                input[i] = '3';
                break;
            case 'i':
                input[i] -= 56;
                break;
            case 'o':
                input[i] -= 63;
                break;
            default:
                input[i] = input[i];
                break;
        }
        printf("%c", input[i]);
    }
    printf("\n");
}
