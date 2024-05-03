import pwn
import sys

poppush = ["push", "pop"]
rotate = ["ror", "rol"]
single = ["not", "mul", "div"]
double = ["mov", "add", "sub", "and", "or", "xor"]
addrreg = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp"]
reglist = [["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp"],
           ["eax", "ebx", "ecx", "edx", "esi", "edi", "ebp", "esp"],
           ["ax", "bx", "cx", "dx", "si", "di", "bp", "sp"],
           ["ah", "bh", "ch", "dh"],
           ["al", "bl", "cl", "dl"]]

word = ["qword", "dword", "word", "byte"]

index = 0

with open(sys.argv[1], 'w') as asm:
    with open(sys.argv[2], 'w') as gadget:
        gadget.write('''
mainoffset = 0
gadgetoffset = 0
leaveoffset = 0

def gendict(base, key):
    if key not in base:
        base[key] = {}

def _push(reg):
    result = (gadgetoffset + push_[reg]).to_bytes(8, 'little')
    return result

def _pop(reg, num):
    result = (gadgetoffset + pop_[reg]).to_bytes(8, 'little')
    result += num.to_bytes(8, 'little')
    return result

def _not(reg):
    result = (gadgetoffset + not_[reg]).to_bytes(8, 'little')
    return result

def _mul(reg):
    result = (gadgetoffset + mul_[reg]).to_bytes(8, 'little')
    return result

def _div(reg):
    result = (gadgetoffset + div_[reg]).to_bytes(8, 'little')
    return result

def _ror(reg, num):
    result = _pop('rcx', num)
    result += (gadgetoffset + ror_[reg]).to_bytes(8, 'little')
    return result

def _rol(reg, num):
    result = _pop('rcx', num)
    result += (gadgetoffset + rol_[reg]).to_bytes(8, 'little')
    return result

def _mov(reg1, reg2):
    result = (gadgetoffset + mov_[reg1][reg2]).to_bytes(8, 'little')
    return result

def _add(reg1, reg2):
    result = (gadgetoffset + add_[reg1][reg2]).to_bytes(8, 'little')
    return result

def _sub(reg1, reg2):
    result = (gadgetoffset + sub_[reg1][reg2]).to_bytes(8, 'little')
    return result

def _and(reg1, reg2):
    result = (gadgetoffset + and_[reg1][reg2]).to_bytes(8, 'little')
    return result

def _or(reg1, reg2):
    result = (gadgetoffset + or_[reg1][reg2]).to_bytes(8, 'little')
    return result

def _xor(reg1, reg2):
    result = (gadgetoffset + xor_[reg1][reg2]).to_bytes(8, 'little')
    return result

def leave():
    result = leaveoffset.to_bytes(8, 'little')
    return result

''')
        for a in poppush:
            gadget.write(f'{a}_ = {{}}\n')
            uselen = 0
            for b in addrreg:
                if uselen == 0:
                    uselen = len(pwn.asm(f'{a} {b}\nret', arch='amd64'))
                asm.write(f'"{a} %{b}\\n\\t"\n')
                asm.write('"ret\\n\\t"\n')
                gadget.write(f'{a}_["{b}"] = {hex(index)}\n')
                index += uselen

        for a in rotate:
            gadget.write(f'{a}_ = {{}}\n')
            for reg in reglist:
                uselen = 0
                for b in reg:
                    if uselen == 0:
                        uselen = len(pwn.asm(f'{a} {b}, cl\nret', arch='amd64'))
                    asm.write(f'"{a} %cl, %{b}\\n\\t"\n')
                    asm.write('"ret\\n\\t"\n')
                    gadget.write(f'{a}_["{b}"] = {hex(index)}\n')
                    index += uselen

        for a in single:
            gadget.write(f'{a}_ = {{}}\n')
            for reg in reglist:
                uselen = 0
                for b in reg:
                    if uselen == 0:
                        uselen = len(pwn.asm(f'{a} {b}\nret', arch='amd64'))
                    asm.write(f'"{a} %{b}\\n\\t"\n')
                    asm.write('"ret\\n\\t"\n')
                    gadget.write(f'{a}_["{b}"] = {hex(index)}\n')
                    index += uselen

        for a in double:
            gadget.write(f'{a}_ = {{}}\n')
            for reg in reglist:
                uselen = 0
                for b in reg:
                    gadget.write(f'gendict({a}_, "{b}")\n')
                    for c in reg:
                        if b != c:
                            if uselen == 0:
                                uselen = len(pwn.asm(f'{a} {b}, {c}\nret', arch='amd64'))
                            asm.write(f'"{a} %{c}, %{b}\\n\\t"\n')
                            asm.write('"ret\\n\\t"\n')
                            gadget.write(f'{a}_["{b}"]["{c}"] = {hex(index)}\n')
                            index += uselen
                    for idx, c in enumerate(addrreg):
                        gadget.write(f'gendict({a}_, "addr{c}")\n')
                        if uselen == 0:
                            uselen = len(pwn.asm(f'{a} {word[idx]} ptr [{c}], {b}\nret', arch='amd64'))
                            if c in ['rbp', 'rsp']:
                                uselen -= 1
                        asm.write(f'"{a} %{b}, (%{c})\\n\\t"\n')
                        asm.write('"ret\\n\\t"\n')
                        gadget.write(f'{a}_["addr{c}"]["{b}"] = {hex(index)}\n')
                        index += uselen
                        if c in ['rbp', 'rsp']:
                            index += 1
                        asm.write(f'"{a} (%{c}), %{b}\\n\\t"\n')
                        asm.write('"ret\\n\\t"\n')
                        gadget.write(f'{a}_["{b}"]["addr{c}"] = {hex(index)}\n')
                        index += uselen
                        if c in ['rbp', 'rsp']:
                            index += 1
