# Ways to prevent the data buffer overflow in the example:

### 1. **Use `fgets()` Instead of `gets()`**
   - `fgets()` ensures that the input does not exceed the buffer size.
   ```c
   printf("Enter the password: ");
   fgets(input, sizeof(input), stdin);
   input[strcspn(input, "\n")] = 0; // Remove newline character
   ```
   This prevents buffer overflow by limiting the input size to 9 characters (leaving space for `\0`).

### 2. **Use `scanf()` with a Width Limit**
   - `scanf()` can also prevent overflows by specifying a maximum width.
   ```c
   scanf("%9s", input); // Limits input to 9 characters (+1 for null terminator)
   ```
   However, `scanf()` stops at whitespace, so it may not behave as expected for multi-word passwords.

### 3. **Use `strncpy()` Instead of `gets()`**
   ```c
   fgets(input, sizeof(input), stdin);
   input[strcspn(input, "\n")] = 0; // Trim the newline
   ```
   This ensures input doesn't exceed the buffer size.


### **Example Solution**
Combining **`fgets()`** w/ proper comparison:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char input[10];
    char password[10] = "GreyHat123";

    printf("Enter the password: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0; // Remove newline

    if (strcmp(input, password) == 0) {
        printf("Access granted.\n");
    } else {
        printf("Access denied.\n");
    }

    return 0;
}
```

