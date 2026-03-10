#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a number: ");
    printf("%i\n", convert(input));
}

int convert(string input)
{
    int n = strlen(input);
    if (n == 1)
        return input[0] - '0';

    int converted_last_digit = input[n - 1] - '0';
    input[n - 1] = '\0';

    return converted_last_digit + 10 * convert(input);
}