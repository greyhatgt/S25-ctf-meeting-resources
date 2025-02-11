#include <stdio.h>
#include <string.h>

#define PASSWORD "GreyHat123"

int main() {
    char input[50];

    printf("Enter the password: ");
    scanf("%49s", input);

    if (strcmp(input, PASSWORD) == 0) {
        printf("Access granted.\n");
    } else {
        printf("Access denied.\n");
    }

    return 0;
}
