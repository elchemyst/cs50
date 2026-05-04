#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int n = strlen(argv[1]);
    for (int i = 0; i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    int key = atoi(argv[1]);

    string plaintext = get_string("Plaintext: ");
    int m = strlen(plaintext);
    string ciphertext = plaintext;
    int x = (key / 26) + 1;
    for (int i = 0; i < m; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                ciphertext[i] = plaintext[i] + key;
                if (ciphertext[i] > 90)
                {
                    ciphertext[i] = ciphertext[i] - x * 26;
                }
            }
            if (islower(plaintext[i]))
            {
                ciphertext[i] = plaintext[i] + key;
                if (ciphertext[i] > 122)
                {
                    ciphertext[i] = ciphertext[i] - x * 26;
                }
            }
        }
    }
    printf("Ciphertext: %s\n", ciphertext);
}