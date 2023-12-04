#include <stdio.h>
#include <string.h>

// char* add(char value1[], char value2[]);

// char[] mult(char[] value1, char[] value2);

// char[] subs(char[] value1, char[] value2);

char* add(char value1[], char value2[]) {

    int i = 0;

    printf("%s\n", value1);
    printf("%s\n", value2);

    for (i = 0; i < strlen(value1); i++) {
        printf("%c\n", value1[i]);
    } 


    return "";
}

int main () {

    printf("Hello, World!\n");

    static char* value1 = "0101";

    static char* value2 = "0111";

    add(value1, value2);
    
    return 0;
}

