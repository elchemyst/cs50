#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

#define BITS_IN_A_BYTE 8

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *ptr1 = fopen(argv[1], "r");
    if (ptr1 == NULL)
    {
        printf("Couldn't read WAV file. Aborting now...\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER buffer;
    fread(&buffer, sizeof(BYTE), sizeof(WAVHEADER), ptr1);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(buffer) != 0)
    {
        printf("Cannot verify WAV file format. Aborting now...\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    char *filename = malloc(sizeof(argv[2]));
    sprintf(filename, "%s", argv[2]);
    FILE *ptr2 = fopen(filename, "w");
    if (ptr2 == NULL)
        return 1;

    // Write header to file
    // TODO #6
    fwrite(&buffer, sizeof(BYTE), sizeof(WAVHEADER), ptr2);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(buffer);

    // Write reversed audio to file
    // TODO #8
    BYTE buffer1[block_size];
    if (fseek(ptr1, block_size, SEEK_END) != 0)
        return 2;
    while (ftell(ptr1) - block_size > sizeof(buffer))
    {
        if (fseek(ptr1, -2 * block_size, SEEK_CUR) != 0)
            return 2;
        fread(&buffer1, block_size, 1, ptr1);
        fwrite(&buffer1, block_size, 1, ptr2);
    }

    free(filename);
    fclose(ptr1);
    fclose(ptr2);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 0x57 && header.format[1] == 0x41 && header.format[2] == 0x56 && header.format[3] == 0x45)
    {
        return 0;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int size = header.numChannels * (header.bitsPerSample / BITS_IN_A_BYTE);
    return size;
}


