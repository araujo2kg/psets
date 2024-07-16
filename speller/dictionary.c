// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

unsigned int dict_size = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
const unsigned int N = 65537;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Get the index
    unsigned int hashcode = hash(word);
    // If hashtable index is empty
    if (table[hashcode] == NULL)
    {
        return false;
    }
    // Traverse linked list looking for a match
    else
    {
        node *trav = table[hashcode];
        while (trav != NULL)
        {
            if (strcasecmp(trav->word, word) == 0)
            {
                return true;
            }
            trav = trav->next;
        }
        return false;
    }
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int ascii_sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        ascii_sum += (1 << i) * tolower(word[i]);
    }
    return ascii_sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Initialize the hashtable to null
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    // Open source dict
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    char w[LENGTH + 1];
    // Read each word in dict
    while (fscanf(dict, "%s", w) != EOF)
    {
        // Get the word hashcode
        unsigned int hashcode = hash(w);
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }
        // Add word to the node
        strcpy(new_node->word, w);
        new_node->next = NULL;

        // If hashtable index is empty
        if (table[hashcode] == NULL)
        {
            table[hashcode] = new_node;
        }
        // If index already contain a node
        else
        {
            new_node->next = table[hashcode];
            table[hashcode] = new_node;
        }
        dict_size++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Traverse the hashtable indexes
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            while (table[i] != NULL)
            {
                node *tmp = table[i];
                table[i] = table[i]->next;
                free(tmp);
            }
        }
    }
    return true;
}
