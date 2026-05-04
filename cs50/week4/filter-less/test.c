#include <stdio.h>

int main(void)
{
    int arr[1];
    int arri[1];
    arr[0] = 1;
    arri[0] = 2;
    printf("%i\n", arr[0]);
    printf("%i\n", arri[0]);
    arr[1] = arri[1];
    printf("%i\n", arr[0]);
}
