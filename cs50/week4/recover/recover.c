#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512
typedef uint8_t byte;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover <file name>\n");
        return 1;
    }

    // opening read file
    FILE *ptr1 = fopen(argv[1], "r");
    if (ptr1 == NULL)
    {
        printf("Couldn't open file! Aborting now...\n");
        return 1;
    }

    byte buffer[BLOCK_SIZE];

    // opening write file
    FILE *ptr2 = NULL;
    char *filename = malloc(8 * sizeof(char));
    int image_count = 0;

    while (fread(&buffer, 1, BLOCK_SIZE, ptr1) == BLOCK_SIZE)
    {
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xe0) == 0xe0))
        {
            sprintf(filename, "%03i.jpg", image_count);
            ptr2 = fopen(filename, "w");
            if (ptr2 == NULL)
                return 1;
            image_count++;
        }
        if (ptr2 != NULL)
        {
            fwrite(&buffer, 1, BLOCK_SIZE, ptr2);
        }
    }

    free(filename);
    fclose(ptr1);
    fclose(ptr2);
}
