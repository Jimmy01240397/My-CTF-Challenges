import sys

#magic = 0x000000e4
magic = int(sys.argv[2])
start = 0x0001F600

def trans(a):
    a = int(a)
    a += start
    a = a ^ magic
    if a >= 0x1f650:
        a += 48
    if a >= 0x1f6c6:
        a += 5
    if a >= 0x1f6d3:
        a += 2
    if a >= 0x1f6d8:
        a += 5
    if a >= 0x1f6ed:
        a += 3
    if a >= 0x1f6fd:
        a += 3
    return (a).to_bytes(4, byteorder='little', signed=False).decode('utf32')


with open(sys.argv[1], 'rb') as f:
    data = f.read()

result = ''

for a in data:
    result += trans(a)
print(result)
