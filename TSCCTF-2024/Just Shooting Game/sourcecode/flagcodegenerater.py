import random

data = b'TSC{reV3R53_4md64_45m_w17H_3m0ji_1n_T3H_NeT_5oO0O_c00L}'
data = list(bytearray(data))
order = list(range(len(data)))
random.shuffle(order)

#code = [
#    '}',
#    'printf("%s\\n", data);'
#]

precode = [
    '_start:',
    'section .text',
    'global _start',
    'push rbp',
    'mov rbp, rsp',
    'push rax'
]

postcode = [
    "_check:",
    f"mov rax, [rbp-8]",
    f"xor rbx, rbx",
    "_loop:",
    "mov cl, [rax+rbx*1]",
    "cmp cl, [rsp+rbx*1]",
    "jne _neq",
    "add rbx, 1",
    f"cmp rbx, {len(data)}",
    "jl _loop",
    "mov rax, 1",
    "jmp _end",
    "_neq:",
    "xor rax, rax",
    "_end:",
    "mov rsp, rbp",
    "pop rbp",
    "ret"
#    "mov rax, 1",
#    "mov rdi, 1",
#    "mov rsi, rsp",
#    f"mov rdx, {len(data)}",
#    "syscall",
]

#code = {}
code = []

for i,a in enumerate(order):
    func = random.randint(0, 1)
    fix = random.randint(1, 255)
    xorindex = random.randint(0, len(data)-1)
    while xorindex == a:
        xorindex = random.randint(0, len(data)-1)
    data[a] ^= data[xorindex]
    if func == 1:
        data[a] += fix
    else: 
        data[a] -= fix
    data[a] = (data[a] + 256*4) % 256
    #code[a] = []
    #code[a].append(f'_{a}:')
    code.append(f'mov rcx, [rbp-8]')
    code.append(f'mov al, [rcx+{hex(a)}]')
    code.append(f'mov bl, [rcx+{hex(xorindex)}]')
    code.append(f'xor al, bl')
    code.append(f'{"add" if func == 1 else "sub"} al, {hex(fix)}')
    code.append(f'mov [rcx+{hex(a)}],al')
    #if i < len(order)-1:
    #    code[a].append(f'jmp _{order[i+1]}')
    #else:
    #    code[a].append(f'jmp _check')

dataindex = list(range(0, len(data), 8))
dataindex.reverse()
for a in dataindex:
    tmp = hex(int.from_bytes(bytes(data).ljust(int((len(data)-1)/8+1)*8, b"\0")[a:a+8], byteorder="little", signed=False))
    precode.append(f'mov rax, {tmp}')
    precode.append('push rax')

#precode.append(f'jmp _{order[0]}')

for a in precode:
    print(a)
#for a in range(len(data)):
#    for b in code[a]:
#        print(b)
for a in code:
    print(a)
for a in postcode:
    print(a)
