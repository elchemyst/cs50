#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Enter start size: ");
    }
    while (start_size < 9);

    // Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("Enter end size: ");
    }
    while (end_size < start_size);
    // Calculate number of years until we reach threshold
    int years = 0;
    int n = start_size;

    // if else returns 0 if end and start size is 0
    if (start_size == end_size)
    {
        printf("Years: 0");
    }

    // do while loops runs to calculate population
    // uses formula from question where n is start population
    // adds year by one untill n >= end population size
    do
    {
        n = round(n + (n / 3) - (n / 4));
        years++;
    }
    while (n < end_size);
    printf("Years: %i", years);
}