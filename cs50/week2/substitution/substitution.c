#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{

    //Invalid key errors
    if (argc != 2)
    {
        printf("./substitution key\n");
        return 1;
    }
    int n = strlen(argv[1]);
    if (n != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        char a = argv[1][i];
        if (!isalpha(argv[1][i]))
        {
            printf("Key must have aplphabets only\n");
            return 1;
        }
    }
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("Each character must be unique\n");
                return 1;
            }
            else if ((argv[1][i] == argv[1][j] + 32) || (argv[1][i] == argv[1][j] - 32))
            {
                printf("Each character must be unique\n");
                return 1;
            }
        }
    }

    //post valid key injection
    string key = argv[1];
    string plaintext = get_string("plaintext: ");
    string ciphertext = plaintext;
    for (int i = 0; i < n; i++)
    {
        if (isupper(plaintext[i]))
        {
            ciphertext[i] = key[plaintext[i] - 65];
            ciphertext[i] = toupper(ciphertext[i]);
        }
        if (islower(plaintext[i]))
        {
            ciphertext[i] = key[plaintext[i] - 97];
            ciphertext[i] = tolower(ciphertext[i]);
        }
    }
    printf("ciphertext: %s\n", ciphertext);

    //make the errors abstract (make custom function )
}