#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    float l = count_letters(text);
    float w = count_words(text);
    float s = count_sentences(text);

    // Letters per 100 words
    float L = (l / w) * 100;

    // Sentences per 100 words
    float S = (s / w) * 100;

    // Coleman-Liau Index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", index);
    }
}

int count_letters(string text)
{
    int n = strlen(text);
    int l = 0;
    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]))
        {
            l += 1;
        }
    }
    return l;
}

int count_words(string text)
{
    int n = strlen(text);
    int w = 0;
    if (n == 0)
    {
        return 0;
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            if (isblank(text[i]))
            {
                w += 1;
            }
        }
    }
    return w + 1;
}

int count_sentences(string text)
{
    int n = strlen(text);
    int s = 0;
    for (int i = 0; i < n; i++)
    {
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            s += 1;
        }
    }
    return s;
}
