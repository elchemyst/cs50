#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void convert(int character);
void print_bulb(int bit);

int main(void)
{
    string message = get_string("Enter message: ");
    int n = strlen(message);
    for (int i = 0; i < n; i++)
    {
        convert(message[i]);
        printf("\n");
    }
    // TODO
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

void convert(int character)
{
    int byt[8];
    for (int i = 8; i > 0; i--)
    {
        if (character % 2 == 0)
        byt[i - 1] = 0;

        else if (character % 2 == 1)
        byt[i - 1] = 1;

        character = character / 2;
    }
    for (int i = 0; i < 8; i++)
    {
        print_bulb(byt[i]);
    }
}
