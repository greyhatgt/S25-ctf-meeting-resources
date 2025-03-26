CC = gcc
CFLAGS = -fno-stack-protector -no-pie

all: outsider-patched

outsider-patched: outsider-patched.c
	$(CC) $(CFLAGS) -o outsider-patched outsider-patched.c

clean:
	rm -f outsider-patched