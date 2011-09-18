/*
 * anagramSolver.c
 *
 * Copyright 2011 Ershad K <ershad92@gmail.com>
 * Licensed under GPL Version 3
 *
 * Usage: anagramSolver <word>
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 50

void permutations(char *string, int k, int m);
void swap(char *x, char *y);
void openFile();

FILE *fp;
char *line = NULL;
size_t len = 0;
ssize_t read;
int j, flag;
unsigned int locations[26][2];

int main(int argc, char *argv[])
{
    char string[MAX];

    if (argc != 2) {
        printf ("Usage: anagramSolver <word>\n");
        return 1;
    }
    
    openFile();
    
    /* Creating index of the word list for fast access */
    int k = 0;
    unsigned int l = 0;
    char first, old = '$';
    while ((read = getline(&line, &len, fp)) != EOF) {
        l++;
        first = line[0];
        if (first != old) {
            if (line[0] < 'a')
                continue;
            locations[line[0] - 'a'][0] = line[0];
            locations[line[0] - 'a'][1] = ftell(fp);
            k++;
        }
        old = first;
    }
    
    permutations(argv[1], 0, strlen(argv[1]));
    return 0;
}

void swap(char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void permutations(char *string, int k, int m)
{
    int i;
    if (k == m) {
        fseek(fp, line[string[0] - 'a'], SEEK_SET);
        while ((read = getline(&line, &len, fp)) != EOF) {
            flag = 0;
            for (j = 0; line[j] != '\n'; j++) {
                if (line[j] != string[j])
                    flag = 1;
            }
            if (flag == 0 && strlen(string) == j)
                printf("%s", line);
        }
    }
    else
        for (i = k; i < m; i++){
            swap(&string[k], &string[i]);
            permutations(string, k+1, m);
            swap(&string[k], &string[i]);
        }
}

void openFile()
{
    char *fileList[] = {"wordlist",
                       "/usr/share/dict/american-english",
                       "/usr/share/dict/british-english",
                       "/usr/share/dict/cracklib-small"};
    int f;
    for (f = 0; f < 4; f++)
        {
            fp = fopen(fileList[f],"r");
            if (fp != NULL) 
                break;
        }
    
    if (fp == NULL) {
        printf("\n Error: Cannot open dictionary file");
        exit(1);
    }
}
