// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
// Declaring variables
unsigned int hash_value = 0;
unsigned int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int h = hash(word);
    node *chk = table[h];
    while (chk != NULL)
    {
        if (strcasecmp(chk->word, word) == 0)
        {
            return true;
        }
        chk = chk->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long total = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        total += toupper(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
        return false;

    // Read each word in the file
    char word[LENGTH + 1];
    while (fscanf(source, "%s", word) != EOF)
    {
        node *new = malloc(sizeof(node));
        if (new == NULL)
            return false;
        strcpy(new->word, word);
        // potential error: remove next line
        new->next = NULL;

        // Add each word to the hash table
        hash_value = hash(word);
        word_count++;

        // merge linked-list to table (when NULL)
        if (table[hash_value] == NULL)
        {
            new->next = NULL;
            table[hash_value] = new;
        }
        // merge linked-list to table (when already active)
        if (table[hash_value] != NULL)
        {
            new->next = table[hash_value];
            table[hash_value] = new;
        }
    }
    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
        if (cursor == NULL)
            return true;
    }
    return false;
}
