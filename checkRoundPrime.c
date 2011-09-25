/*
 * checkRoundPrime.c
 *
 * Copyright 2011 Ershad K ershad92@gmail.com
 * Licensed under GPL Version 3
 * 
 * Code is inefficient, will post a new one soon :) 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 20

int permutations(char *string, int k, int m);
void swap(char *x, char *y);
int checkPrime(int n);
int checkRoundPrime(int n);

int flag = 0;
unsigned long int globalnum;
int main(int argc, char *argv[])
{
    unsigned long int i;
    
    for (i = 0; i < 1000000; i++) 
        if (checkRoundPrime(i))
            printf("%ld\n", i);

    return 0;
}

void swap(char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int permutations(char *string, int k, int m)
{
    int i;
    if (k == m) {
        if(!checkPrime(atol(string)) || (atol(string) < globalnum))
            flag = 1;
    }
    else
        for (i = k; i < m; i++){
            swap(&string[k], &string[i]);
            permutations(string, k+1, m);
            swap(&string[k], &string[i]);
        }
}

int checkPrime(int n)
{
    register int i;
    for (i = 2; i <= (n/2); i++)
        if (n % i == 0)
            return 0;
    return 1;
}

int checkRoundPrime(int n)
{
    char cnumber[MAX];
    sprintf(cnumber, "%d", n);
    flag = 0;
    globalnum = atol(cnumber);
    permutations(cnumber, 0, strlen(cnumber));
    if (flag == 0)
        return 1;
    else
        return 0;            
}
