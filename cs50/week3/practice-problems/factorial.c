#include <cs50.h>
#include <stdio.h>

int factorial(int number);

int main(void)
{
    int number = get_int("Enter a number: ");
    factorial(number);
}

void factorial(int number)
{
    factorial(number - 1);

    int factorial;
    factorial = number * (number - 1);
    number--;
}