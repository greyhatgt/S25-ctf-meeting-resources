#include <stdio.h>


void win() {
    printf("You win!\n");
}

int main() {

    int len;
    char buf[10];

    setvbuf(stdout, NULL, _IONBF, 0); // Turn off stdout


    printf("How many chars of buf would you like to read?");
    scanf("%d", &len);
    char c; while ((c = getchar()) != '\n' && c != EOF); // Clean up trailing newline

    write(1, buf, len);
    
    printf("\n\nWhat would you like to write to buf?\n\n");
    gets(buf);

}

