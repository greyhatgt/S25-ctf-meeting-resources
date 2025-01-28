#include <stdio.h>

int main() {
    // set up a variable to store the user input
    char inputBuffer[32];
    char password[] = "super sneaky";

    // read the user input to the variable
    scanf("%s", inputBuffer);

    // print the user input to the console
    printf("You entered: %s\n", inputBuffer);

    // Prints Hello World to the console
    printf("Hello world\n");
}
