#include <stdio.h>
#include <string.h>
#include <cs50.h>

int adjacentElementsProduct(int inputArray[], size_t input_size);

char *to_jaden_case (char *jaden_case, const char *string);

int main(void)
{
  int inputArray[9] = {-23, 4, -5, 99, -27, 329, -2, 7, -921};
  int inputsize = 9;
  printf("%i\n", adjacentElementsProduct(inputArray, 9));
}

int adjacentElementsProduct(int inputArray[], size_t input_size)
{
  int max = 0;
  for (int i = 0; i < input_size - 1; i ++)
  {
    if (inputArray[i] * inputArray[i + 1] > max)
      max = inputArray[i] * inputArray[i + 1];
  }
  return max;
}
