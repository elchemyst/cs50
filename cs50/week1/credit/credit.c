#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool checksum(const string number, int length);

int main(void)
{
    string number = get_string("Enter card number: ");
    int length = strlen(number);
    if (checksum(number, length) == false)
        printf("INVALID\n");
    if (length == 15)
        printf("AMEX\n");
    if (length == 13)
        printf("MASTERCARD\n");
    if (length == 16)
        printf("VISA\n");

}

bool checksum(const string number, int length)
{
    long num = atoi(number);
    int arr[length];
    int i = 0;
    int ops = 1;
    while (num != 0)
    {
        arr[i] = num % 10;
        num = num / 10;
        i++;
    }
    for (int j = 0; j < length / 2; j++)
    {
        int temp = 0;
        temp = arr[length - j];
        arr[length - j] = arr[j];
        arr[j] = temp;
    }
    for (int j = 0; j < length; j++)
    {
        printf("%i", arr[j]);
    }
    for (int j = length - 2; j > 0; j -= 2)
    {
        if (j == 1)
            break;
        ops = ops * arr[j];
    }
    for (int j = length - 1; j > 0; j -= 2)
    {
        if (j == 1)
            break;
        ops = ops + arr[j];
    }
    if (ops % 10 == 0)
        return true;
    return false;
}
