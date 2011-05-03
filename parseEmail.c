/*
 * parseEmail.c
 *
 * Copyright 2011 Ershad K ershad92@gmail.com
 * Licensed under GPL Version 3
 *
 * Usage: parseEmail [FILE]
 */

#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	int i, k, a, b, x, flag = 0;
    int validateChar(char c);
    
	fp = fopen(argv[1], "r");
	if (fp == NULL) {
		printf(" Usage: parseEmail [FILE]\n Error: File not found (exit 1)\n");
		exit(EXIT_FAILURE);
	}

	while ((read = getline(&line, &len, fp)) != EOF) {
		for (i = 0; i < read; i++) {
		    if (line[i] == '@') {
		    
                if ((validateChar(line[i+1]) != 1) || (validateChar(line[i-1]) != 1))
		            continue; 
               
                flag = 0;		       
                for (b = i+1; validateChar(line[b]) != 0; b++) {
		            if (line[b] == '.') {
	                        flag = 1;
        	            }
		        }
                if (flag == 0) 
		            continue;
		            
                for (a = i-1; validateChar(line[a]) != 0; a--);
		            
                for (x = a+1; x < i; x++)
		            printf("%c", line[x]);
		       
                printf("@");

                for (b = i+1; validateChar(line[b]) != 0; b++)
                    printf("%c", line[b]);

                printf("\n");
            }
	    }     
	
	}

	exit(EXIT_SUCCESS);
}

int validateChar(char c)
{
    /* Add (c == '_') in the end to consider '_' too while extracting */
	if (((c >= 'a') && (c <= 'z')) || ((c >= 'A') && (c <= 'Z')) || 
        ((c >= '0') && (c <= '9')) || (c == '.'))
		return 1;
	else
		return 0;
}
