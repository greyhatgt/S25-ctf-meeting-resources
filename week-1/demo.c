#include <stdio.h>  // Include the standard input/output library
#include <string.h> // Include the string manipulation library

int main() {
    // Declare a buffer to store the user input
    char inputBuffer[32];
    // Declare and initialize the correct password
    char password[] = "supersneaky";
    // Set the number of attempts the user has to guess the password
    int attempts = 3;

    // Loop through the number of attempts
    for (int i = 0; i < attempts; i++) {
        // Prompt the user to enter the password
        printf("Attempt %d: Enter the password: ", i + 1);

        // Use fgets to read user input
        if (fgets(inputBuffer, sizeof(inputBuffer), stdin) != NULL) {
            // Remove the trailing newline character, if present
            size_t length = strlen(inputBuffer);
            if (length > 0 && inputBuffer[length - 1] == '\n') {
                inputBuffer[length - 1] = '\0';
            }

            // Compare the user input to the correct password
            if (strcmp(inputBuffer, password) == 0) {
                // If the input matches the password, print success message
                printf("You guessed the password!\n");
                // Exit the program with a success status
                return 0;
            } else {
                // If the input does not match, print failure message
                printf("You did not guess the password :(\n");
            }
        } else {
            // If fgets encounters an error, notify the user
            printf("Error reading input. Please try again.\n");
        }
    }

    // If all attempts are used, print a message indicating failure
    printf("Sorry, you've used all attempts.\n");
    // Exit the program with a success status
    return 0;
}
