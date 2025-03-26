#include <inttypes.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void win() {
    execl("/bin/sh", "sh", NULL);
}

int main() {
    char want[16];
    uint64_t money = 10;

    setbuf(stdout, NULL);

    printf("Welcome to the Duty-Free Shop!\n\n"
           "What would you like to buy? ");

    gets(want);

    // if (strcmp(want, "shell") == 0) {
    //     if (money == 0xdeadbeef13371337) {
    //         win();
    //     } else {
    //         printf("Sorry, you don't have the right amount "
    //                "of money to buy that.\n");
    //     }
    // } else {
    printf("Sorry, we don't have any %s.\n", want);
    // }
}
