#include <stdio.h>
#include <string.h>

int main() {
    char input[10];
    char password[10] = "GreyHat123";

    printf("Enter the password: ");
    gets(input);

    printf("Input: %s\n", input);
    printf("Password: %s\n", password);

    if (strncmp(input, password, 10) == 0) {
        printf("Access granted.\n");
    } else {
        printf("Access denied.\n");
    }

    return 0;
}
