
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

push_ = {}
push_["rax"] = 0x0
push_["rbx"] = 0x2
push_["rcx"] = 0x4
push_["rdx"] = 0x6
push_["rsi"] = 0x8
push_["rdi"] = 0xa
push_["rbp"] = 0xc
push_["rsp"] = 0xe
pop_ = {}
pop_["rax"] = 0x10
pop_["rbx"] = 0x12
pop_["rcx"] = 0x14
pop_["rdx"] = 0x16
pop_["rsi"] = 0x18
pop_["rdi"] = 0x1a
pop_["rbp"] = 0x1c
pop_["rsp"] = 0x1e
ror_ = {}
ror_["rax"] = 0x20
ror_["rbx"] = 0x24
ror_["rcx"] = 0x28
ror_["rdx"] = 0x2c
ror_["rsi"] = 0x30
ror_["rdi"] = 0x34
ror_["rbp"] = 0x38
ror_["rsp"] = 0x3c
ror_["eax"] = 0x40
ror_["ebx"] = 0x43
ror_["ecx"] = 0x46
ror_["edx"] = 0x49
ror_["esi"] = 0x4c
ror_["edi"] = 0x4f
ror_["ebp"] = 0x52
ror_["esp"] = 0x55
ror_["ax"] = 0x58
ror_["bx"] = 0x5c
ror_["cx"] = 0x60
ror_["dx"] = 0x64
ror_["si"] = 0x68
ror_["di"] = 0x6c
ror_["bp"] = 0x70
ror_["sp"] = 0x74
ror_["ah"] = 0x78
ror_["bh"] = 0x7b
ror_["ch"] = 0x7e
ror_["dh"] = 0x81
ror_["al"] = 0x84
ror_["bl"] = 0x87
ror_["cl"] = 0x8a
ror_["dl"] = 0x8d
rol_ = {}
rol_["rax"] = 0x90
rol_["rbx"] = 0x94
rol_["rcx"] = 0x98
rol_["rdx"] = 0x9c
rol_["rsi"] = 0xa0
rol_["rdi"] = 0xa4
rol_["rbp"] = 0xa8
rol_["rsp"] = 0xac
rol_["eax"] = 0xb0
rol_["ebx"] = 0xb3
rol_["ecx"] = 0xb6
rol_["edx"] = 0xb9
rol_["esi"] = 0xbc
rol_["edi"] = 0xbf
rol_["ebp"] = 0xc2
rol_["esp"] = 0xc5
rol_["ax"] = 0xc8
rol_["bx"] = 0xcc
rol_["cx"] = 0xd0
rol_["dx"] = 0xd4
rol_["si"] = 0xd8
rol_["di"] = 0xdc
rol_["bp"] = 0xe0
rol_["sp"] = 0xe4
rol_["ah"] = 0xe8
rol_["bh"] = 0xeb
rol_["ch"] = 0xee
rol_["dh"] = 0xf1
rol_["al"] = 0xf4
rol_["bl"] = 0xf7
rol_["cl"] = 0xfa
rol_["dl"] = 0xfd
not_ = {}
not_["rax"] = 0x100
not_["rbx"] = 0x104
not_["rcx"] = 0x108
not_["rdx"] = 0x10c
not_["rsi"] = 0x110
not_["rdi"] = 0x114
not_["rbp"] = 0x118
not_["rsp"] = 0x11c
not_["eax"] = 0x120
not_["ebx"] = 0x123
not_["ecx"] = 0x126
not_["edx"] = 0x129
not_["esi"] = 0x12c
not_["edi"] = 0x12f
not_["ebp"] = 0x132
not_["esp"] = 0x135
not_["ax"] = 0x138
not_["bx"] = 0x13c
not_["cx"] = 0x140
not_["dx"] = 0x144
not_["si"] = 0x148
not_["di"] = 0x14c
not_["bp"] = 0x150
not_["sp"] = 0x154
not_["ah"] = 0x158
not_["bh"] = 0x15b
not_["ch"] = 0x15e
not_["dh"] = 0x161
not_["al"] = 0x164
not_["bl"] = 0x167
not_["cl"] = 0x16a
not_["dl"] = 0x16d
mul_ = {}
mul_["rax"] = 0x170
mul_["rbx"] = 0x174
mul_["rcx"] = 0x178
mul_["rdx"] = 0x17c
mul_["rsi"] = 0x180
mul_["rdi"] = 0x184
mul_["rbp"] = 0x188
mul_["rsp"] = 0x18c
mul_["eax"] = 0x190
mul_["ebx"] = 0x193
mul_["ecx"] = 0x196
mul_["edx"] = 0x199
mul_["esi"] = 0x19c
mul_["edi"] = 0x19f
mul_["ebp"] = 0x1a2
mul_["esp"] = 0x1a5
mul_["ax"] = 0x1a8
mul_["bx"] = 0x1ac
mul_["cx"] = 0x1b0
mul_["dx"] = 0x1b4
mul_["si"] = 0x1b8
mul_["di"] = 0x1bc
mul_["bp"] = 0x1c0
mul_["sp"] = 0x1c4
mul_["ah"] = 0x1c8
mul_["bh"] = 0x1cb
mul_["ch"] = 0x1ce
mul_["dh"] = 0x1d1
mul_["al"] = 0x1d4
mul_["bl"] = 0x1d7
mul_["cl"] = 0x1da
mul_["dl"] = 0x1dd
div_ = {}
div_["rax"] = 0x1e0
div_["rbx"] = 0x1e4
div_["rcx"] = 0x1e8
div_["rdx"] = 0x1ec
div_["rsi"] = 0x1f0
div_["rdi"] = 0x1f4
div_["rbp"] = 0x1f8
div_["rsp"] = 0x1fc
div_["eax"] = 0x200
div_["ebx"] = 0x203
div_["ecx"] = 0x206
div_["edx"] = 0x209
div_["esi"] = 0x20c
div_["edi"] = 0x20f
div_["ebp"] = 0x212
div_["esp"] = 0x215
div_["ax"] = 0x218
div_["bx"] = 0x21c
div_["cx"] = 0x220
div_["dx"] = 0x224
div_["si"] = 0x228
div_["di"] = 0x22c
div_["bp"] = 0x230
div_["sp"] = 0x234
div_["ah"] = 0x238
div_["bh"] = 0x23b
div_["ch"] = 0x23e
div_["dh"] = 0x241
div_["al"] = 0x244
div_["bl"] = 0x247
div_["cl"] = 0x24a
div_["dl"] = 0x24d
mov_ = {}
gendict(mov_, "rax")
mov_["rax"]["rbx"] = 0x250
mov_["rax"]["rcx"] = 0x254
mov_["rax"]["rdx"] = 0x258
mov_["rax"]["rsi"] = 0x25c
mov_["rax"]["rdi"] = 0x260
mov_["rax"]["rbp"] = 0x264
mov_["rax"]["rsp"] = 0x268
gendict(mov_, "addrrax")
mov_["addrrax"]["rax"] = 0x26c
mov_["rax"]["addrrax"] = 0x270
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rax"] = 0x274
mov_["rax"]["addrrbx"] = 0x278
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rax"] = 0x27c
mov_["rax"]["addrrcx"] = 0x280
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rax"] = 0x284
mov_["rax"]["addrrdx"] = 0x288
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rax"] = 0x28c
mov_["rax"]["addrrsi"] = 0x290
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rax"] = 0x294
mov_["rax"]["addrrdi"] = 0x298
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rax"] = 0x29c
mov_["rax"]["addrrbp"] = 0x2a1
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rax"] = 0x2a6
mov_["rax"]["addrrsp"] = 0x2ab
gendict(mov_, "rbx")
mov_["rbx"]["rax"] = 0x2b0
mov_["rbx"]["rcx"] = 0x2b4
mov_["rbx"]["rdx"] = 0x2b8
mov_["rbx"]["rsi"] = 0x2bc
mov_["rbx"]["rdi"] = 0x2c0
mov_["rbx"]["rbp"] = 0x2c4
mov_["rbx"]["rsp"] = 0x2c8
gendict(mov_, "addrrax")
mov_["addrrax"]["rbx"] = 0x2cc
mov_["rbx"]["addrrax"] = 0x2d0
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rbx"] = 0x2d4
mov_["rbx"]["addrrbx"] = 0x2d8
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rbx"] = 0x2dc
mov_["rbx"]["addrrcx"] = 0x2e0
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rbx"] = 0x2e4
mov_["rbx"]["addrrdx"] = 0x2e8
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rbx"] = 0x2ec
mov_["rbx"]["addrrsi"] = 0x2f0
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rbx"] = 0x2f4
mov_["rbx"]["addrrdi"] = 0x2f8
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rbx"] = 0x2fc
mov_["rbx"]["addrrbp"] = 0x301
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rbx"] = 0x306
mov_["rbx"]["addrrsp"] = 0x30b
gendict(mov_, "rcx")
mov_["rcx"]["rax"] = 0x310
mov_["rcx"]["rbx"] = 0x314
mov_["rcx"]["rdx"] = 0x318
mov_["rcx"]["rsi"] = 0x31c
mov_["rcx"]["rdi"] = 0x320
mov_["rcx"]["rbp"] = 0x324
mov_["rcx"]["rsp"] = 0x328
gendict(mov_, "addrrax")
mov_["addrrax"]["rcx"] = 0x32c
mov_["rcx"]["addrrax"] = 0x330
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rcx"] = 0x334
mov_["rcx"]["addrrbx"] = 0x338
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rcx"] = 0x33c
mov_["rcx"]["addrrcx"] = 0x340
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rcx"] = 0x344
mov_["rcx"]["addrrdx"] = 0x348
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rcx"] = 0x34c
mov_["rcx"]["addrrsi"] = 0x350
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rcx"] = 0x354
mov_["rcx"]["addrrdi"] = 0x358
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rcx"] = 0x35c
mov_["rcx"]["addrrbp"] = 0x361
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rcx"] = 0x366
mov_["rcx"]["addrrsp"] = 0x36b
gendict(mov_, "rdx")
mov_["rdx"]["rax"] = 0x370
mov_["rdx"]["rbx"] = 0x374
mov_["rdx"]["rcx"] = 0x378
mov_["rdx"]["rsi"] = 0x37c
mov_["rdx"]["rdi"] = 0x380
mov_["rdx"]["rbp"] = 0x384
mov_["rdx"]["rsp"] = 0x388
gendict(mov_, "addrrax")
mov_["addrrax"]["rdx"] = 0x38c
mov_["rdx"]["addrrax"] = 0x390
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rdx"] = 0x394
mov_["rdx"]["addrrbx"] = 0x398
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rdx"] = 0x39c
mov_["rdx"]["addrrcx"] = 0x3a0
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rdx"] = 0x3a4
mov_["rdx"]["addrrdx"] = 0x3a8
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rdx"] = 0x3ac
mov_["rdx"]["addrrsi"] = 0x3b0
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rdx"] = 0x3b4
mov_["rdx"]["addrrdi"] = 0x3b8
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rdx"] = 0x3bc
mov_["rdx"]["addrrbp"] = 0x3c1
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rdx"] = 0x3c6
mov_["rdx"]["addrrsp"] = 0x3cb
gendict(mov_, "rsi")
mov_["rsi"]["rax"] = 0x3d0
mov_["rsi"]["rbx"] = 0x3d4
mov_["rsi"]["rcx"] = 0x3d8
mov_["rsi"]["rdx"] = 0x3dc
mov_["rsi"]["rdi"] = 0x3e0
mov_["rsi"]["rbp"] = 0x3e4
mov_["rsi"]["rsp"] = 0x3e8
gendict(mov_, "addrrax")
mov_["addrrax"]["rsi"] = 0x3ec
mov_["rsi"]["addrrax"] = 0x3f0
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rsi"] = 0x3f4
mov_["rsi"]["addrrbx"] = 0x3f8
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rsi"] = 0x3fc
mov_["rsi"]["addrrcx"] = 0x400
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rsi"] = 0x404
mov_["rsi"]["addrrdx"] = 0x408
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rsi"] = 0x40c
mov_["rsi"]["addrrsi"] = 0x410
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rsi"] = 0x414
mov_["rsi"]["addrrdi"] = 0x418
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rsi"] = 0x41c
mov_["rsi"]["addrrbp"] = 0x421
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rsi"] = 0x426
mov_["rsi"]["addrrsp"] = 0x42b
gendict(mov_, "rdi")
mov_["rdi"]["rax"] = 0x430
mov_["rdi"]["rbx"] = 0x434
mov_["rdi"]["rcx"] = 0x438
mov_["rdi"]["rdx"] = 0x43c
mov_["rdi"]["rsi"] = 0x440
mov_["rdi"]["rbp"] = 0x444
mov_["rdi"]["rsp"] = 0x448
gendict(mov_, "addrrax")
mov_["addrrax"]["rdi"] = 0x44c
mov_["rdi"]["addrrax"] = 0x450
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rdi"] = 0x454
mov_["rdi"]["addrrbx"] = 0x458
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rdi"] = 0x45c
mov_["rdi"]["addrrcx"] = 0x460
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rdi"] = 0x464
mov_["rdi"]["addrrdx"] = 0x468
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rdi"] = 0x46c
mov_["rdi"]["addrrsi"] = 0x470
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rdi"] = 0x474
mov_["rdi"]["addrrdi"] = 0x478
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rdi"] = 0x47c
mov_["rdi"]["addrrbp"] = 0x481
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rdi"] = 0x486
mov_["rdi"]["addrrsp"] = 0x48b
gendict(mov_, "rbp")
mov_["rbp"]["rax"] = 0x490
mov_["rbp"]["rbx"] = 0x494
mov_["rbp"]["rcx"] = 0x498
mov_["rbp"]["rdx"] = 0x49c
mov_["rbp"]["rsi"] = 0x4a0
mov_["rbp"]["rdi"] = 0x4a4
mov_["rbp"]["rsp"] = 0x4a8
gendict(mov_, "addrrax")
mov_["addrrax"]["rbp"] = 0x4ac
mov_["rbp"]["addrrax"] = 0x4b0
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rbp"] = 0x4b4
mov_["rbp"]["addrrbx"] = 0x4b8
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rbp"] = 0x4bc
mov_["rbp"]["addrrcx"] = 0x4c0
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rbp"] = 0x4c4
mov_["rbp"]["addrrdx"] = 0x4c8
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rbp"] = 0x4cc
mov_["rbp"]["addrrsi"] = 0x4d0
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rbp"] = 0x4d4
mov_["rbp"]["addrrdi"] = 0x4d8
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rbp"] = 0x4dc
mov_["rbp"]["addrrbp"] = 0x4e1
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rbp"] = 0x4e6
mov_["rbp"]["addrrsp"] = 0x4eb
gendict(mov_, "rsp")
mov_["rsp"]["rax"] = 0x4f0
mov_["rsp"]["rbx"] = 0x4f4
mov_["rsp"]["rcx"] = 0x4f8
mov_["rsp"]["rdx"] = 0x4fc
mov_["rsp"]["rsi"] = 0x500
mov_["rsp"]["rdi"] = 0x504
mov_["rsp"]["rbp"] = 0x508
gendict(mov_, "addrrax")
mov_["addrrax"]["rsp"] = 0x50c
mov_["rsp"]["addrrax"] = 0x510
gendict(mov_, "addrrbx")
mov_["addrrbx"]["rsp"] = 0x514
mov_["rsp"]["addrrbx"] = 0x518
gendict(mov_, "addrrcx")
mov_["addrrcx"]["rsp"] = 0x51c
mov_["rsp"]["addrrcx"] = 0x520
gendict(mov_, "addrrdx")
mov_["addrrdx"]["rsp"] = 0x524
mov_["rsp"]["addrrdx"] = 0x528
gendict(mov_, "addrrsi")
mov_["addrrsi"]["rsp"] = 0x52c
mov_["rsp"]["addrrsi"] = 0x530
gendict(mov_, "addrrdi")
mov_["addrrdi"]["rsp"] = 0x534
mov_["rsp"]["addrrdi"] = 0x538
gendict(mov_, "addrrbp")
mov_["addrrbp"]["rsp"] = 0x53c
mov_["rsp"]["addrrbp"] = 0x541
gendict(mov_, "addrrsp")
mov_["addrrsp"]["rsp"] = 0x546
mov_["rsp"]["addrrsp"] = 0x54b
gendict(mov_, "eax")
mov_["eax"]["ebx"] = 0x550
mov_["eax"]["ecx"] = 0x553
mov_["eax"]["edx"] = 0x556
mov_["eax"]["esi"] = 0x559
mov_["eax"]["edi"] = 0x55c
mov_["eax"]["ebp"] = 0x55f
mov_["eax"]["esp"] = 0x562
gendict(mov_, "addrrax")
mov_["addrrax"]["eax"] = 0x565
mov_["eax"]["addrrax"] = 0x568
gendict(mov_, "addrrbx")
mov_["addrrbx"]["eax"] = 0x56b
mov_["eax"]["addrrbx"] = 0x56e
gendict(mov_, "addrrcx")
mov_["addrrcx"]["eax"] = 0x571
mov_["eax"]["addrrcx"] = 0x574
gendict(mov_, "addrrdx")
mov_["addrrdx"]["eax"] = 0x577
mov_["eax"]["addrrdx"] = 0x57a
gendict(mov_, "addrrsi")
mov_["addrrsi"]["eax"] = 0x57d
mov_["eax"]["addrrsi"] = 0x580
gendict(mov_, "addrrdi")
mov_["addrrdi"]["eax"] = 0x583
mov_["eax"]["addrrdi"] = 0x586
gendict(mov_, "addrrbp")
mov_["addrrbp"]["eax"] = 0x589
mov_["eax"]["addrrbp"] = 0x58d
gendict(mov_, "addrrsp")
mov_["addrrsp"]["eax"] = 0x591
mov_["eax"]["addrrsp"] = 0x595
gendict(mov_, "ebx")
mov_["ebx"]["eax"] = 0x599
mov_["ebx"]["ecx"] = 0x59c
mov_["ebx"]["edx"] = 0x59f
mov_["ebx"]["esi"] = 0x5a2
mov_["ebx"]["edi"] = 0x5a5
mov_["ebx"]["ebp"] = 0x5a8
mov_["ebx"]["esp"] = 0x5ab
gendict(mov_, "addrrax")
mov_["addrrax"]["ebx"] = 0x5ae
mov_["ebx"]["addrrax"] = 0x5b1
gendict(mov_, "addrrbx")
mov_["addrrbx"]["ebx"] = 0x5b4
mov_["ebx"]["addrrbx"] = 0x5b7
gendict(mov_, "addrrcx")
mov_["addrrcx"]["ebx"] = 0x5ba
mov_["ebx"]["addrrcx"] = 0x5bd
gendict(mov_, "addrrdx")
mov_["addrrdx"]["ebx"] = 0x5c0
mov_["ebx"]["addrrdx"] = 0x5c3
gendict(mov_, "addrrsi")
mov_["addrrsi"]["ebx"] = 0x5c6
mov_["ebx"]["addrrsi"] = 0x5c9
gendict(mov_, "addrrdi")
mov_["addrrdi"]["ebx"] = 0x5cc
mov_["ebx"]["addrrdi"] = 0x5cf
gendict(mov_, "addrrbp")
mov_["addrrbp"]["ebx"] = 0x5d2
mov_["ebx"]["addrrbp"] = 0x5d6
gendict(mov_, "addrrsp")
mov_["addrrsp"]["ebx"] = 0x5da
mov_["ebx"]["addrrsp"] = 0x5de
gendict(mov_, "ecx")
mov_["ecx"]["eax"] = 0x5e2
mov_["ecx"]["ebx"] = 0x5e5
mov_["ecx"]["edx"] = 0x5e8
mov_["ecx"]["esi"] = 0x5eb
mov_["ecx"]["edi"] = 0x5ee
mov_["ecx"]["ebp"] = 0x5f1
mov_["ecx"]["esp"] = 0x5f4
gendict(mov_, "addrrax")
mov_["addrrax"]["ecx"] = 0x5f7
mov_["ecx"]["addrrax"] = 0x5fa
gendict(mov_, "addrrbx")
mov_["addrrbx"]["ecx"] = 0x5fd
mov_["ecx"]["addrrbx"] = 0x600
gendict(mov_, "addrrcx")
mov_["addrrcx"]["ecx"] = 0x603
mov_["ecx"]["addrrcx"] = 0x606
gendict(mov_, "addrrdx")
mov_["addrrdx"]["ecx"] = 0x609
mov_["ecx"]["addrrdx"] = 0x60c
gendict(mov_, "addrrsi")
mov_["addrrsi"]["ecx"] = 0x60f
mov_["ecx"]["addrrsi"] = 0x612
gendict(mov_, "addrrdi")
mov_["addrrdi"]["ecx"] = 0x615
mov_["ecx"]["addrrdi"] = 0x618
gendict(mov_, "addrrbp")
mov_["addrrbp"]["ecx"] = 0x61b
mov_["ecx"]["addrrbp"] = 0x61f
gendict(mov_, "addrrsp")
mov_["addrrsp"]["ecx"] = 0x623
mov_["ecx"]["addrrsp"] = 0x627
gendict(mov_, "edx")
mov_["edx"]["eax"] = 0x62b
mov_["edx"]["ebx"] = 0x62e
mov_["edx"]["ecx"] = 0x631
mov_["edx"]["esi"] = 0x634
mov_["edx"]["edi"] = 0x637
mov_["edx"]["ebp"] = 0x63a
mov_["edx"]["esp"] = 0x63d
gendict(mov_, "addrrax")
mov_["addrrax"]["edx"] = 0x640
mov_["edx"]["addrrax"] = 0x643
gendict(mov_, "addrrbx")
mov_["addrrbx"]["edx"] = 0x646
mov_["edx"]["addrrbx"] = 0x649
gendict(mov_, "addrrcx")
mov_["addrrcx"]["edx"] = 0x64c
mov_["edx"]["addrrcx"] = 0x64f
gendict(mov_, "addrrdx")
mov_["addrrdx"]["edx"] = 0x652
mov_["edx"]["addrrdx"] = 0x655
gendict(mov_, "addrrsi")
mov_["addrrsi"]["edx"] = 0x658
mov_["edx"]["addrrsi"] = 0x65b
gendict(mov_, "addrrdi")
mov_["addrrdi"]["edx"] = 0x65e
mov_["edx"]["addrrdi"] = 0x661
gendict(mov_, "addrrbp")
mov_["addrrbp"]["edx"] = 0x664
mov_["edx"]["addrrbp"] = 0x668
gendict(mov_, "addrrsp")
mov_["addrrsp"]["edx"] = 0x66c
mov_["edx"]["addrrsp"] = 0x670
gendict(mov_, "esi")
mov_["esi"]["eax"] = 0x674
mov_["esi"]["ebx"] = 0x677
mov_["esi"]["ecx"] = 0x67a
mov_["esi"]["edx"] = 0x67d
mov_["esi"]["edi"] = 0x680
mov_["esi"]["ebp"] = 0x683
mov_["esi"]["esp"] = 0x686
gendict(mov_, "addrrax")
mov_["addrrax"]["esi"] = 0x689
mov_["esi"]["addrrax"] = 0x68c
gendict(mov_, "addrrbx")
mov_["addrrbx"]["esi"] = 0x68f
mov_["esi"]["addrrbx"] = 0x692
gendict(mov_, "addrrcx")
mov_["addrrcx"]["esi"] = 0x695
mov_["esi"]["addrrcx"] = 0x698
gendict(mov_, "addrrdx")
mov_["addrrdx"]["esi"] = 0x69b
mov_["esi"]["addrrdx"] = 0x69e
gendict(mov_, "addrrsi")
mov_["addrrsi"]["esi"] = 0x6a1
mov_["esi"]["addrrsi"] = 0x6a4
gendict(mov_, "addrrdi")
mov_["addrrdi"]["esi"] = 0x6a7
mov_["esi"]["addrrdi"] = 0x6aa
gendict(mov_, "addrrbp")
mov_["addrrbp"]["esi"] = 0x6ad
mov_["esi"]["addrrbp"] = 0x6b1
gendict(mov_, "addrrsp")
mov_["addrrsp"]["esi"] = 0x6b5
mov_["esi"]["addrrsp"] = 0x6b9
gendict(mov_, "edi")
mov_["edi"]["eax"] = 0x6bd
mov_["edi"]["ebx"] = 0x6c0
mov_["edi"]["ecx"] = 0x6c3
mov_["edi"]["edx"] = 0x6c6
mov_["edi"]["esi"] = 0x6c9
mov_["edi"]["ebp"] = 0x6cc
mov_["edi"]["esp"] = 0x6cf
gendict(mov_, "addrrax")
mov_["addrrax"]["edi"] = 0x6d2
mov_["edi"]["addrrax"] = 0x6d5
gendict(mov_, "addrrbx")
mov_["addrrbx"]["edi"] = 0x6d8
mov_["edi"]["addrrbx"] = 0x6db
gendict(mov_, "addrrcx")
mov_["addrrcx"]["edi"] = 0x6de
mov_["edi"]["addrrcx"] = 0x6e1
gendict(mov_, "addrrdx")
mov_["addrrdx"]["edi"] = 0x6e4
mov_["edi"]["addrrdx"] = 0x6e7
gendict(mov_, "addrrsi")
mov_["addrrsi"]["edi"] = 0x6ea
mov_["edi"]["addrrsi"] = 0x6ed
gendict(mov_, "addrrdi")
mov_["addrrdi"]["edi"] = 0x6f0
mov_["edi"]["addrrdi"] = 0x6f3
gendict(mov_, "addrrbp")
mov_["addrrbp"]["edi"] = 0x6f6
mov_["edi"]["addrrbp"] = 0x6fa
gendict(mov_, "addrrsp")
mov_["addrrsp"]["edi"] = 0x6fe
mov_["edi"]["addrrsp"] = 0x702
gendict(mov_, "ebp")
mov_["ebp"]["eax"] = 0x706
mov_["ebp"]["ebx"] = 0x709
mov_["ebp"]["ecx"] = 0x70c
mov_["ebp"]["edx"] = 0x70f
mov_["ebp"]["esi"] = 0x712
mov_["ebp"]["edi"] = 0x715
mov_["ebp"]["esp"] = 0x718
gendict(mov_, "addrrax")
mov_["addrrax"]["ebp"] = 0x71b
mov_["ebp"]["addrrax"] = 0x71e
gendict(mov_, "addrrbx")
mov_["addrrbx"]["ebp"] = 0x721
mov_["ebp"]["addrrbx"] = 0x724
gendict(mov_, "addrrcx")
mov_["addrrcx"]["ebp"] = 0x727
mov_["ebp"]["addrrcx"] = 0x72a
gendict(mov_, "addrrdx")
mov_["addrrdx"]["ebp"] = 0x72d
mov_["ebp"]["addrrdx"] = 0x730
gendict(mov_, "addrrsi")
mov_["addrrsi"]["ebp"] = 0x733
mov_["ebp"]["addrrsi"] = 0x736
gendict(mov_, "addrrdi")
mov_["addrrdi"]["ebp"] = 0x739
mov_["ebp"]["addrrdi"] = 0x73c
gendict(mov_, "addrrbp")
mov_["addrrbp"]["ebp"] = 0x73f
mov_["ebp"]["addrrbp"] = 0x743
gendict(mov_, "addrrsp")
mov_["addrrsp"]["ebp"] = 0x747
mov_["ebp"]["addrrsp"] = 0x74b
gendict(mov_, "esp")
mov_["esp"]["eax"] = 0x74f
mov_["esp"]["ebx"] = 0x752
mov_["esp"]["ecx"] = 0x755
mov_["esp"]["edx"] = 0x758
mov_["esp"]["esi"] = 0x75b
mov_["esp"]["edi"] = 0x75e
mov_["esp"]["ebp"] = 0x761
gendict(mov_, "addrrax")
mov_["addrrax"]["esp"] = 0x764
mov_["esp"]["addrrax"] = 0x767
gendict(mov_, "addrrbx")
mov_["addrrbx"]["esp"] = 0x76a
mov_["esp"]["addrrbx"] = 0x76d
gendict(mov_, "addrrcx")
mov_["addrrcx"]["esp"] = 0x770
mov_["esp"]["addrrcx"] = 0x773
gendict(mov_, "addrrdx")
mov_["addrrdx"]["esp"] = 0x776
mov_["esp"]["addrrdx"] = 0x779
gendict(mov_, "addrrsi")
mov_["addrrsi"]["esp"] = 0x77c
mov_["esp"]["addrrsi"] = 0x77f
gendict(mov_, "addrrdi")
mov_["addrrdi"]["esp"] = 0x782
mov_["esp"]["addrrdi"] = 0x785
gendict(mov_, "addrrbp")
mov_["addrrbp"]["esp"] = 0x788
mov_["esp"]["addrrbp"] = 0x78c
gendict(mov_, "addrrsp")
mov_["addrrsp"]["esp"] = 0x790
mov_["esp"]["addrrsp"] = 0x794
gendict(mov_, "ax")
mov_["ax"]["bx"] = 0x798
mov_["ax"]["cx"] = 0x79c
mov_["ax"]["dx"] = 0x7a0
mov_["ax"]["si"] = 0x7a4
mov_["ax"]["di"] = 0x7a8
mov_["ax"]["bp"] = 0x7ac
mov_["ax"]["sp"] = 0x7b0
gendict(mov_, "addrrax")
mov_["addrrax"]["ax"] = 0x7b4
mov_["ax"]["addrrax"] = 0x7b8
gendict(mov_, "addrrbx")
mov_["addrrbx"]["ax"] = 0x7bc
mov_["ax"]["addrrbx"] = 0x7c0
gendict(mov_, "addrrcx")
mov_["addrrcx"]["ax"] = 0x7c4
mov_["ax"]["addrrcx"] = 0x7c8
gendict(mov_, "addrrdx")
mov_["addrrdx"]["ax"] = 0x7cc
mov_["ax"]["addrrdx"] = 0x7d0
gendict(mov_, "addrrsi")
mov_["addrrsi"]["ax"] = 0x7d4
mov_["ax"]["addrrsi"] = 0x7d8
gendict(mov_, "addrrdi")
mov_["addrrdi"]["ax"] = 0x7dc
mov_["ax"]["addrrdi"] = 0x7e0
gendict(mov_, "addrrbp")
mov_["addrrbp"]["ax"] = 0x7e4
mov_["ax"]["addrrbp"] = 0x7e9
gendict(mov_, "addrrsp")
mov_["addrrsp"]["ax"] = 0x7ee
mov_["ax"]["addrrsp"] = 0x7f3
gendict(mov_, "bx")
mov_["bx"]["ax"] = 0x7f8
mov_["bx"]["cx"] = 0x7fc
mov_["bx"]["dx"] = 0x800
mov_["bx"]["si"] = 0x804
mov_["bx"]["di"] = 0x808
mov_["bx"]["bp"] = 0x80c
mov_["bx"]["sp"] = 0x810
gendict(mov_, "addrrax")
mov_["addrrax"]["bx"] = 0x814
mov_["bx"]["addrrax"] = 0x818
gendict(mov_, "addrrbx")
mov_["addrrbx"]["bx"] = 0x81c
mov_["bx"]["addrrbx"] = 0x820
gendict(mov_, "addrrcx")
mov_["addrrcx"]["bx"] = 0x824
mov_["bx"]["addrrcx"] = 0x828
gendict(mov_, "addrrdx")
mov_["addrrdx"]["bx"] = 0x82c
mov_["bx"]["addrrdx"] = 0x830
gendict(mov_, "addrrsi")
mov_["addrrsi"]["bx"] = 0x834
mov_["bx"]["addrrsi"] = 0x838
gendict(mov_, "addrrdi")
mov_["addrrdi"]["bx"] = 0x83c
mov_["bx"]["addrrdi"] = 0x840
gendict(mov_, "addrrbp")
mov_["addrrbp"]["bx"] = 0x844
mov_["bx"]["addrrbp"] = 0x849
gendict(mov_, "addrrsp")
mov_["addrrsp"]["bx"] = 0x84e
mov_["bx"]["addrrsp"] = 0x853
gendict(mov_, "cx")
mov_["cx"]["ax"] = 0x858
mov_["cx"]["bx"] = 0x85c
mov_["cx"]["dx"] = 0x860
mov_["cx"]["si"] = 0x864
mov_["cx"]["di"] = 0x868
mov_["cx"]["bp"] = 0x86c
mov_["cx"]["sp"] = 0x870
gendict(mov_, "addrrax")
mov_["addrrax"]["cx"] = 0x874
mov_["cx"]["addrrax"] = 0x878
gendict(mov_, "addrrbx")
mov_["addrrbx"]["cx"] = 0x87c
mov_["cx"]["addrrbx"] = 0x880
gendict(mov_, "addrrcx")
mov_["addrrcx"]["cx"] = 0x884
mov_["cx"]["addrrcx"] = 0x888
gendict(mov_, "addrrdx")
mov_["addrrdx"]["cx"] = 0x88c
mov_["cx"]["addrrdx"] = 0x890
gendict(mov_, "addrrsi")
mov_["addrrsi"]["cx"] = 0x894
mov_["cx"]["addrrsi"] = 0x898
gendict(mov_, "addrrdi")
mov_["addrrdi"]["cx"] = 0x89c
mov_["cx"]["addrrdi"] = 0x8a0
gendict(mov_, "addrrbp")
mov_["addrrbp"]["cx"] = 0x8a4
mov_["cx"]["addrrbp"] = 0x8a9
gendict(mov_, "addrrsp")
mov_["addrrsp"]["cx"] = 0x8ae
mov_["cx"]["addrrsp"] = 0x8b3
gendict(mov_, "dx")
mov_["dx"]["ax"] = 0x8b8
mov_["dx"]["bx"] = 0x8bc
mov_["dx"]["cx"] = 0x8c0
mov_["dx"]["si"] = 0x8c4
mov_["dx"]["di"] = 0x8c8
mov_["dx"]["bp"] = 0x8cc
mov_["dx"]["sp"] = 0x8d0
gendict(mov_, "addrrax")
mov_["addrrax"]["dx"] = 0x8d4
mov_["dx"]["addrrax"] = 0x8d8
gendict(mov_, "addrrbx")
mov_["addrrbx"]["dx"] = 0x8dc
mov_["dx"]["addrrbx"] = 0x8e0
gendict(mov_, "addrrcx")
mov_["addrrcx"]["dx"] = 0x8e4
mov_["dx"]["addrrcx"] = 0x8e8
gendict(mov_, "addrrdx")
mov_["addrrdx"]["dx"] = 0x8ec
mov_["dx"]["addrrdx"] = 0x8f0
gendict(mov_, "addrrsi")
mov_["addrrsi"]["dx"] = 0x8f4
mov_["dx"]["addrrsi"] = 0x8f8
gendict(mov_, "addrrdi")
mov_["addrrdi"]["dx"] = 0x8fc
mov_["dx"]["addrrdi"] = 0x900
gendict(mov_, "addrrbp")
mov_["addrrbp"]["dx"] = 0x904
mov_["dx"]["addrrbp"] = 0x909
gendict(mov_, "addrrsp")
mov_["addrrsp"]["dx"] = 0x90e
mov_["dx"]["addrrsp"] = 0x913
gendict(mov_, "si")
mov_["si"]["ax"] = 0x918
mov_["si"]["bx"] = 0x91c
mov_["si"]["cx"] = 0x920
mov_["si"]["dx"] = 0x924
mov_["si"]["di"] = 0x928
mov_["si"]["bp"] = 0x92c
mov_["si"]["sp"] = 0x930
gendict(mov_, "addrrax")
mov_["addrrax"]["si"] = 0x934
mov_["si"]["addrrax"] = 0x938
gendict(mov_, "addrrbx")
mov_["addrrbx"]["si"] = 0x93c
mov_["si"]["addrrbx"] = 0x940
gendict(mov_, "addrrcx")
mov_["addrrcx"]["si"] = 0x944
mov_["si"]["addrrcx"] = 0x948
gendict(mov_, "addrrdx")
mov_["addrrdx"]["si"] = 0x94c
mov_["si"]["addrrdx"] = 0x950
gendict(mov_, "addrrsi")
mov_["addrrsi"]["si"] = 0x954
mov_["si"]["addrrsi"] = 0x958
gendict(mov_, "addrrdi")
mov_["addrrdi"]["si"] = 0x95c
mov_["si"]["addrrdi"] = 0x960
gendict(mov_, "addrrbp")
mov_["addrrbp"]["si"] = 0x964
mov_["si"]["addrrbp"] = 0x969
gendict(mov_, "addrrsp")
mov_["addrrsp"]["si"] = 0x96e
mov_["si"]["addrrsp"] = 0x973
gendict(mov_, "di")
mov_["di"]["ax"] = 0x978
mov_["di"]["bx"] = 0x97c
mov_["di"]["cx"] = 0x980
mov_["di"]["dx"] = 0x984
mov_["di"]["si"] = 0x988
mov_["di"]["bp"] = 0x98c
mov_["di"]["sp"] = 0x990
gendict(mov_, "addrrax")
mov_["addrrax"]["di"] = 0x994
mov_["di"]["addrrax"] = 0x998
gendict(mov_, "addrrbx")
mov_["addrrbx"]["di"] = 0x99c
mov_["di"]["addrrbx"] = 0x9a0
gendict(mov_, "addrrcx")
mov_["addrrcx"]["di"] = 0x9a4
mov_["di"]["addrrcx"] = 0x9a8
gendict(mov_, "addrrdx")
mov_["addrrdx"]["di"] = 0x9ac
mov_["di"]["addrrdx"] = 0x9b0
gendict(mov_, "addrrsi")
mov_["addrrsi"]["di"] = 0x9b4
mov_["di"]["addrrsi"] = 0x9b8
gendict(mov_, "addrrdi")
mov_["addrrdi"]["di"] = 0x9bc
mov_["di"]["addrrdi"] = 0x9c0
gendict(mov_, "addrrbp")
mov_["addrrbp"]["di"] = 0x9c4
mov_["di"]["addrrbp"] = 0x9c9
gendict(mov_, "addrrsp")
mov_["addrrsp"]["di"] = 0x9ce
mov_["di"]["addrrsp"] = 0x9d3
gendict(mov_, "bp")
mov_["bp"]["ax"] = 0x9d8
mov_["bp"]["bx"] = 0x9dc
mov_["bp"]["cx"] = 0x9e0
mov_["bp"]["dx"] = 0x9e4
mov_["bp"]["si"] = 0x9e8
mov_["bp"]["di"] = 0x9ec
mov_["bp"]["sp"] = 0x9f0
gendict(mov_, "addrrax")
mov_["addrrax"]["bp"] = 0x9f4
mov_["bp"]["addrrax"] = 0x9f8
gendict(mov_, "addrrbx")
mov_["addrrbx"]["bp"] = 0x9fc
mov_["bp"]["addrrbx"] = 0xa00
gendict(mov_, "addrrcx")
mov_["addrrcx"]["bp"] = 0xa04
mov_["bp"]["addrrcx"] = 0xa08
gendict(mov_, "addrrdx")
mov_["addrrdx"]["bp"] = 0xa0c
mov_["bp"]["addrrdx"] = 0xa10
gendict(mov_, "addrrsi")
mov_["addrrsi"]["bp"] = 0xa14
mov_["bp"]["addrrsi"] = 0xa18
gendict(mov_, "addrrdi")
mov_["addrrdi"]["bp"] = 0xa1c
mov_["bp"]["addrrdi"] = 0xa20
gendict(mov_, "addrrbp")
mov_["addrrbp"]["bp"] = 0xa24
mov_["bp"]["addrrbp"] = 0xa29
gendict(mov_, "addrrsp")
mov_["addrrsp"]["bp"] = 0xa2e
mov_["bp"]["addrrsp"] = 0xa33
gendict(mov_, "sp")
mov_["sp"]["ax"] = 0xa38
mov_["sp"]["bx"] = 0xa3c
mov_["sp"]["cx"] = 0xa40
mov_["sp"]["dx"] = 0xa44
mov_["sp"]["si"] = 0xa48
mov_["sp"]["di"] = 0xa4c
mov_["sp"]["bp"] = 0xa50
gendict(mov_, "addrrax")
mov_["addrrax"]["sp"] = 0xa54
mov_["sp"]["addrrax"] = 0xa58
gendict(mov_, "addrrbx")
mov_["addrrbx"]["sp"] = 0xa5c
mov_["sp"]["addrrbx"] = 0xa60
gendict(mov_, "addrrcx")
mov_["addrrcx"]["sp"] = 0xa64
mov_["sp"]["addrrcx"] = 0xa68
gendict(mov_, "addrrdx")
mov_["addrrdx"]["sp"] = 0xa6c
mov_["sp"]["addrrdx"] = 0xa70
gendict(mov_, "addrrsi")
mov_["addrrsi"]["sp"] = 0xa74
mov_["sp"]["addrrsi"] = 0xa78
gendict(mov_, "addrrdi")
mov_["addrrdi"]["sp"] = 0xa7c
mov_["sp"]["addrrdi"] = 0xa80
gendict(mov_, "addrrbp")
mov_["addrrbp"]["sp"] = 0xa84
mov_["sp"]["addrrbp"] = 0xa89
gendict(mov_, "addrrsp")
mov_["addrrsp"]["sp"] = 0xa8e
mov_["sp"]["addrrsp"] = 0xa93
gendict(mov_, "ah")
mov_["ah"]["bh"] = 0xa98
mov_["ah"]["ch"] = 0xa9b
mov_["ah"]["dh"] = 0xa9e
gendict(mov_, "addrrax")
mov_["addrrax"]["ah"] = 0xaa1
mov_["ah"]["addrrax"] = 0xaa4
gendict(mov_, "addrrbx")
mov_["addrrbx"]["ah"] = 0xaa7
mov_["ah"]["addrrbx"] = 0xaaa
gendict(mov_, "addrrcx")
mov_["addrrcx"]["ah"] = 0xaad
mov_["ah"]["addrrcx"] = 0xab0
gendict(mov_, "addrrdx")
mov_["addrrdx"]["ah"] = 0xab3
mov_["ah"]["addrrdx"] = 0xab6
gendict(mov_, "addrrsi")
mov_["addrrsi"]["ah"] = 0xab9
mov_["ah"]["addrrsi"] = 0xabc
gendict(mov_, "addrrdi")
mov_["addrrdi"]["ah"] = 0xabf
mov_["ah"]["addrrdi"] = 0xac2
gendict(mov_, "addrrbp")
mov_["addrrbp"]["ah"] = 0xac5
mov_["ah"]["addrrbp"] = 0xac9
gendict(mov_, "addrrsp")
mov_["addrrsp"]["ah"] = 0xacd
mov_["ah"]["addrrsp"] = 0xad1
gendict(mov_, "bh")
mov_["bh"]["ah"] = 0xad5
mov_["bh"]["ch"] = 0xad8
mov_["bh"]["dh"] = 0xadb
gendict(mov_, "addrrax")
mov_["addrrax"]["bh"] = 0xade
mov_["bh"]["addrrax"] = 0xae1
gendict(mov_, "addrrbx")
mov_["addrrbx"]["bh"] = 0xae4
mov_["bh"]["addrrbx"] = 0xae7
gendict(mov_, "addrrcx")
mov_["addrrcx"]["bh"] = 0xaea
mov_["bh"]["addrrcx"] = 0xaed
gendict(mov_, "addrrdx")
mov_["addrrdx"]["bh"] = 0xaf0
mov_["bh"]["addrrdx"] = 0xaf3
gendict(mov_, "addrrsi")
mov_["addrrsi"]["bh"] = 0xaf6
mov_["bh"]["addrrsi"] = 0xaf9
gendict(mov_, "addrrdi")
mov_["addrrdi"]["bh"] = 0xafc
mov_["bh"]["addrrdi"] = 0xaff
gendict(mov_, "addrrbp")
mov_["addrrbp"]["bh"] = 0xb02
mov_["bh"]["addrrbp"] = 0xb06
gendict(mov_, "addrrsp")
mov_["addrrsp"]["bh"] = 0xb0a
mov_["bh"]["addrrsp"] = 0xb0e
gendict(mov_, "ch")
mov_["ch"]["ah"] = 0xb12
mov_["ch"]["bh"] = 0xb15
mov_["ch"]["dh"] = 0xb18
gendict(mov_, "addrrax")
mov_["addrrax"]["ch"] = 0xb1b
mov_["ch"]["addrrax"] = 0xb1e
gendict(mov_, "addrrbx")
mov_["addrrbx"]["ch"] = 0xb21
mov_["ch"]["addrrbx"] = 0xb24
gendict(mov_, "addrrcx")
mov_["addrrcx"]["ch"] = 0xb27
mov_["ch"]["addrrcx"] = 0xb2a
gendict(mov_, "addrrdx")
mov_["addrrdx"]["ch"] = 0xb2d
mov_["ch"]["addrrdx"] = 0xb30
gendict(mov_, "addrrsi")
mov_["addrrsi"]["ch"] = 0xb33
mov_["ch"]["addrrsi"] = 0xb36
gendict(mov_, "addrrdi")
mov_["addrrdi"]["ch"] = 0xb39
mov_["ch"]["addrrdi"] = 0xb3c
gendict(mov_, "addrrbp")
mov_["addrrbp"]["ch"] = 0xb3f
mov_["ch"]["addrrbp"] = 0xb43
gendict(mov_, "addrrsp")
mov_["addrrsp"]["ch"] = 0xb47
mov_["ch"]["addrrsp"] = 0xb4b
gendict(mov_, "dh")
mov_["dh"]["ah"] = 0xb4f
mov_["dh"]["bh"] = 0xb52
mov_["dh"]["ch"] = 0xb55
gendict(mov_, "addrrax")
mov_["addrrax"]["dh"] = 0xb58
mov_["dh"]["addrrax"] = 0xb5b
gendict(mov_, "addrrbx")
mov_["addrrbx"]["dh"] = 0xb5e
mov_["dh"]["addrrbx"] = 0xb61
gendict(mov_, "addrrcx")
mov_["addrrcx"]["dh"] = 0xb64
mov_["dh"]["addrrcx"] = 0xb67
gendict(mov_, "addrrdx")
mov_["addrrdx"]["dh"] = 0xb6a
mov_["dh"]["addrrdx"] = 0xb6d
gendict(mov_, "addrrsi")
mov_["addrrsi"]["dh"] = 0xb70
mov_["dh"]["addrrsi"] = 0xb73
gendict(mov_, "addrrdi")
mov_["addrrdi"]["dh"] = 0xb76
mov_["dh"]["addrrdi"] = 0xb79
gendict(mov_, "addrrbp")
mov_["addrrbp"]["dh"] = 0xb7c
mov_["dh"]["addrrbp"] = 0xb80
gendict(mov_, "addrrsp")
mov_["addrrsp"]["dh"] = 0xb84
mov_["dh"]["addrrsp"] = 0xb88
gendict(mov_, "al")
mov_["al"]["bl"] = 0xb8c
mov_["al"]["cl"] = 0xb8f
mov_["al"]["dl"] = 0xb92
gendict(mov_, "addrrax")
mov_["addrrax"]["al"] = 0xb95
mov_["al"]["addrrax"] = 0xb98
gendict(mov_, "addrrbx")
mov_["addrrbx"]["al"] = 0xb9b
mov_["al"]["addrrbx"] = 0xb9e
gendict(mov_, "addrrcx")
mov_["addrrcx"]["al"] = 0xba1
mov_["al"]["addrrcx"] = 0xba4
gendict(mov_, "addrrdx")
mov_["addrrdx"]["al"] = 0xba7
mov_["al"]["addrrdx"] = 0xbaa
gendict(mov_, "addrrsi")
mov_["addrrsi"]["al"] = 0xbad
mov_["al"]["addrrsi"] = 0xbb0
gendict(mov_, "addrrdi")
mov_["addrrdi"]["al"] = 0xbb3
mov_["al"]["addrrdi"] = 0xbb6
gendict(mov_, "addrrbp")
mov_["addrrbp"]["al"] = 0xbb9
mov_["al"]["addrrbp"] = 0xbbd
gendict(mov_, "addrrsp")
mov_["addrrsp"]["al"] = 0xbc1
mov_["al"]["addrrsp"] = 0xbc5
gendict(mov_, "bl")
mov_["bl"]["al"] = 0xbc9
mov_["bl"]["cl"] = 0xbcc
mov_["bl"]["dl"] = 0xbcf
gendict(mov_, "addrrax")
mov_["addrrax"]["bl"] = 0xbd2
mov_["bl"]["addrrax"] = 0xbd5
gendict(mov_, "addrrbx")
mov_["addrrbx"]["bl"] = 0xbd8
mov_["bl"]["addrrbx"] = 0xbdb
gendict(mov_, "addrrcx")
mov_["addrrcx"]["bl"] = 0xbde
mov_["bl"]["addrrcx"] = 0xbe1
gendict(mov_, "addrrdx")
mov_["addrrdx"]["bl"] = 0xbe4
mov_["bl"]["addrrdx"] = 0xbe7
gendict(mov_, "addrrsi")
mov_["addrrsi"]["bl"] = 0xbea
mov_["bl"]["addrrsi"] = 0xbed
gendict(mov_, "addrrdi")
mov_["addrrdi"]["bl"] = 0xbf0
mov_["bl"]["addrrdi"] = 0xbf3
gendict(mov_, "addrrbp")
mov_["addrrbp"]["bl"] = 0xbf6
mov_["bl"]["addrrbp"] = 0xbfa
gendict(mov_, "addrrsp")
mov_["addrrsp"]["bl"] = 0xbfe
mov_["bl"]["addrrsp"] = 0xc02
gendict(mov_, "cl")
mov_["cl"]["al"] = 0xc06
mov_["cl"]["bl"] = 0xc09
mov_["cl"]["dl"] = 0xc0c
gendict(mov_, "addrrax")
mov_["addrrax"]["cl"] = 0xc0f
mov_["cl"]["addrrax"] = 0xc12
gendict(mov_, "addrrbx")
mov_["addrrbx"]["cl"] = 0xc15
mov_["cl"]["addrrbx"] = 0xc18
gendict(mov_, "addrrcx")
mov_["addrrcx"]["cl"] = 0xc1b
mov_["cl"]["addrrcx"] = 0xc1e
gendict(mov_, "addrrdx")
mov_["addrrdx"]["cl"] = 0xc21
mov_["cl"]["addrrdx"] = 0xc24
gendict(mov_, "addrrsi")
mov_["addrrsi"]["cl"] = 0xc27
mov_["cl"]["addrrsi"] = 0xc2a
gendict(mov_, "addrrdi")
mov_["addrrdi"]["cl"] = 0xc2d
mov_["cl"]["addrrdi"] = 0xc30
gendict(mov_, "addrrbp")
mov_["addrrbp"]["cl"] = 0xc33
mov_["cl"]["addrrbp"] = 0xc37
gendict(mov_, "addrrsp")
mov_["addrrsp"]["cl"] = 0xc3b
mov_["cl"]["addrrsp"] = 0xc3f
gendict(mov_, "dl")
mov_["dl"]["al"] = 0xc43
mov_["dl"]["bl"] = 0xc46
mov_["dl"]["cl"] = 0xc49
gendict(mov_, "addrrax")
mov_["addrrax"]["dl"] = 0xc4c
mov_["dl"]["addrrax"] = 0xc4f
gendict(mov_, "addrrbx")
mov_["addrrbx"]["dl"] = 0xc52
mov_["dl"]["addrrbx"] = 0xc55
gendict(mov_, "addrrcx")
mov_["addrrcx"]["dl"] = 0xc58
mov_["dl"]["addrrcx"] = 0xc5b
gendict(mov_, "addrrdx")
mov_["addrrdx"]["dl"] = 0xc5e
mov_["dl"]["addrrdx"] = 0xc61
gendict(mov_, "addrrsi")
mov_["addrrsi"]["dl"] = 0xc64
mov_["dl"]["addrrsi"] = 0xc67
gendict(mov_, "addrrdi")
mov_["addrrdi"]["dl"] = 0xc6a
mov_["dl"]["addrrdi"] = 0xc6d
gendict(mov_, "addrrbp")
mov_["addrrbp"]["dl"] = 0xc70
mov_["dl"]["addrrbp"] = 0xc74
gendict(mov_, "addrrsp")
mov_["addrrsp"]["dl"] = 0xc78
mov_["dl"]["addrrsp"] = 0xc7c
add_ = {}
gendict(add_, "rax")
add_["rax"]["rbx"] = 0xc80
add_["rax"]["rcx"] = 0xc84
add_["rax"]["rdx"] = 0xc88
add_["rax"]["rsi"] = 0xc8c
add_["rax"]["rdi"] = 0xc90
add_["rax"]["rbp"] = 0xc94
add_["rax"]["rsp"] = 0xc98
gendict(add_, "addrrax")
add_["addrrax"]["rax"] = 0xc9c
add_["rax"]["addrrax"] = 0xca0
gendict(add_, "addrrbx")
add_["addrrbx"]["rax"] = 0xca4
add_["rax"]["addrrbx"] = 0xca8
gendict(add_, "addrrcx")
add_["addrrcx"]["rax"] = 0xcac
add_["rax"]["addrrcx"] = 0xcb0
gendict(add_, "addrrdx")
add_["addrrdx"]["rax"] = 0xcb4
add_["rax"]["addrrdx"] = 0xcb8
gendict(add_, "addrrsi")
add_["addrrsi"]["rax"] = 0xcbc
add_["rax"]["addrrsi"] = 0xcc0
gendict(add_, "addrrdi")
add_["addrrdi"]["rax"] = 0xcc4
add_["rax"]["addrrdi"] = 0xcc8
gendict(add_, "addrrbp")
add_["addrrbp"]["rax"] = 0xccc
add_["rax"]["addrrbp"] = 0xcd1
gendict(add_, "addrrsp")
add_["addrrsp"]["rax"] = 0xcd6
add_["rax"]["addrrsp"] = 0xcdb
gendict(add_, "rbx")
add_["rbx"]["rax"] = 0xce0
add_["rbx"]["rcx"] = 0xce4
add_["rbx"]["rdx"] = 0xce8
add_["rbx"]["rsi"] = 0xcec
add_["rbx"]["rdi"] = 0xcf0
add_["rbx"]["rbp"] = 0xcf4
add_["rbx"]["rsp"] = 0xcf8
gendict(add_, "addrrax")
add_["addrrax"]["rbx"] = 0xcfc
add_["rbx"]["addrrax"] = 0xd00
gendict(add_, "addrrbx")
add_["addrrbx"]["rbx"] = 0xd04
add_["rbx"]["addrrbx"] = 0xd08
gendict(add_, "addrrcx")
add_["addrrcx"]["rbx"] = 0xd0c
add_["rbx"]["addrrcx"] = 0xd10
gendict(add_, "addrrdx")
add_["addrrdx"]["rbx"] = 0xd14
add_["rbx"]["addrrdx"] = 0xd18
gendict(add_, "addrrsi")
add_["addrrsi"]["rbx"] = 0xd1c
add_["rbx"]["addrrsi"] = 0xd20
gendict(add_, "addrrdi")
add_["addrrdi"]["rbx"] = 0xd24
add_["rbx"]["addrrdi"] = 0xd28
gendict(add_, "addrrbp")
add_["addrrbp"]["rbx"] = 0xd2c
add_["rbx"]["addrrbp"] = 0xd31
gendict(add_, "addrrsp")
add_["addrrsp"]["rbx"] = 0xd36
add_["rbx"]["addrrsp"] = 0xd3b
gendict(add_, "rcx")
add_["rcx"]["rax"] = 0xd40
add_["rcx"]["rbx"] = 0xd44
add_["rcx"]["rdx"] = 0xd48
add_["rcx"]["rsi"] = 0xd4c
add_["rcx"]["rdi"] = 0xd50
add_["rcx"]["rbp"] = 0xd54
add_["rcx"]["rsp"] = 0xd58
gendict(add_, "addrrax")
add_["addrrax"]["rcx"] = 0xd5c
add_["rcx"]["addrrax"] = 0xd60
gendict(add_, "addrrbx")
add_["addrrbx"]["rcx"] = 0xd64
add_["rcx"]["addrrbx"] = 0xd68
gendict(add_, "addrrcx")
add_["addrrcx"]["rcx"] = 0xd6c
add_["rcx"]["addrrcx"] = 0xd70
gendict(add_, "addrrdx")
add_["addrrdx"]["rcx"] = 0xd74
add_["rcx"]["addrrdx"] = 0xd78
gendict(add_, "addrrsi")
add_["addrrsi"]["rcx"] = 0xd7c
add_["rcx"]["addrrsi"] = 0xd80
gendict(add_, "addrrdi")
add_["addrrdi"]["rcx"] = 0xd84
add_["rcx"]["addrrdi"] = 0xd88
gendict(add_, "addrrbp")
add_["addrrbp"]["rcx"] = 0xd8c
add_["rcx"]["addrrbp"] = 0xd91
gendict(add_, "addrrsp")
add_["addrrsp"]["rcx"] = 0xd96
add_["rcx"]["addrrsp"] = 0xd9b
gendict(add_, "rdx")
add_["rdx"]["rax"] = 0xda0
add_["rdx"]["rbx"] = 0xda4
add_["rdx"]["rcx"] = 0xda8
add_["rdx"]["rsi"] = 0xdac
add_["rdx"]["rdi"] = 0xdb0
add_["rdx"]["rbp"] = 0xdb4
add_["rdx"]["rsp"] = 0xdb8
gendict(add_, "addrrax")
add_["addrrax"]["rdx"] = 0xdbc
add_["rdx"]["addrrax"] = 0xdc0
gendict(add_, "addrrbx")
add_["addrrbx"]["rdx"] = 0xdc4
add_["rdx"]["addrrbx"] = 0xdc8
gendict(add_, "addrrcx")
add_["addrrcx"]["rdx"] = 0xdcc
add_["rdx"]["addrrcx"] = 0xdd0
gendict(add_, "addrrdx")
add_["addrrdx"]["rdx"] = 0xdd4
add_["rdx"]["addrrdx"] = 0xdd8
gendict(add_, "addrrsi")
add_["addrrsi"]["rdx"] = 0xddc
add_["rdx"]["addrrsi"] = 0xde0
gendict(add_, "addrrdi")
add_["addrrdi"]["rdx"] = 0xde4
add_["rdx"]["addrrdi"] = 0xde8
gendict(add_, "addrrbp")
add_["addrrbp"]["rdx"] = 0xdec
add_["rdx"]["addrrbp"] = 0xdf1
gendict(add_, "addrrsp")
add_["addrrsp"]["rdx"] = 0xdf6
add_["rdx"]["addrrsp"] = 0xdfb
gendict(add_, "rsi")
add_["rsi"]["rax"] = 0xe00
add_["rsi"]["rbx"] = 0xe04
add_["rsi"]["rcx"] = 0xe08
add_["rsi"]["rdx"] = 0xe0c
add_["rsi"]["rdi"] = 0xe10
add_["rsi"]["rbp"] = 0xe14
add_["rsi"]["rsp"] = 0xe18
gendict(add_, "addrrax")
add_["addrrax"]["rsi"] = 0xe1c
add_["rsi"]["addrrax"] = 0xe20
gendict(add_, "addrrbx")
add_["addrrbx"]["rsi"] = 0xe24
add_["rsi"]["addrrbx"] = 0xe28
gendict(add_, "addrrcx")
add_["addrrcx"]["rsi"] = 0xe2c
add_["rsi"]["addrrcx"] = 0xe30
gendict(add_, "addrrdx")
add_["addrrdx"]["rsi"] = 0xe34
add_["rsi"]["addrrdx"] = 0xe38
gendict(add_, "addrrsi")
add_["addrrsi"]["rsi"] = 0xe3c
add_["rsi"]["addrrsi"] = 0xe40
gendict(add_, "addrrdi")
add_["addrrdi"]["rsi"] = 0xe44
add_["rsi"]["addrrdi"] = 0xe48
gendict(add_, "addrrbp")
add_["addrrbp"]["rsi"] = 0xe4c
add_["rsi"]["addrrbp"] = 0xe51
gendict(add_, "addrrsp")
add_["addrrsp"]["rsi"] = 0xe56
add_["rsi"]["addrrsp"] = 0xe5b
gendict(add_, "rdi")
add_["rdi"]["rax"] = 0xe60
add_["rdi"]["rbx"] = 0xe64
add_["rdi"]["rcx"] = 0xe68
add_["rdi"]["rdx"] = 0xe6c
add_["rdi"]["rsi"] = 0xe70
add_["rdi"]["rbp"] = 0xe74
add_["rdi"]["rsp"] = 0xe78
gendict(add_, "addrrax")
add_["addrrax"]["rdi"] = 0xe7c
add_["rdi"]["addrrax"] = 0xe80
gendict(add_, "addrrbx")
add_["addrrbx"]["rdi"] = 0xe84
add_["rdi"]["addrrbx"] = 0xe88
gendict(add_, "addrrcx")
add_["addrrcx"]["rdi"] = 0xe8c
add_["rdi"]["addrrcx"] = 0xe90
gendict(add_, "addrrdx")
add_["addrrdx"]["rdi"] = 0xe94
add_["rdi"]["addrrdx"] = 0xe98
gendict(add_, "addrrsi")
add_["addrrsi"]["rdi"] = 0xe9c
add_["rdi"]["addrrsi"] = 0xea0
gendict(add_, "addrrdi")
add_["addrrdi"]["rdi"] = 0xea4
add_["rdi"]["addrrdi"] = 0xea8
gendict(add_, "addrrbp")
add_["addrrbp"]["rdi"] = 0xeac
add_["rdi"]["addrrbp"] = 0xeb1
gendict(add_, "addrrsp")
add_["addrrsp"]["rdi"] = 0xeb6
add_["rdi"]["addrrsp"] = 0xebb
gendict(add_, "rbp")
add_["rbp"]["rax"] = 0xec0
add_["rbp"]["rbx"] = 0xec4
add_["rbp"]["rcx"] = 0xec8
add_["rbp"]["rdx"] = 0xecc
add_["rbp"]["rsi"] = 0xed0
add_["rbp"]["rdi"] = 0xed4
add_["rbp"]["rsp"] = 0xed8
gendict(add_, "addrrax")
add_["addrrax"]["rbp"] = 0xedc
add_["rbp"]["addrrax"] = 0xee0
gendict(add_, "addrrbx")
add_["addrrbx"]["rbp"] = 0xee4
add_["rbp"]["addrrbx"] = 0xee8
gendict(add_, "addrrcx")
add_["addrrcx"]["rbp"] = 0xeec
add_["rbp"]["addrrcx"] = 0xef0
gendict(add_, "addrrdx")
add_["addrrdx"]["rbp"] = 0xef4
add_["rbp"]["addrrdx"] = 0xef8
gendict(add_, "addrrsi")
add_["addrrsi"]["rbp"] = 0xefc
add_["rbp"]["addrrsi"] = 0xf00
gendict(add_, "addrrdi")
add_["addrrdi"]["rbp"] = 0xf04
add_["rbp"]["addrrdi"] = 0xf08
gendict(add_, "addrrbp")
add_["addrrbp"]["rbp"] = 0xf0c
add_["rbp"]["addrrbp"] = 0xf11
gendict(add_, "addrrsp")
add_["addrrsp"]["rbp"] = 0xf16
add_["rbp"]["addrrsp"] = 0xf1b
gendict(add_, "rsp")
add_["rsp"]["rax"] = 0xf20
add_["rsp"]["rbx"] = 0xf24
add_["rsp"]["rcx"] = 0xf28
add_["rsp"]["rdx"] = 0xf2c
add_["rsp"]["rsi"] = 0xf30
add_["rsp"]["rdi"] = 0xf34
add_["rsp"]["rbp"] = 0xf38
gendict(add_, "addrrax")
add_["addrrax"]["rsp"] = 0xf3c
add_["rsp"]["addrrax"] = 0xf40
gendict(add_, "addrrbx")
add_["addrrbx"]["rsp"] = 0xf44
add_["rsp"]["addrrbx"] = 0xf48
gendict(add_, "addrrcx")
add_["addrrcx"]["rsp"] = 0xf4c
add_["rsp"]["addrrcx"] = 0xf50
gendict(add_, "addrrdx")
add_["addrrdx"]["rsp"] = 0xf54
add_["rsp"]["addrrdx"] = 0xf58
gendict(add_, "addrrsi")
add_["addrrsi"]["rsp"] = 0xf5c
add_["rsp"]["addrrsi"] = 0xf60
gendict(add_, "addrrdi")
add_["addrrdi"]["rsp"] = 0xf64
add_["rsp"]["addrrdi"] = 0xf68
gendict(add_, "addrrbp")
add_["addrrbp"]["rsp"] = 0xf6c
add_["rsp"]["addrrbp"] = 0xf71
gendict(add_, "addrrsp")
add_["addrrsp"]["rsp"] = 0xf76
add_["rsp"]["addrrsp"] = 0xf7b
gendict(add_, "eax")
add_["eax"]["ebx"] = 0xf80
add_["eax"]["ecx"] = 0xf83
add_["eax"]["edx"] = 0xf86
add_["eax"]["esi"] = 0xf89
add_["eax"]["edi"] = 0xf8c
add_["eax"]["ebp"] = 0xf8f
add_["eax"]["esp"] = 0xf92
gendict(add_, "addrrax")
add_["addrrax"]["eax"] = 0xf95
add_["eax"]["addrrax"] = 0xf98
gendict(add_, "addrrbx")
add_["addrrbx"]["eax"] = 0xf9b
add_["eax"]["addrrbx"] = 0xf9e
gendict(add_, "addrrcx")
add_["addrrcx"]["eax"] = 0xfa1
add_["eax"]["addrrcx"] = 0xfa4
gendict(add_, "addrrdx")
add_["addrrdx"]["eax"] = 0xfa7
add_["eax"]["addrrdx"] = 0xfaa
gendict(add_, "addrrsi")
add_["addrrsi"]["eax"] = 0xfad
add_["eax"]["addrrsi"] = 0xfb0
gendict(add_, "addrrdi")
add_["addrrdi"]["eax"] = 0xfb3
add_["eax"]["addrrdi"] = 0xfb6
gendict(add_, "addrrbp")
add_["addrrbp"]["eax"] = 0xfb9
add_["eax"]["addrrbp"] = 0xfbd
gendict(add_, "addrrsp")
add_["addrrsp"]["eax"] = 0xfc1
add_["eax"]["addrrsp"] = 0xfc5
gendict(add_, "ebx")
add_["ebx"]["eax"] = 0xfc9
add_["ebx"]["ecx"] = 0xfcc
add_["ebx"]["edx"] = 0xfcf
add_["ebx"]["esi"] = 0xfd2
add_["ebx"]["edi"] = 0xfd5
add_["ebx"]["ebp"] = 0xfd8
add_["ebx"]["esp"] = 0xfdb
gendict(add_, "addrrax")
add_["addrrax"]["ebx"] = 0xfde
add_["ebx"]["addrrax"] = 0xfe1
gendict(add_, "addrrbx")
add_["addrrbx"]["ebx"] = 0xfe4
add_["ebx"]["addrrbx"] = 0xfe7
gendict(add_, "addrrcx")
add_["addrrcx"]["ebx"] = 0xfea
add_["ebx"]["addrrcx"] = 0xfed
gendict(add_, "addrrdx")
add_["addrrdx"]["ebx"] = 0xff0
add_["ebx"]["addrrdx"] = 0xff3
gendict(add_, "addrrsi")
add_["addrrsi"]["ebx"] = 0xff6
add_["ebx"]["addrrsi"] = 0xff9
gendict(add_, "addrrdi")
add_["addrrdi"]["ebx"] = 0xffc
add_["ebx"]["addrrdi"] = 0xfff
gendict(add_, "addrrbp")
add_["addrrbp"]["ebx"] = 0x1002
add_["ebx"]["addrrbp"] = 0x1006
gendict(add_, "addrrsp")
add_["addrrsp"]["ebx"] = 0x100a
add_["ebx"]["addrrsp"] = 0x100e
gendict(add_, "ecx")
add_["ecx"]["eax"] = 0x1012
add_["ecx"]["ebx"] = 0x1015
add_["ecx"]["edx"] = 0x1018
add_["ecx"]["esi"] = 0x101b
add_["ecx"]["edi"] = 0x101e
add_["ecx"]["ebp"] = 0x1021
add_["ecx"]["esp"] = 0x1024
gendict(add_, "addrrax")
add_["addrrax"]["ecx"] = 0x1027
add_["ecx"]["addrrax"] = 0x102a
gendict(add_, "addrrbx")
add_["addrrbx"]["ecx"] = 0x102d
add_["ecx"]["addrrbx"] = 0x1030
gendict(add_, "addrrcx")
add_["addrrcx"]["ecx"] = 0x1033
add_["ecx"]["addrrcx"] = 0x1036
gendict(add_, "addrrdx")
add_["addrrdx"]["ecx"] = 0x1039
add_["ecx"]["addrrdx"] = 0x103c
gendict(add_, "addrrsi")
add_["addrrsi"]["ecx"] = 0x103f
add_["ecx"]["addrrsi"] = 0x1042
gendict(add_, "addrrdi")
add_["addrrdi"]["ecx"] = 0x1045
add_["ecx"]["addrrdi"] = 0x1048
gendict(add_, "addrrbp")
add_["addrrbp"]["ecx"] = 0x104b
add_["ecx"]["addrrbp"] = 0x104f
gendict(add_, "addrrsp")
add_["addrrsp"]["ecx"] = 0x1053
add_["ecx"]["addrrsp"] = 0x1057
gendict(add_, "edx")
add_["edx"]["eax"] = 0x105b
add_["edx"]["ebx"] = 0x105e
add_["edx"]["ecx"] = 0x1061
add_["edx"]["esi"] = 0x1064
add_["edx"]["edi"] = 0x1067
add_["edx"]["ebp"] = 0x106a
add_["edx"]["esp"] = 0x106d
gendict(add_, "addrrax")
add_["addrrax"]["edx"] = 0x1070
add_["edx"]["addrrax"] = 0x1073
gendict(add_, "addrrbx")
add_["addrrbx"]["edx"] = 0x1076
add_["edx"]["addrrbx"] = 0x1079
gendict(add_, "addrrcx")
add_["addrrcx"]["edx"] = 0x107c
add_["edx"]["addrrcx"] = 0x107f
gendict(add_, "addrrdx")
add_["addrrdx"]["edx"] = 0x1082
add_["edx"]["addrrdx"] = 0x1085
gendict(add_, "addrrsi")
add_["addrrsi"]["edx"] = 0x1088
add_["edx"]["addrrsi"] = 0x108b
gendict(add_, "addrrdi")
add_["addrrdi"]["edx"] = 0x108e
add_["edx"]["addrrdi"] = 0x1091
gendict(add_, "addrrbp")
add_["addrrbp"]["edx"] = 0x1094
add_["edx"]["addrrbp"] = 0x1098
gendict(add_, "addrrsp")
add_["addrrsp"]["edx"] = 0x109c
add_["edx"]["addrrsp"] = 0x10a0
gendict(add_, "esi")
add_["esi"]["eax"] = 0x10a4
add_["esi"]["ebx"] = 0x10a7
add_["esi"]["ecx"] = 0x10aa
add_["esi"]["edx"] = 0x10ad
add_["esi"]["edi"] = 0x10b0
add_["esi"]["ebp"] = 0x10b3
add_["esi"]["esp"] = 0x10b6
gendict(add_, "addrrax")
add_["addrrax"]["esi"] = 0x10b9
add_["esi"]["addrrax"] = 0x10bc
gendict(add_, "addrrbx")
add_["addrrbx"]["esi"] = 0x10bf
add_["esi"]["addrrbx"] = 0x10c2
gendict(add_, "addrrcx")
add_["addrrcx"]["esi"] = 0x10c5
add_["esi"]["addrrcx"] = 0x10c8
gendict(add_, "addrrdx")
add_["addrrdx"]["esi"] = 0x10cb
add_["esi"]["addrrdx"] = 0x10ce
gendict(add_, "addrrsi")
add_["addrrsi"]["esi"] = 0x10d1
add_["esi"]["addrrsi"] = 0x10d4
gendict(add_, "addrrdi")
add_["addrrdi"]["esi"] = 0x10d7
add_["esi"]["addrrdi"] = 0x10da
gendict(add_, "addrrbp")
add_["addrrbp"]["esi"] = 0x10dd
add_["esi"]["addrrbp"] = 0x10e1
gendict(add_, "addrrsp")
add_["addrrsp"]["esi"] = 0x10e5
add_["esi"]["addrrsp"] = 0x10e9
gendict(add_, "edi")
add_["edi"]["eax"] = 0x10ed
add_["edi"]["ebx"] = 0x10f0
add_["edi"]["ecx"] = 0x10f3
add_["edi"]["edx"] = 0x10f6
add_["edi"]["esi"] = 0x10f9
add_["edi"]["ebp"] = 0x10fc
add_["edi"]["esp"] = 0x10ff
gendict(add_, "addrrax")
add_["addrrax"]["edi"] = 0x1102
add_["edi"]["addrrax"] = 0x1105
gendict(add_, "addrrbx")
add_["addrrbx"]["edi"] = 0x1108
add_["edi"]["addrrbx"] = 0x110b
gendict(add_, "addrrcx")
add_["addrrcx"]["edi"] = 0x110e
add_["edi"]["addrrcx"] = 0x1111
gendict(add_, "addrrdx")
add_["addrrdx"]["edi"] = 0x1114
add_["edi"]["addrrdx"] = 0x1117
gendict(add_, "addrrsi")
add_["addrrsi"]["edi"] = 0x111a
add_["edi"]["addrrsi"] = 0x111d
gendict(add_, "addrrdi")
add_["addrrdi"]["edi"] = 0x1120
add_["edi"]["addrrdi"] = 0x1123
gendict(add_, "addrrbp")
add_["addrrbp"]["edi"] = 0x1126
add_["edi"]["addrrbp"] = 0x112a
gendict(add_, "addrrsp")
add_["addrrsp"]["edi"] = 0x112e
add_["edi"]["addrrsp"] = 0x1132
gendict(add_, "ebp")
add_["ebp"]["eax"] = 0x1136
add_["ebp"]["ebx"] = 0x1139
add_["ebp"]["ecx"] = 0x113c
add_["ebp"]["edx"] = 0x113f
add_["ebp"]["esi"] = 0x1142
add_["ebp"]["edi"] = 0x1145
add_["ebp"]["esp"] = 0x1148
gendict(add_, "addrrax")
add_["addrrax"]["ebp"] = 0x114b
add_["ebp"]["addrrax"] = 0x114e
gendict(add_, "addrrbx")
add_["addrrbx"]["ebp"] = 0x1151
add_["ebp"]["addrrbx"] = 0x1154
gendict(add_, "addrrcx")
add_["addrrcx"]["ebp"] = 0x1157
add_["ebp"]["addrrcx"] = 0x115a
gendict(add_, "addrrdx")
add_["addrrdx"]["ebp"] = 0x115d
add_["ebp"]["addrrdx"] = 0x1160
gendict(add_, "addrrsi")
add_["addrrsi"]["ebp"] = 0x1163
add_["ebp"]["addrrsi"] = 0x1166
gendict(add_, "addrrdi")
add_["addrrdi"]["ebp"] = 0x1169
add_["ebp"]["addrrdi"] = 0x116c
gendict(add_, "addrrbp")
add_["addrrbp"]["ebp"] = 0x116f
add_["ebp"]["addrrbp"] = 0x1173
gendict(add_, "addrrsp")
add_["addrrsp"]["ebp"] = 0x1177
add_["ebp"]["addrrsp"] = 0x117b
gendict(add_, "esp")
add_["esp"]["eax"] = 0x117f
add_["esp"]["ebx"] = 0x1182
add_["esp"]["ecx"] = 0x1185
add_["esp"]["edx"] = 0x1188
add_["esp"]["esi"] = 0x118b
add_["esp"]["edi"] = 0x118e
add_["esp"]["ebp"] = 0x1191
gendict(add_, "addrrax")
add_["addrrax"]["esp"] = 0x1194
add_["esp"]["addrrax"] = 0x1197
gendict(add_, "addrrbx")
add_["addrrbx"]["esp"] = 0x119a
add_["esp"]["addrrbx"] = 0x119d
gendict(add_, "addrrcx")
add_["addrrcx"]["esp"] = 0x11a0
add_["esp"]["addrrcx"] = 0x11a3
gendict(add_, "addrrdx")
add_["addrrdx"]["esp"] = 0x11a6
add_["esp"]["addrrdx"] = 0x11a9
gendict(add_, "addrrsi")
add_["addrrsi"]["esp"] = 0x11ac
add_["esp"]["addrrsi"] = 0x11af
gendict(add_, "addrrdi")
add_["addrrdi"]["esp"] = 0x11b2
add_["esp"]["addrrdi"] = 0x11b5
gendict(add_, "addrrbp")
add_["addrrbp"]["esp"] = 0x11b8
add_["esp"]["addrrbp"] = 0x11bc
gendict(add_, "addrrsp")
add_["addrrsp"]["esp"] = 0x11c0
add_["esp"]["addrrsp"] = 0x11c4
gendict(add_, "ax")
add_["ax"]["bx"] = 0x11c8
add_["ax"]["cx"] = 0x11cc
add_["ax"]["dx"] = 0x11d0
add_["ax"]["si"] = 0x11d4
add_["ax"]["di"] = 0x11d8
add_["ax"]["bp"] = 0x11dc
add_["ax"]["sp"] = 0x11e0
gendict(add_, "addrrax")
add_["addrrax"]["ax"] = 0x11e4
add_["ax"]["addrrax"] = 0x11e8
gendict(add_, "addrrbx")
add_["addrrbx"]["ax"] = 0x11ec
add_["ax"]["addrrbx"] = 0x11f0
gendict(add_, "addrrcx")
add_["addrrcx"]["ax"] = 0x11f4
add_["ax"]["addrrcx"] = 0x11f8
gendict(add_, "addrrdx")
add_["addrrdx"]["ax"] = 0x11fc
add_["ax"]["addrrdx"] = 0x1200
gendict(add_, "addrrsi")
add_["addrrsi"]["ax"] = 0x1204
add_["ax"]["addrrsi"] = 0x1208
gendict(add_, "addrrdi")
add_["addrrdi"]["ax"] = 0x120c
add_["ax"]["addrrdi"] = 0x1210
gendict(add_, "addrrbp")
add_["addrrbp"]["ax"] = 0x1214
add_["ax"]["addrrbp"] = 0x1219
gendict(add_, "addrrsp")
add_["addrrsp"]["ax"] = 0x121e
add_["ax"]["addrrsp"] = 0x1223
gendict(add_, "bx")
add_["bx"]["ax"] = 0x1228
add_["bx"]["cx"] = 0x122c
add_["bx"]["dx"] = 0x1230
add_["bx"]["si"] = 0x1234
add_["bx"]["di"] = 0x1238
add_["bx"]["bp"] = 0x123c
add_["bx"]["sp"] = 0x1240
gendict(add_, "addrrax")
add_["addrrax"]["bx"] = 0x1244
add_["bx"]["addrrax"] = 0x1248
gendict(add_, "addrrbx")
add_["addrrbx"]["bx"] = 0x124c
add_["bx"]["addrrbx"] = 0x1250
gendict(add_, "addrrcx")
add_["addrrcx"]["bx"] = 0x1254
add_["bx"]["addrrcx"] = 0x1258
gendict(add_, "addrrdx")
add_["addrrdx"]["bx"] = 0x125c
add_["bx"]["addrrdx"] = 0x1260
gendict(add_, "addrrsi")
add_["addrrsi"]["bx"] = 0x1264
add_["bx"]["addrrsi"] = 0x1268
gendict(add_, "addrrdi")
add_["addrrdi"]["bx"] = 0x126c
add_["bx"]["addrrdi"] = 0x1270
gendict(add_, "addrrbp")
add_["addrrbp"]["bx"] = 0x1274
add_["bx"]["addrrbp"] = 0x1279
gendict(add_, "addrrsp")
add_["addrrsp"]["bx"] = 0x127e
add_["bx"]["addrrsp"] = 0x1283
gendict(add_, "cx")
add_["cx"]["ax"] = 0x1288
add_["cx"]["bx"] = 0x128c
add_["cx"]["dx"] = 0x1290
add_["cx"]["si"] = 0x1294
add_["cx"]["di"] = 0x1298
add_["cx"]["bp"] = 0x129c
add_["cx"]["sp"] = 0x12a0
gendict(add_, "addrrax")
add_["addrrax"]["cx"] = 0x12a4
add_["cx"]["addrrax"] = 0x12a8
gendict(add_, "addrrbx")
add_["addrrbx"]["cx"] = 0x12ac
add_["cx"]["addrrbx"] = 0x12b0
gendict(add_, "addrrcx")
add_["addrrcx"]["cx"] = 0x12b4
add_["cx"]["addrrcx"] = 0x12b8
gendict(add_, "addrrdx")
add_["addrrdx"]["cx"] = 0x12bc
add_["cx"]["addrrdx"] = 0x12c0
gendict(add_, "addrrsi")
add_["addrrsi"]["cx"] = 0x12c4
add_["cx"]["addrrsi"] = 0x12c8
gendict(add_, "addrrdi")
add_["addrrdi"]["cx"] = 0x12cc
add_["cx"]["addrrdi"] = 0x12d0
gendict(add_, "addrrbp")
add_["addrrbp"]["cx"] = 0x12d4
add_["cx"]["addrrbp"] = 0x12d9
gendict(add_, "addrrsp")
add_["addrrsp"]["cx"] = 0x12de
add_["cx"]["addrrsp"] = 0x12e3
gendict(add_, "dx")
add_["dx"]["ax"] = 0x12e8
add_["dx"]["bx"] = 0x12ec
add_["dx"]["cx"] = 0x12f0
add_["dx"]["si"] = 0x12f4
add_["dx"]["di"] = 0x12f8
add_["dx"]["bp"] = 0x12fc
add_["dx"]["sp"] = 0x1300
gendict(add_, "addrrax")
add_["addrrax"]["dx"] = 0x1304
add_["dx"]["addrrax"] = 0x1308
gendict(add_, "addrrbx")
add_["addrrbx"]["dx"] = 0x130c
add_["dx"]["addrrbx"] = 0x1310
gendict(add_, "addrrcx")
add_["addrrcx"]["dx"] = 0x1314
add_["dx"]["addrrcx"] = 0x1318
gendict(add_, "addrrdx")
add_["addrrdx"]["dx"] = 0x131c
add_["dx"]["addrrdx"] = 0x1320
gendict(add_, "addrrsi")
add_["addrrsi"]["dx"] = 0x1324
add_["dx"]["addrrsi"] = 0x1328
gendict(add_, "addrrdi")
add_["addrrdi"]["dx"] = 0x132c
add_["dx"]["addrrdi"] = 0x1330
gendict(add_, "addrrbp")
add_["addrrbp"]["dx"] = 0x1334
add_["dx"]["addrrbp"] = 0x1339
gendict(add_, "addrrsp")
add_["addrrsp"]["dx"] = 0x133e
add_["dx"]["addrrsp"] = 0x1343
gendict(add_, "si")
add_["si"]["ax"] = 0x1348
add_["si"]["bx"] = 0x134c
add_["si"]["cx"] = 0x1350
add_["si"]["dx"] = 0x1354
add_["si"]["di"] = 0x1358
add_["si"]["bp"] = 0x135c
add_["si"]["sp"] = 0x1360
gendict(add_, "addrrax")
add_["addrrax"]["si"] = 0x1364
add_["si"]["addrrax"] = 0x1368
gendict(add_, "addrrbx")
add_["addrrbx"]["si"] = 0x136c
add_["si"]["addrrbx"] = 0x1370
gendict(add_, "addrrcx")
add_["addrrcx"]["si"] = 0x1374
add_["si"]["addrrcx"] = 0x1378
gendict(add_, "addrrdx")
add_["addrrdx"]["si"] = 0x137c
add_["si"]["addrrdx"] = 0x1380
gendict(add_, "addrrsi")
add_["addrrsi"]["si"] = 0x1384
add_["si"]["addrrsi"] = 0x1388
gendict(add_, "addrrdi")
add_["addrrdi"]["si"] = 0x138c
add_["si"]["addrrdi"] = 0x1390
gendict(add_, "addrrbp")
add_["addrrbp"]["si"] = 0x1394
add_["si"]["addrrbp"] = 0x1399
gendict(add_, "addrrsp")
add_["addrrsp"]["si"] = 0x139e
add_["si"]["addrrsp"] = 0x13a3
gendict(add_, "di")
add_["di"]["ax"] = 0x13a8
add_["di"]["bx"] = 0x13ac
add_["di"]["cx"] = 0x13b0
add_["di"]["dx"] = 0x13b4
add_["di"]["si"] = 0x13b8
add_["di"]["bp"] = 0x13bc
add_["di"]["sp"] = 0x13c0
gendict(add_, "addrrax")
add_["addrrax"]["di"] = 0x13c4
add_["di"]["addrrax"] = 0x13c8
gendict(add_, "addrrbx")
add_["addrrbx"]["di"] = 0x13cc
add_["di"]["addrrbx"] = 0x13d0
gendict(add_, "addrrcx")
add_["addrrcx"]["di"] = 0x13d4
add_["di"]["addrrcx"] = 0x13d8
gendict(add_, "addrrdx")
add_["addrrdx"]["di"] = 0x13dc
add_["di"]["addrrdx"] = 0x13e0
gendict(add_, "addrrsi")
add_["addrrsi"]["di"] = 0x13e4
add_["di"]["addrrsi"] = 0x13e8
gendict(add_, "addrrdi")
add_["addrrdi"]["di"] = 0x13ec
add_["di"]["addrrdi"] = 0x13f0
gendict(add_, "addrrbp")
add_["addrrbp"]["di"] = 0x13f4
add_["di"]["addrrbp"] = 0x13f9
gendict(add_, "addrrsp")
add_["addrrsp"]["di"] = 0x13fe
add_["di"]["addrrsp"] = 0x1403
gendict(add_, "bp")
add_["bp"]["ax"] = 0x1408
add_["bp"]["bx"] = 0x140c
add_["bp"]["cx"] = 0x1410
add_["bp"]["dx"] = 0x1414
add_["bp"]["si"] = 0x1418
add_["bp"]["di"] = 0x141c
add_["bp"]["sp"] = 0x1420
gendict(add_, "addrrax")
add_["addrrax"]["bp"] = 0x1424
add_["bp"]["addrrax"] = 0x1428
gendict(add_, "addrrbx")
add_["addrrbx"]["bp"] = 0x142c
add_["bp"]["addrrbx"] = 0x1430
gendict(add_, "addrrcx")
add_["addrrcx"]["bp"] = 0x1434
add_["bp"]["addrrcx"] = 0x1438
gendict(add_, "addrrdx")
add_["addrrdx"]["bp"] = 0x143c
add_["bp"]["addrrdx"] = 0x1440
gendict(add_, "addrrsi")
add_["addrrsi"]["bp"] = 0x1444
add_["bp"]["addrrsi"] = 0x1448
gendict(add_, "addrrdi")
add_["addrrdi"]["bp"] = 0x144c
add_["bp"]["addrrdi"] = 0x1450
gendict(add_, "addrrbp")
add_["addrrbp"]["bp"] = 0x1454
add_["bp"]["addrrbp"] = 0x1459
gendict(add_, "addrrsp")
add_["addrrsp"]["bp"] = 0x145e
add_["bp"]["addrrsp"] = 0x1463
gendict(add_, "sp")
add_["sp"]["ax"] = 0x1468
add_["sp"]["bx"] = 0x146c
add_["sp"]["cx"] = 0x1470
add_["sp"]["dx"] = 0x1474
add_["sp"]["si"] = 0x1478
add_["sp"]["di"] = 0x147c
add_["sp"]["bp"] = 0x1480
gendict(add_, "addrrax")
add_["addrrax"]["sp"] = 0x1484
add_["sp"]["addrrax"] = 0x1488
gendict(add_, "addrrbx")
add_["addrrbx"]["sp"] = 0x148c
add_["sp"]["addrrbx"] = 0x1490
gendict(add_, "addrrcx")
add_["addrrcx"]["sp"] = 0x1494
add_["sp"]["addrrcx"] = 0x1498
gendict(add_, "addrrdx")
add_["addrrdx"]["sp"] = 0x149c
add_["sp"]["addrrdx"] = 0x14a0
gendict(add_, "addrrsi")
add_["addrrsi"]["sp"] = 0x14a4
add_["sp"]["addrrsi"] = 0x14a8
gendict(add_, "addrrdi")
add_["addrrdi"]["sp"] = 0x14ac
add_["sp"]["addrrdi"] = 0x14b0
gendict(add_, "addrrbp")
add_["addrrbp"]["sp"] = 0x14b4
add_["sp"]["addrrbp"] = 0x14b9
gendict(add_, "addrrsp")
add_["addrrsp"]["sp"] = 0x14be
add_["sp"]["addrrsp"] = 0x14c3
gendict(add_, "ah")
add_["ah"]["bh"] = 0x14c8
add_["ah"]["ch"] = 0x14cb
add_["ah"]["dh"] = 0x14ce
gendict(add_, "addrrax")
add_["addrrax"]["ah"] = 0x14d1
add_["ah"]["addrrax"] = 0x14d4
gendict(add_, "addrrbx")
add_["addrrbx"]["ah"] = 0x14d7
add_["ah"]["addrrbx"] = 0x14da
gendict(add_, "addrrcx")
add_["addrrcx"]["ah"] = 0x14dd
add_["ah"]["addrrcx"] = 0x14e0
gendict(add_, "addrrdx")
add_["addrrdx"]["ah"] = 0x14e3
add_["ah"]["addrrdx"] = 0x14e6
gendict(add_, "addrrsi")
add_["addrrsi"]["ah"] = 0x14e9
add_["ah"]["addrrsi"] = 0x14ec
gendict(add_, "addrrdi")
add_["addrrdi"]["ah"] = 0x14ef
add_["ah"]["addrrdi"] = 0x14f2
gendict(add_, "addrrbp")
add_["addrrbp"]["ah"] = 0x14f5
add_["ah"]["addrrbp"] = 0x14f9
gendict(add_, "addrrsp")
add_["addrrsp"]["ah"] = 0x14fd
add_["ah"]["addrrsp"] = 0x1501
gendict(add_, "bh")
add_["bh"]["ah"] = 0x1505
add_["bh"]["ch"] = 0x1508
add_["bh"]["dh"] = 0x150b
gendict(add_, "addrrax")
add_["addrrax"]["bh"] = 0x150e
add_["bh"]["addrrax"] = 0x1511
gendict(add_, "addrrbx")
add_["addrrbx"]["bh"] = 0x1514
add_["bh"]["addrrbx"] = 0x1517
gendict(add_, "addrrcx")
add_["addrrcx"]["bh"] = 0x151a
add_["bh"]["addrrcx"] = 0x151d
gendict(add_, "addrrdx")
add_["addrrdx"]["bh"] = 0x1520
add_["bh"]["addrrdx"] = 0x1523
gendict(add_, "addrrsi")
add_["addrrsi"]["bh"] = 0x1526
add_["bh"]["addrrsi"] = 0x1529
gendict(add_, "addrrdi")
add_["addrrdi"]["bh"] = 0x152c
add_["bh"]["addrrdi"] = 0x152f
gendict(add_, "addrrbp")
add_["addrrbp"]["bh"] = 0x1532
add_["bh"]["addrrbp"] = 0x1536
gendict(add_, "addrrsp")
add_["addrrsp"]["bh"] = 0x153a
add_["bh"]["addrrsp"] = 0x153e
gendict(add_, "ch")
add_["ch"]["ah"] = 0x1542
add_["ch"]["bh"] = 0x1545
add_["ch"]["dh"] = 0x1548
gendict(add_, "addrrax")
add_["addrrax"]["ch"] = 0x154b
add_["ch"]["addrrax"] = 0x154e
gendict(add_, "addrrbx")
add_["addrrbx"]["ch"] = 0x1551
add_["ch"]["addrrbx"] = 0x1554
gendict(add_, "addrrcx")
add_["addrrcx"]["ch"] = 0x1557
add_["ch"]["addrrcx"] = 0x155a
gendict(add_, "addrrdx")
add_["addrrdx"]["ch"] = 0x155d
add_["ch"]["addrrdx"] = 0x1560
gendict(add_, "addrrsi")
add_["addrrsi"]["ch"] = 0x1563
add_["ch"]["addrrsi"] = 0x1566
gendict(add_, "addrrdi")
add_["addrrdi"]["ch"] = 0x1569
add_["ch"]["addrrdi"] = 0x156c
gendict(add_, "addrrbp")
add_["addrrbp"]["ch"] = 0x156f
add_["ch"]["addrrbp"] = 0x1573
gendict(add_, "addrrsp")
add_["addrrsp"]["ch"] = 0x1577
add_["ch"]["addrrsp"] = 0x157b
gendict(add_, "dh")
add_["dh"]["ah"] = 0x157f
add_["dh"]["bh"] = 0x1582
add_["dh"]["ch"] = 0x1585
gendict(add_, "addrrax")
add_["addrrax"]["dh"] = 0x1588
add_["dh"]["addrrax"] = 0x158b
gendict(add_, "addrrbx")
add_["addrrbx"]["dh"] = 0x158e
add_["dh"]["addrrbx"] = 0x1591
gendict(add_, "addrrcx")
add_["addrrcx"]["dh"] = 0x1594
add_["dh"]["addrrcx"] = 0x1597
gendict(add_, "addrrdx")
add_["addrrdx"]["dh"] = 0x159a
add_["dh"]["addrrdx"] = 0x159d
gendict(add_, "addrrsi")
add_["addrrsi"]["dh"] = 0x15a0
add_["dh"]["addrrsi"] = 0x15a3
gendict(add_, "addrrdi")
add_["addrrdi"]["dh"] = 0x15a6
add_["dh"]["addrrdi"] = 0x15a9
gendict(add_, "addrrbp")
add_["addrrbp"]["dh"] = 0x15ac
add_["dh"]["addrrbp"] = 0x15b0
gendict(add_, "addrrsp")
add_["addrrsp"]["dh"] = 0x15b4
add_["dh"]["addrrsp"] = 0x15b8
gendict(add_, "al")
add_["al"]["bl"] = 0x15bc
add_["al"]["cl"] = 0x15bf
add_["al"]["dl"] = 0x15c2
gendict(add_, "addrrax")
add_["addrrax"]["al"] = 0x15c5
add_["al"]["addrrax"] = 0x15c8
gendict(add_, "addrrbx")
add_["addrrbx"]["al"] = 0x15cb
add_["al"]["addrrbx"] = 0x15ce
gendict(add_, "addrrcx")
add_["addrrcx"]["al"] = 0x15d1
add_["al"]["addrrcx"] = 0x15d4
gendict(add_, "addrrdx")
add_["addrrdx"]["al"] = 0x15d7
add_["al"]["addrrdx"] = 0x15da
gendict(add_, "addrrsi")
add_["addrrsi"]["al"] = 0x15dd
add_["al"]["addrrsi"] = 0x15e0
gendict(add_, "addrrdi")
add_["addrrdi"]["al"] = 0x15e3
add_["al"]["addrrdi"] = 0x15e6
gendict(add_, "addrrbp")
add_["addrrbp"]["al"] = 0x15e9
add_["al"]["addrrbp"] = 0x15ed
gendict(add_, "addrrsp")
add_["addrrsp"]["al"] = 0x15f1
add_["al"]["addrrsp"] = 0x15f5
gendict(add_, "bl")
add_["bl"]["al"] = 0x15f9
add_["bl"]["cl"] = 0x15fc
add_["bl"]["dl"] = 0x15ff
gendict(add_, "addrrax")
add_["addrrax"]["bl"] = 0x1602
add_["bl"]["addrrax"] = 0x1605
gendict(add_, "addrrbx")
add_["addrrbx"]["bl"] = 0x1608
add_["bl"]["addrrbx"] = 0x160b
gendict(add_, "addrrcx")
add_["addrrcx"]["bl"] = 0x160e
add_["bl"]["addrrcx"] = 0x1611
gendict(add_, "addrrdx")
add_["addrrdx"]["bl"] = 0x1614
add_["bl"]["addrrdx"] = 0x1617
gendict(add_, "addrrsi")
add_["addrrsi"]["bl"] = 0x161a
add_["bl"]["addrrsi"] = 0x161d
gendict(add_, "addrrdi")
add_["addrrdi"]["bl"] = 0x1620
add_["bl"]["addrrdi"] = 0x1623
gendict(add_, "addrrbp")
add_["addrrbp"]["bl"] = 0x1626
add_["bl"]["addrrbp"] = 0x162a
gendict(add_, "addrrsp")
add_["addrrsp"]["bl"] = 0x162e
add_["bl"]["addrrsp"] = 0x1632
gendict(add_, "cl")
add_["cl"]["al"] = 0x1636
add_["cl"]["bl"] = 0x1639
add_["cl"]["dl"] = 0x163c
gendict(add_, "addrrax")
add_["addrrax"]["cl"] = 0x163f
add_["cl"]["addrrax"] = 0x1642
gendict(add_, "addrrbx")
add_["addrrbx"]["cl"] = 0x1645
add_["cl"]["addrrbx"] = 0x1648
gendict(add_, "addrrcx")
add_["addrrcx"]["cl"] = 0x164b
add_["cl"]["addrrcx"] = 0x164e
gendict(add_, "addrrdx")
add_["addrrdx"]["cl"] = 0x1651
add_["cl"]["addrrdx"] = 0x1654
gendict(add_, "addrrsi")
add_["addrrsi"]["cl"] = 0x1657
add_["cl"]["addrrsi"] = 0x165a
gendict(add_, "addrrdi")
add_["addrrdi"]["cl"] = 0x165d
add_["cl"]["addrrdi"] = 0x1660
gendict(add_, "addrrbp")
add_["addrrbp"]["cl"] = 0x1663
add_["cl"]["addrrbp"] = 0x1667
gendict(add_, "addrrsp")
add_["addrrsp"]["cl"] = 0x166b
add_["cl"]["addrrsp"] = 0x166f
gendict(add_, "dl")
add_["dl"]["al"] = 0x1673
add_["dl"]["bl"] = 0x1676
add_["dl"]["cl"] = 0x1679
gendict(add_, "addrrax")
add_["addrrax"]["dl"] = 0x167c
add_["dl"]["addrrax"] = 0x167f
gendict(add_, "addrrbx")
add_["addrrbx"]["dl"] = 0x1682
add_["dl"]["addrrbx"] = 0x1685
gendict(add_, "addrrcx")
add_["addrrcx"]["dl"] = 0x1688
add_["dl"]["addrrcx"] = 0x168b
gendict(add_, "addrrdx")
add_["addrrdx"]["dl"] = 0x168e
add_["dl"]["addrrdx"] = 0x1691
gendict(add_, "addrrsi")
add_["addrrsi"]["dl"] = 0x1694
add_["dl"]["addrrsi"] = 0x1697
gendict(add_, "addrrdi")
add_["addrrdi"]["dl"] = 0x169a
add_["dl"]["addrrdi"] = 0x169d
gendict(add_, "addrrbp")
add_["addrrbp"]["dl"] = 0x16a0
add_["dl"]["addrrbp"] = 0x16a4
gendict(add_, "addrrsp")
add_["addrrsp"]["dl"] = 0x16a8
add_["dl"]["addrrsp"] = 0x16ac
sub_ = {}
gendict(sub_, "rax")
sub_["rax"]["rbx"] = 0x16b0
sub_["rax"]["rcx"] = 0x16b4
sub_["rax"]["rdx"] = 0x16b8
sub_["rax"]["rsi"] = 0x16bc
sub_["rax"]["rdi"] = 0x16c0
sub_["rax"]["rbp"] = 0x16c4
sub_["rax"]["rsp"] = 0x16c8
gendict(sub_, "addrrax")
sub_["addrrax"]["rax"] = 0x16cc
sub_["rax"]["addrrax"] = 0x16d0
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rax"] = 0x16d4
sub_["rax"]["addrrbx"] = 0x16d8
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rax"] = 0x16dc
sub_["rax"]["addrrcx"] = 0x16e0
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rax"] = 0x16e4
sub_["rax"]["addrrdx"] = 0x16e8
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rax"] = 0x16ec
sub_["rax"]["addrrsi"] = 0x16f0
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rax"] = 0x16f4
sub_["rax"]["addrrdi"] = 0x16f8
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rax"] = 0x16fc
sub_["rax"]["addrrbp"] = 0x1701
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rax"] = 0x1706
sub_["rax"]["addrrsp"] = 0x170b
gendict(sub_, "rbx")
sub_["rbx"]["rax"] = 0x1710
sub_["rbx"]["rcx"] = 0x1714
sub_["rbx"]["rdx"] = 0x1718
sub_["rbx"]["rsi"] = 0x171c
sub_["rbx"]["rdi"] = 0x1720
sub_["rbx"]["rbp"] = 0x1724
sub_["rbx"]["rsp"] = 0x1728
gendict(sub_, "addrrax")
sub_["addrrax"]["rbx"] = 0x172c
sub_["rbx"]["addrrax"] = 0x1730
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rbx"] = 0x1734
sub_["rbx"]["addrrbx"] = 0x1738
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rbx"] = 0x173c
sub_["rbx"]["addrrcx"] = 0x1740
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rbx"] = 0x1744
sub_["rbx"]["addrrdx"] = 0x1748
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rbx"] = 0x174c
sub_["rbx"]["addrrsi"] = 0x1750
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rbx"] = 0x1754
sub_["rbx"]["addrrdi"] = 0x1758
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rbx"] = 0x175c
sub_["rbx"]["addrrbp"] = 0x1761
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rbx"] = 0x1766
sub_["rbx"]["addrrsp"] = 0x176b
gendict(sub_, "rcx")
sub_["rcx"]["rax"] = 0x1770
sub_["rcx"]["rbx"] = 0x1774
sub_["rcx"]["rdx"] = 0x1778
sub_["rcx"]["rsi"] = 0x177c
sub_["rcx"]["rdi"] = 0x1780
sub_["rcx"]["rbp"] = 0x1784
sub_["rcx"]["rsp"] = 0x1788
gendict(sub_, "addrrax")
sub_["addrrax"]["rcx"] = 0x178c
sub_["rcx"]["addrrax"] = 0x1790
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rcx"] = 0x1794
sub_["rcx"]["addrrbx"] = 0x1798
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rcx"] = 0x179c
sub_["rcx"]["addrrcx"] = 0x17a0
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rcx"] = 0x17a4
sub_["rcx"]["addrrdx"] = 0x17a8
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rcx"] = 0x17ac
sub_["rcx"]["addrrsi"] = 0x17b0
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rcx"] = 0x17b4
sub_["rcx"]["addrrdi"] = 0x17b8
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rcx"] = 0x17bc
sub_["rcx"]["addrrbp"] = 0x17c1
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rcx"] = 0x17c6
sub_["rcx"]["addrrsp"] = 0x17cb
gendict(sub_, "rdx")
sub_["rdx"]["rax"] = 0x17d0
sub_["rdx"]["rbx"] = 0x17d4
sub_["rdx"]["rcx"] = 0x17d8
sub_["rdx"]["rsi"] = 0x17dc
sub_["rdx"]["rdi"] = 0x17e0
sub_["rdx"]["rbp"] = 0x17e4
sub_["rdx"]["rsp"] = 0x17e8
gendict(sub_, "addrrax")
sub_["addrrax"]["rdx"] = 0x17ec
sub_["rdx"]["addrrax"] = 0x17f0
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rdx"] = 0x17f4
sub_["rdx"]["addrrbx"] = 0x17f8
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rdx"] = 0x17fc
sub_["rdx"]["addrrcx"] = 0x1800
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rdx"] = 0x1804
sub_["rdx"]["addrrdx"] = 0x1808
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rdx"] = 0x180c
sub_["rdx"]["addrrsi"] = 0x1810
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rdx"] = 0x1814
sub_["rdx"]["addrrdi"] = 0x1818
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rdx"] = 0x181c
sub_["rdx"]["addrrbp"] = 0x1821
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rdx"] = 0x1826
sub_["rdx"]["addrrsp"] = 0x182b
gendict(sub_, "rsi")
sub_["rsi"]["rax"] = 0x1830
sub_["rsi"]["rbx"] = 0x1834
sub_["rsi"]["rcx"] = 0x1838
sub_["rsi"]["rdx"] = 0x183c
sub_["rsi"]["rdi"] = 0x1840
sub_["rsi"]["rbp"] = 0x1844
sub_["rsi"]["rsp"] = 0x1848
gendict(sub_, "addrrax")
sub_["addrrax"]["rsi"] = 0x184c
sub_["rsi"]["addrrax"] = 0x1850
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rsi"] = 0x1854
sub_["rsi"]["addrrbx"] = 0x1858
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rsi"] = 0x185c
sub_["rsi"]["addrrcx"] = 0x1860
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rsi"] = 0x1864
sub_["rsi"]["addrrdx"] = 0x1868
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rsi"] = 0x186c
sub_["rsi"]["addrrsi"] = 0x1870
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rsi"] = 0x1874
sub_["rsi"]["addrrdi"] = 0x1878
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rsi"] = 0x187c
sub_["rsi"]["addrrbp"] = 0x1881
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rsi"] = 0x1886
sub_["rsi"]["addrrsp"] = 0x188b
gendict(sub_, "rdi")
sub_["rdi"]["rax"] = 0x1890
sub_["rdi"]["rbx"] = 0x1894
sub_["rdi"]["rcx"] = 0x1898
sub_["rdi"]["rdx"] = 0x189c
sub_["rdi"]["rsi"] = 0x18a0
sub_["rdi"]["rbp"] = 0x18a4
sub_["rdi"]["rsp"] = 0x18a8
gendict(sub_, "addrrax")
sub_["addrrax"]["rdi"] = 0x18ac
sub_["rdi"]["addrrax"] = 0x18b0
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rdi"] = 0x18b4
sub_["rdi"]["addrrbx"] = 0x18b8
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rdi"] = 0x18bc
sub_["rdi"]["addrrcx"] = 0x18c0
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rdi"] = 0x18c4
sub_["rdi"]["addrrdx"] = 0x18c8
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rdi"] = 0x18cc
sub_["rdi"]["addrrsi"] = 0x18d0
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rdi"] = 0x18d4
sub_["rdi"]["addrrdi"] = 0x18d8
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rdi"] = 0x18dc
sub_["rdi"]["addrrbp"] = 0x18e1
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rdi"] = 0x18e6
sub_["rdi"]["addrrsp"] = 0x18eb
gendict(sub_, "rbp")
sub_["rbp"]["rax"] = 0x18f0
sub_["rbp"]["rbx"] = 0x18f4
sub_["rbp"]["rcx"] = 0x18f8
sub_["rbp"]["rdx"] = 0x18fc
sub_["rbp"]["rsi"] = 0x1900
sub_["rbp"]["rdi"] = 0x1904
sub_["rbp"]["rsp"] = 0x1908
gendict(sub_, "addrrax")
sub_["addrrax"]["rbp"] = 0x190c
sub_["rbp"]["addrrax"] = 0x1910
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rbp"] = 0x1914
sub_["rbp"]["addrrbx"] = 0x1918
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rbp"] = 0x191c
sub_["rbp"]["addrrcx"] = 0x1920
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rbp"] = 0x1924
sub_["rbp"]["addrrdx"] = 0x1928
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rbp"] = 0x192c
sub_["rbp"]["addrrsi"] = 0x1930
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rbp"] = 0x1934
sub_["rbp"]["addrrdi"] = 0x1938
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rbp"] = 0x193c
sub_["rbp"]["addrrbp"] = 0x1941
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rbp"] = 0x1946
sub_["rbp"]["addrrsp"] = 0x194b
gendict(sub_, "rsp")
sub_["rsp"]["rax"] = 0x1950
sub_["rsp"]["rbx"] = 0x1954
sub_["rsp"]["rcx"] = 0x1958
sub_["rsp"]["rdx"] = 0x195c
sub_["rsp"]["rsi"] = 0x1960
sub_["rsp"]["rdi"] = 0x1964
sub_["rsp"]["rbp"] = 0x1968
gendict(sub_, "addrrax")
sub_["addrrax"]["rsp"] = 0x196c
sub_["rsp"]["addrrax"] = 0x1970
gendict(sub_, "addrrbx")
sub_["addrrbx"]["rsp"] = 0x1974
sub_["rsp"]["addrrbx"] = 0x1978
gendict(sub_, "addrrcx")
sub_["addrrcx"]["rsp"] = 0x197c
sub_["rsp"]["addrrcx"] = 0x1980
gendict(sub_, "addrrdx")
sub_["addrrdx"]["rsp"] = 0x1984
sub_["rsp"]["addrrdx"] = 0x1988
gendict(sub_, "addrrsi")
sub_["addrrsi"]["rsp"] = 0x198c
sub_["rsp"]["addrrsi"] = 0x1990
gendict(sub_, "addrrdi")
sub_["addrrdi"]["rsp"] = 0x1994
sub_["rsp"]["addrrdi"] = 0x1998
gendict(sub_, "addrrbp")
sub_["addrrbp"]["rsp"] = 0x199c
sub_["rsp"]["addrrbp"] = 0x19a1
gendict(sub_, "addrrsp")
sub_["addrrsp"]["rsp"] = 0x19a6
sub_["rsp"]["addrrsp"] = 0x19ab
gendict(sub_, "eax")
sub_["eax"]["ebx"] = 0x19b0
sub_["eax"]["ecx"] = 0x19b3
sub_["eax"]["edx"] = 0x19b6
sub_["eax"]["esi"] = 0x19b9
sub_["eax"]["edi"] = 0x19bc
sub_["eax"]["ebp"] = 0x19bf
sub_["eax"]["esp"] = 0x19c2
gendict(sub_, "addrrax")
sub_["addrrax"]["eax"] = 0x19c5
sub_["eax"]["addrrax"] = 0x19c8
gendict(sub_, "addrrbx")
sub_["addrrbx"]["eax"] = 0x19cb
sub_["eax"]["addrrbx"] = 0x19ce
gendict(sub_, "addrrcx")
sub_["addrrcx"]["eax"] = 0x19d1
sub_["eax"]["addrrcx"] = 0x19d4
gendict(sub_, "addrrdx")
sub_["addrrdx"]["eax"] = 0x19d7
sub_["eax"]["addrrdx"] = 0x19da
gendict(sub_, "addrrsi")
sub_["addrrsi"]["eax"] = 0x19dd
sub_["eax"]["addrrsi"] = 0x19e0
gendict(sub_, "addrrdi")
sub_["addrrdi"]["eax"] = 0x19e3
sub_["eax"]["addrrdi"] = 0x19e6
gendict(sub_, "addrrbp")
sub_["addrrbp"]["eax"] = 0x19e9
sub_["eax"]["addrrbp"] = 0x19ed
gendict(sub_, "addrrsp")
sub_["addrrsp"]["eax"] = 0x19f1
sub_["eax"]["addrrsp"] = 0x19f5
gendict(sub_, "ebx")
sub_["ebx"]["eax"] = 0x19f9
sub_["ebx"]["ecx"] = 0x19fc
sub_["ebx"]["edx"] = 0x19ff
sub_["ebx"]["esi"] = 0x1a02
sub_["ebx"]["edi"] = 0x1a05
sub_["ebx"]["ebp"] = 0x1a08
sub_["ebx"]["esp"] = 0x1a0b
gendict(sub_, "addrrax")
sub_["addrrax"]["ebx"] = 0x1a0e
sub_["ebx"]["addrrax"] = 0x1a11
gendict(sub_, "addrrbx")
sub_["addrrbx"]["ebx"] = 0x1a14
sub_["ebx"]["addrrbx"] = 0x1a17
gendict(sub_, "addrrcx")
sub_["addrrcx"]["ebx"] = 0x1a1a
sub_["ebx"]["addrrcx"] = 0x1a1d
gendict(sub_, "addrrdx")
sub_["addrrdx"]["ebx"] = 0x1a20
sub_["ebx"]["addrrdx"] = 0x1a23
gendict(sub_, "addrrsi")
sub_["addrrsi"]["ebx"] = 0x1a26
sub_["ebx"]["addrrsi"] = 0x1a29
gendict(sub_, "addrrdi")
sub_["addrrdi"]["ebx"] = 0x1a2c
sub_["ebx"]["addrrdi"] = 0x1a2f
gendict(sub_, "addrrbp")
sub_["addrrbp"]["ebx"] = 0x1a32
sub_["ebx"]["addrrbp"] = 0x1a36
gendict(sub_, "addrrsp")
sub_["addrrsp"]["ebx"] = 0x1a3a
sub_["ebx"]["addrrsp"] = 0x1a3e
gendict(sub_, "ecx")
sub_["ecx"]["eax"] = 0x1a42
sub_["ecx"]["ebx"] = 0x1a45
sub_["ecx"]["edx"] = 0x1a48
sub_["ecx"]["esi"] = 0x1a4b
sub_["ecx"]["edi"] = 0x1a4e
sub_["ecx"]["ebp"] = 0x1a51
sub_["ecx"]["esp"] = 0x1a54
gendict(sub_, "addrrax")
sub_["addrrax"]["ecx"] = 0x1a57
sub_["ecx"]["addrrax"] = 0x1a5a
gendict(sub_, "addrrbx")
sub_["addrrbx"]["ecx"] = 0x1a5d
sub_["ecx"]["addrrbx"] = 0x1a60
gendict(sub_, "addrrcx")
sub_["addrrcx"]["ecx"] = 0x1a63
sub_["ecx"]["addrrcx"] = 0x1a66
gendict(sub_, "addrrdx")
sub_["addrrdx"]["ecx"] = 0x1a69
sub_["ecx"]["addrrdx"] = 0x1a6c
gendict(sub_, "addrrsi")
sub_["addrrsi"]["ecx"] = 0x1a6f
sub_["ecx"]["addrrsi"] = 0x1a72
gendict(sub_, "addrrdi")
sub_["addrrdi"]["ecx"] = 0x1a75
sub_["ecx"]["addrrdi"] = 0x1a78
gendict(sub_, "addrrbp")
sub_["addrrbp"]["ecx"] = 0x1a7b
sub_["ecx"]["addrrbp"] = 0x1a7f
gendict(sub_, "addrrsp")
sub_["addrrsp"]["ecx"] = 0x1a83
sub_["ecx"]["addrrsp"] = 0x1a87
gendict(sub_, "edx")
sub_["edx"]["eax"] = 0x1a8b
sub_["edx"]["ebx"] = 0x1a8e
sub_["edx"]["ecx"] = 0x1a91
sub_["edx"]["esi"] = 0x1a94
sub_["edx"]["edi"] = 0x1a97
sub_["edx"]["ebp"] = 0x1a9a
sub_["edx"]["esp"] = 0x1a9d
gendict(sub_, "addrrax")
sub_["addrrax"]["edx"] = 0x1aa0
sub_["edx"]["addrrax"] = 0x1aa3
gendict(sub_, "addrrbx")
sub_["addrrbx"]["edx"] = 0x1aa6
sub_["edx"]["addrrbx"] = 0x1aa9
gendict(sub_, "addrrcx")
sub_["addrrcx"]["edx"] = 0x1aac
sub_["edx"]["addrrcx"] = 0x1aaf
gendict(sub_, "addrrdx")
sub_["addrrdx"]["edx"] = 0x1ab2
sub_["edx"]["addrrdx"] = 0x1ab5
gendict(sub_, "addrrsi")
sub_["addrrsi"]["edx"] = 0x1ab8
sub_["edx"]["addrrsi"] = 0x1abb
gendict(sub_, "addrrdi")
sub_["addrrdi"]["edx"] = 0x1abe
sub_["edx"]["addrrdi"] = 0x1ac1
gendict(sub_, "addrrbp")
sub_["addrrbp"]["edx"] = 0x1ac4
sub_["edx"]["addrrbp"] = 0x1ac8
gendict(sub_, "addrrsp")
sub_["addrrsp"]["edx"] = 0x1acc
sub_["edx"]["addrrsp"] = 0x1ad0
gendict(sub_, "esi")
sub_["esi"]["eax"] = 0x1ad4
sub_["esi"]["ebx"] = 0x1ad7
sub_["esi"]["ecx"] = 0x1ada
sub_["esi"]["edx"] = 0x1add
sub_["esi"]["edi"] = 0x1ae0
sub_["esi"]["ebp"] = 0x1ae3
sub_["esi"]["esp"] = 0x1ae6
gendict(sub_, "addrrax")
sub_["addrrax"]["esi"] = 0x1ae9
sub_["esi"]["addrrax"] = 0x1aec
gendict(sub_, "addrrbx")
sub_["addrrbx"]["esi"] = 0x1aef
sub_["esi"]["addrrbx"] = 0x1af2
gendict(sub_, "addrrcx")
sub_["addrrcx"]["esi"] = 0x1af5
sub_["esi"]["addrrcx"] = 0x1af8
gendict(sub_, "addrrdx")
sub_["addrrdx"]["esi"] = 0x1afb
sub_["esi"]["addrrdx"] = 0x1afe
gendict(sub_, "addrrsi")
sub_["addrrsi"]["esi"] = 0x1b01
sub_["esi"]["addrrsi"] = 0x1b04
gendict(sub_, "addrrdi")
sub_["addrrdi"]["esi"] = 0x1b07
sub_["esi"]["addrrdi"] = 0x1b0a
gendict(sub_, "addrrbp")
sub_["addrrbp"]["esi"] = 0x1b0d
sub_["esi"]["addrrbp"] = 0x1b11
gendict(sub_, "addrrsp")
sub_["addrrsp"]["esi"] = 0x1b15
sub_["esi"]["addrrsp"] = 0x1b19
gendict(sub_, "edi")
sub_["edi"]["eax"] = 0x1b1d
sub_["edi"]["ebx"] = 0x1b20
sub_["edi"]["ecx"] = 0x1b23
sub_["edi"]["edx"] = 0x1b26
sub_["edi"]["esi"] = 0x1b29
sub_["edi"]["ebp"] = 0x1b2c
sub_["edi"]["esp"] = 0x1b2f
gendict(sub_, "addrrax")
sub_["addrrax"]["edi"] = 0x1b32
sub_["edi"]["addrrax"] = 0x1b35
gendict(sub_, "addrrbx")
sub_["addrrbx"]["edi"] = 0x1b38
sub_["edi"]["addrrbx"] = 0x1b3b
gendict(sub_, "addrrcx")
sub_["addrrcx"]["edi"] = 0x1b3e
sub_["edi"]["addrrcx"] = 0x1b41
gendict(sub_, "addrrdx")
sub_["addrrdx"]["edi"] = 0x1b44
sub_["edi"]["addrrdx"] = 0x1b47
gendict(sub_, "addrrsi")
sub_["addrrsi"]["edi"] = 0x1b4a
sub_["edi"]["addrrsi"] = 0x1b4d
gendict(sub_, "addrrdi")
sub_["addrrdi"]["edi"] = 0x1b50
sub_["edi"]["addrrdi"] = 0x1b53
gendict(sub_, "addrrbp")
sub_["addrrbp"]["edi"] = 0x1b56
sub_["edi"]["addrrbp"] = 0x1b5a
gendict(sub_, "addrrsp")
sub_["addrrsp"]["edi"] = 0x1b5e
sub_["edi"]["addrrsp"] = 0x1b62
gendict(sub_, "ebp")
sub_["ebp"]["eax"] = 0x1b66
sub_["ebp"]["ebx"] = 0x1b69
sub_["ebp"]["ecx"] = 0x1b6c
sub_["ebp"]["edx"] = 0x1b6f
sub_["ebp"]["esi"] = 0x1b72
sub_["ebp"]["edi"] = 0x1b75
sub_["ebp"]["esp"] = 0x1b78
gendict(sub_, "addrrax")
sub_["addrrax"]["ebp"] = 0x1b7b
sub_["ebp"]["addrrax"] = 0x1b7e
gendict(sub_, "addrrbx")
sub_["addrrbx"]["ebp"] = 0x1b81
sub_["ebp"]["addrrbx"] = 0x1b84
gendict(sub_, "addrrcx")
sub_["addrrcx"]["ebp"] = 0x1b87
sub_["ebp"]["addrrcx"] = 0x1b8a
gendict(sub_, "addrrdx")
sub_["addrrdx"]["ebp"] = 0x1b8d
sub_["ebp"]["addrrdx"] = 0x1b90
gendict(sub_, "addrrsi")
sub_["addrrsi"]["ebp"] = 0x1b93
sub_["ebp"]["addrrsi"] = 0x1b96
gendict(sub_, "addrrdi")
sub_["addrrdi"]["ebp"] = 0x1b99
sub_["ebp"]["addrrdi"] = 0x1b9c
gendict(sub_, "addrrbp")
sub_["addrrbp"]["ebp"] = 0x1b9f
sub_["ebp"]["addrrbp"] = 0x1ba3
gendict(sub_, "addrrsp")
sub_["addrrsp"]["ebp"] = 0x1ba7
sub_["ebp"]["addrrsp"] = 0x1bab
gendict(sub_, "esp")
sub_["esp"]["eax"] = 0x1baf
sub_["esp"]["ebx"] = 0x1bb2
sub_["esp"]["ecx"] = 0x1bb5
sub_["esp"]["edx"] = 0x1bb8
sub_["esp"]["esi"] = 0x1bbb
sub_["esp"]["edi"] = 0x1bbe
sub_["esp"]["ebp"] = 0x1bc1
gendict(sub_, "addrrax")
sub_["addrrax"]["esp"] = 0x1bc4
sub_["esp"]["addrrax"] = 0x1bc7
gendict(sub_, "addrrbx")
sub_["addrrbx"]["esp"] = 0x1bca
sub_["esp"]["addrrbx"] = 0x1bcd
gendict(sub_, "addrrcx")
sub_["addrrcx"]["esp"] = 0x1bd0
sub_["esp"]["addrrcx"] = 0x1bd3
gendict(sub_, "addrrdx")
sub_["addrrdx"]["esp"] = 0x1bd6
sub_["esp"]["addrrdx"] = 0x1bd9
gendict(sub_, "addrrsi")
sub_["addrrsi"]["esp"] = 0x1bdc
sub_["esp"]["addrrsi"] = 0x1bdf
gendict(sub_, "addrrdi")
sub_["addrrdi"]["esp"] = 0x1be2
sub_["esp"]["addrrdi"] = 0x1be5
gendict(sub_, "addrrbp")
sub_["addrrbp"]["esp"] = 0x1be8
sub_["esp"]["addrrbp"] = 0x1bec
gendict(sub_, "addrrsp")
sub_["addrrsp"]["esp"] = 0x1bf0
sub_["esp"]["addrrsp"] = 0x1bf4
gendict(sub_, "ax")
sub_["ax"]["bx"] = 0x1bf8
sub_["ax"]["cx"] = 0x1bfc
sub_["ax"]["dx"] = 0x1c00
sub_["ax"]["si"] = 0x1c04
sub_["ax"]["di"] = 0x1c08
sub_["ax"]["bp"] = 0x1c0c
sub_["ax"]["sp"] = 0x1c10
gendict(sub_, "addrrax")
sub_["addrrax"]["ax"] = 0x1c14
sub_["ax"]["addrrax"] = 0x1c18
gendict(sub_, "addrrbx")
sub_["addrrbx"]["ax"] = 0x1c1c
sub_["ax"]["addrrbx"] = 0x1c20
gendict(sub_, "addrrcx")
sub_["addrrcx"]["ax"] = 0x1c24
sub_["ax"]["addrrcx"] = 0x1c28
gendict(sub_, "addrrdx")
sub_["addrrdx"]["ax"] = 0x1c2c
sub_["ax"]["addrrdx"] = 0x1c30
gendict(sub_, "addrrsi")
sub_["addrrsi"]["ax"] = 0x1c34
sub_["ax"]["addrrsi"] = 0x1c38
gendict(sub_, "addrrdi")
sub_["addrrdi"]["ax"] = 0x1c3c
sub_["ax"]["addrrdi"] = 0x1c40
gendict(sub_, "addrrbp")
sub_["addrrbp"]["ax"] = 0x1c44
sub_["ax"]["addrrbp"] = 0x1c49
gendict(sub_, "addrrsp")
sub_["addrrsp"]["ax"] = 0x1c4e
sub_["ax"]["addrrsp"] = 0x1c53
gendict(sub_, "bx")
sub_["bx"]["ax"] = 0x1c58
sub_["bx"]["cx"] = 0x1c5c
sub_["bx"]["dx"] = 0x1c60
sub_["bx"]["si"] = 0x1c64
sub_["bx"]["di"] = 0x1c68
sub_["bx"]["bp"] = 0x1c6c
sub_["bx"]["sp"] = 0x1c70
gendict(sub_, "addrrax")
sub_["addrrax"]["bx"] = 0x1c74
sub_["bx"]["addrrax"] = 0x1c78
gendict(sub_, "addrrbx")
sub_["addrrbx"]["bx"] = 0x1c7c
sub_["bx"]["addrrbx"] = 0x1c80
gendict(sub_, "addrrcx")
sub_["addrrcx"]["bx"] = 0x1c84
sub_["bx"]["addrrcx"] = 0x1c88
gendict(sub_, "addrrdx")
sub_["addrrdx"]["bx"] = 0x1c8c
sub_["bx"]["addrrdx"] = 0x1c90
gendict(sub_, "addrrsi")
sub_["addrrsi"]["bx"] = 0x1c94
sub_["bx"]["addrrsi"] = 0x1c98
gendict(sub_, "addrrdi")
sub_["addrrdi"]["bx"] = 0x1c9c
sub_["bx"]["addrrdi"] = 0x1ca0
gendict(sub_, "addrrbp")
sub_["addrrbp"]["bx"] = 0x1ca4
sub_["bx"]["addrrbp"] = 0x1ca9
gendict(sub_, "addrrsp")
sub_["addrrsp"]["bx"] = 0x1cae
sub_["bx"]["addrrsp"] = 0x1cb3
gendict(sub_, "cx")
sub_["cx"]["ax"] = 0x1cb8
sub_["cx"]["bx"] = 0x1cbc
sub_["cx"]["dx"] = 0x1cc0
sub_["cx"]["si"] = 0x1cc4
sub_["cx"]["di"] = 0x1cc8
sub_["cx"]["bp"] = 0x1ccc
sub_["cx"]["sp"] = 0x1cd0
gendict(sub_, "addrrax")
sub_["addrrax"]["cx"] = 0x1cd4
sub_["cx"]["addrrax"] = 0x1cd8
gendict(sub_, "addrrbx")
sub_["addrrbx"]["cx"] = 0x1cdc
sub_["cx"]["addrrbx"] = 0x1ce0
gendict(sub_, "addrrcx")
sub_["addrrcx"]["cx"] = 0x1ce4
sub_["cx"]["addrrcx"] = 0x1ce8
gendict(sub_, "addrrdx")
sub_["addrrdx"]["cx"] = 0x1cec
sub_["cx"]["addrrdx"] = 0x1cf0
gendict(sub_, "addrrsi")
sub_["addrrsi"]["cx"] = 0x1cf4
sub_["cx"]["addrrsi"] = 0x1cf8
gendict(sub_, "addrrdi")
sub_["addrrdi"]["cx"] = 0x1cfc
sub_["cx"]["addrrdi"] = 0x1d00
gendict(sub_, "addrrbp")
sub_["addrrbp"]["cx"] = 0x1d04
sub_["cx"]["addrrbp"] = 0x1d09
gendict(sub_, "addrrsp")
sub_["addrrsp"]["cx"] = 0x1d0e
sub_["cx"]["addrrsp"] = 0x1d13
gendict(sub_, "dx")
sub_["dx"]["ax"] = 0x1d18
sub_["dx"]["bx"] = 0x1d1c
sub_["dx"]["cx"] = 0x1d20
sub_["dx"]["si"] = 0x1d24
sub_["dx"]["di"] = 0x1d28
sub_["dx"]["bp"] = 0x1d2c
sub_["dx"]["sp"] = 0x1d30
gendict(sub_, "addrrax")
sub_["addrrax"]["dx"] = 0x1d34
sub_["dx"]["addrrax"] = 0x1d38
gendict(sub_, "addrrbx")
sub_["addrrbx"]["dx"] = 0x1d3c
sub_["dx"]["addrrbx"] = 0x1d40
gendict(sub_, "addrrcx")
sub_["addrrcx"]["dx"] = 0x1d44
sub_["dx"]["addrrcx"] = 0x1d48
gendict(sub_, "addrrdx")
sub_["addrrdx"]["dx"] = 0x1d4c
sub_["dx"]["addrrdx"] = 0x1d50
gendict(sub_, "addrrsi")
sub_["addrrsi"]["dx"] = 0x1d54
sub_["dx"]["addrrsi"] = 0x1d58
gendict(sub_, "addrrdi")
sub_["addrrdi"]["dx"] = 0x1d5c
sub_["dx"]["addrrdi"] = 0x1d60
gendict(sub_, "addrrbp")
sub_["addrrbp"]["dx"] = 0x1d64
sub_["dx"]["addrrbp"] = 0x1d69
gendict(sub_, "addrrsp")
sub_["addrrsp"]["dx"] = 0x1d6e
sub_["dx"]["addrrsp"] = 0x1d73
gendict(sub_, "si")
sub_["si"]["ax"] = 0x1d78
sub_["si"]["bx"] = 0x1d7c
sub_["si"]["cx"] = 0x1d80
sub_["si"]["dx"] = 0x1d84
sub_["si"]["di"] = 0x1d88
sub_["si"]["bp"] = 0x1d8c
sub_["si"]["sp"] = 0x1d90
gendict(sub_, "addrrax")
sub_["addrrax"]["si"] = 0x1d94
sub_["si"]["addrrax"] = 0x1d98
gendict(sub_, "addrrbx")
sub_["addrrbx"]["si"] = 0x1d9c
sub_["si"]["addrrbx"] = 0x1da0
gendict(sub_, "addrrcx")
sub_["addrrcx"]["si"] = 0x1da4
sub_["si"]["addrrcx"] = 0x1da8
gendict(sub_, "addrrdx")
sub_["addrrdx"]["si"] = 0x1dac
sub_["si"]["addrrdx"] = 0x1db0
gendict(sub_, "addrrsi")
sub_["addrrsi"]["si"] = 0x1db4
sub_["si"]["addrrsi"] = 0x1db8
gendict(sub_, "addrrdi")
sub_["addrrdi"]["si"] = 0x1dbc
sub_["si"]["addrrdi"] = 0x1dc0
gendict(sub_, "addrrbp")
sub_["addrrbp"]["si"] = 0x1dc4
sub_["si"]["addrrbp"] = 0x1dc9
gendict(sub_, "addrrsp")
sub_["addrrsp"]["si"] = 0x1dce
sub_["si"]["addrrsp"] = 0x1dd3
gendict(sub_, "di")
sub_["di"]["ax"] = 0x1dd8
sub_["di"]["bx"] = 0x1ddc
sub_["di"]["cx"] = 0x1de0
sub_["di"]["dx"] = 0x1de4
sub_["di"]["si"] = 0x1de8
sub_["di"]["bp"] = 0x1dec
sub_["di"]["sp"] = 0x1df0
gendict(sub_, "addrrax")
sub_["addrrax"]["di"] = 0x1df4
sub_["di"]["addrrax"] = 0x1df8
gendict(sub_, "addrrbx")
sub_["addrrbx"]["di"] = 0x1dfc
sub_["di"]["addrrbx"] = 0x1e00
gendict(sub_, "addrrcx")
sub_["addrrcx"]["di"] = 0x1e04
sub_["di"]["addrrcx"] = 0x1e08
gendict(sub_, "addrrdx")
sub_["addrrdx"]["di"] = 0x1e0c
sub_["di"]["addrrdx"] = 0x1e10
gendict(sub_, "addrrsi")
sub_["addrrsi"]["di"] = 0x1e14
sub_["di"]["addrrsi"] = 0x1e18
gendict(sub_, "addrrdi")
sub_["addrrdi"]["di"] = 0x1e1c
sub_["di"]["addrrdi"] = 0x1e20
gendict(sub_, "addrrbp")
sub_["addrrbp"]["di"] = 0x1e24
sub_["di"]["addrrbp"] = 0x1e29
gendict(sub_, "addrrsp")
sub_["addrrsp"]["di"] = 0x1e2e
sub_["di"]["addrrsp"] = 0x1e33
gendict(sub_, "bp")
sub_["bp"]["ax"] = 0x1e38
sub_["bp"]["bx"] = 0x1e3c
sub_["bp"]["cx"] = 0x1e40
sub_["bp"]["dx"] = 0x1e44
sub_["bp"]["si"] = 0x1e48
sub_["bp"]["di"] = 0x1e4c
sub_["bp"]["sp"] = 0x1e50
gendict(sub_, "addrrax")
sub_["addrrax"]["bp"] = 0x1e54
sub_["bp"]["addrrax"] = 0x1e58
gendict(sub_, "addrrbx")
sub_["addrrbx"]["bp"] = 0x1e5c
sub_["bp"]["addrrbx"] = 0x1e60
gendict(sub_, "addrrcx")
sub_["addrrcx"]["bp"] = 0x1e64
sub_["bp"]["addrrcx"] = 0x1e68
gendict(sub_, "addrrdx")
sub_["addrrdx"]["bp"] = 0x1e6c
sub_["bp"]["addrrdx"] = 0x1e70
gendict(sub_, "addrrsi")
sub_["addrrsi"]["bp"] = 0x1e74
sub_["bp"]["addrrsi"] = 0x1e78
gendict(sub_, "addrrdi")
sub_["addrrdi"]["bp"] = 0x1e7c
sub_["bp"]["addrrdi"] = 0x1e80
gendict(sub_, "addrrbp")
sub_["addrrbp"]["bp"] = 0x1e84
sub_["bp"]["addrrbp"] = 0x1e89
gendict(sub_, "addrrsp")
sub_["addrrsp"]["bp"] = 0x1e8e
sub_["bp"]["addrrsp"] = 0x1e93
gendict(sub_, "sp")
sub_["sp"]["ax"] = 0x1e98
sub_["sp"]["bx"] = 0x1e9c
sub_["sp"]["cx"] = 0x1ea0
sub_["sp"]["dx"] = 0x1ea4
sub_["sp"]["si"] = 0x1ea8
sub_["sp"]["di"] = 0x1eac
sub_["sp"]["bp"] = 0x1eb0
gendict(sub_, "addrrax")
sub_["addrrax"]["sp"] = 0x1eb4
sub_["sp"]["addrrax"] = 0x1eb8
gendict(sub_, "addrrbx")
sub_["addrrbx"]["sp"] = 0x1ebc
sub_["sp"]["addrrbx"] = 0x1ec0
gendict(sub_, "addrrcx")
sub_["addrrcx"]["sp"] = 0x1ec4
sub_["sp"]["addrrcx"] = 0x1ec8
gendict(sub_, "addrrdx")
sub_["addrrdx"]["sp"] = 0x1ecc
sub_["sp"]["addrrdx"] = 0x1ed0
gendict(sub_, "addrrsi")
sub_["addrrsi"]["sp"] = 0x1ed4
sub_["sp"]["addrrsi"] = 0x1ed8
gendict(sub_, "addrrdi")
sub_["addrrdi"]["sp"] = 0x1edc
sub_["sp"]["addrrdi"] = 0x1ee0
gendict(sub_, "addrrbp")
sub_["addrrbp"]["sp"] = 0x1ee4
sub_["sp"]["addrrbp"] = 0x1ee9
gendict(sub_, "addrrsp")
sub_["addrrsp"]["sp"] = 0x1eee
sub_["sp"]["addrrsp"] = 0x1ef3
gendict(sub_, "ah")
sub_["ah"]["bh"] = 0x1ef8
sub_["ah"]["ch"] = 0x1efb
sub_["ah"]["dh"] = 0x1efe
gendict(sub_, "addrrax")
sub_["addrrax"]["ah"] = 0x1f01
sub_["ah"]["addrrax"] = 0x1f04
gendict(sub_, "addrrbx")
sub_["addrrbx"]["ah"] = 0x1f07
sub_["ah"]["addrrbx"] = 0x1f0a
gendict(sub_, "addrrcx")
sub_["addrrcx"]["ah"] = 0x1f0d
sub_["ah"]["addrrcx"] = 0x1f10
gendict(sub_, "addrrdx")
sub_["addrrdx"]["ah"] = 0x1f13
sub_["ah"]["addrrdx"] = 0x1f16
gendict(sub_, "addrrsi")
sub_["addrrsi"]["ah"] = 0x1f19
sub_["ah"]["addrrsi"] = 0x1f1c
gendict(sub_, "addrrdi")
sub_["addrrdi"]["ah"] = 0x1f1f
sub_["ah"]["addrrdi"] = 0x1f22
gendict(sub_, "addrrbp")
sub_["addrrbp"]["ah"] = 0x1f25
sub_["ah"]["addrrbp"] = 0x1f29
gendict(sub_, "addrrsp")
sub_["addrrsp"]["ah"] = 0x1f2d
sub_["ah"]["addrrsp"] = 0x1f31
gendict(sub_, "bh")
sub_["bh"]["ah"] = 0x1f35
sub_["bh"]["ch"] = 0x1f38
sub_["bh"]["dh"] = 0x1f3b
gendict(sub_, "addrrax")
sub_["addrrax"]["bh"] = 0x1f3e
sub_["bh"]["addrrax"] = 0x1f41
gendict(sub_, "addrrbx")
sub_["addrrbx"]["bh"] = 0x1f44
sub_["bh"]["addrrbx"] = 0x1f47
gendict(sub_, "addrrcx")
sub_["addrrcx"]["bh"] = 0x1f4a
sub_["bh"]["addrrcx"] = 0x1f4d
gendict(sub_, "addrrdx")
sub_["addrrdx"]["bh"] = 0x1f50
sub_["bh"]["addrrdx"] = 0x1f53
gendict(sub_, "addrrsi")
sub_["addrrsi"]["bh"] = 0x1f56
sub_["bh"]["addrrsi"] = 0x1f59
gendict(sub_, "addrrdi")
sub_["addrrdi"]["bh"] = 0x1f5c
sub_["bh"]["addrrdi"] = 0x1f5f
gendict(sub_, "addrrbp")
sub_["addrrbp"]["bh"] = 0x1f62
sub_["bh"]["addrrbp"] = 0x1f66
gendict(sub_, "addrrsp")
sub_["addrrsp"]["bh"] = 0x1f6a
sub_["bh"]["addrrsp"] = 0x1f6e
gendict(sub_, "ch")
sub_["ch"]["ah"] = 0x1f72
sub_["ch"]["bh"] = 0x1f75
sub_["ch"]["dh"] = 0x1f78
gendict(sub_, "addrrax")
sub_["addrrax"]["ch"] = 0x1f7b
sub_["ch"]["addrrax"] = 0x1f7e
gendict(sub_, "addrrbx")
sub_["addrrbx"]["ch"] = 0x1f81
sub_["ch"]["addrrbx"] = 0x1f84
gendict(sub_, "addrrcx")
sub_["addrrcx"]["ch"] = 0x1f87
sub_["ch"]["addrrcx"] = 0x1f8a
gendict(sub_, "addrrdx")
sub_["addrrdx"]["ch"] = 0x1f8d
sub_["ch"]["addrrdx"] = 0x1f90
gendict(sub_, "addrrsi")
sub_["addrrsi"]["ch"] = 0x1f93
sub_["ch"]["addrrsi"] = 0x1f96
gendict(sub_, "addrrdi")
sub_["addrrdi"]["ch"] = 0x1f99
sub_["ch"]["addrrdi"] = 0x1f9c
gendict(sub_, "addrrbp")
sub_["addrrbp"]["ch"] = 0x1f9f
sub_["ch"]["addrrbp"] = 0x1fa3
gendict(sub_, "addrrsp")
sub_["addrrsp"]["ch"] = 0x1fa7
sub_["ch"]["addrrsp"] = 0x1fab
gendict(sub_, "dh")
sub_["dh"]["ah"] = 0x1faf
sub_["dh"]["bh"] = 0x1fb2
sub_["dh"]["ch"] = 0x1fb5
gendict(sub_, "addrrax")
sub_["addrrax"]["dh"] = 0x1fb8
sub_["dh"]["addrrax"] = 0x1fbb
gendict(sub_, "addrrbx")
sub_["addrrbx"]["dh"] = 0x1fbe
sub_["dh"]["addrrbx"] = 0x1fc1
gendict(sub_, "addrrcx")
sub_["addrrcx"]["dh"] = 0x1fc4
sub_["dh"]["addrrcx"] = 0x1fc7
gendict(sub_, "addrrdx")
sub_["addrrdx"]["dh"] = 0x1fca
sub_["dh"]["addrrdx"] = 0x1fcd
gendict(sub_, "addrrsi")
sub_["addrrsi"]["dh"] = 0x1fd0
sub_["dh"]["addrrsi"] = 0x1fd3
gendict(sub_, "addrrdi")
sub_["addrrdi"]["dh"] = 0x1fd6
sub_["dh"]["addrrdi"] = 0x1fd9
gendict(sub_, "addrrbp")
sub_["addrrbp"]["dh"] = 0x1fdc
sub_["dh"]["addrrbp"] = 0x1fe0
gendict(sub_, "addrrsp")
sub_["addrrsp"]["dh"] = 0x1fe4
sub_["dh"]["addrrsp"] = 0x1fe8
gendict(sub_, "al")
sub_["al"]["bl"] = 0x1fec
sub_["al"]["cl"] = 0x1fef
sub_["al"]["dl"] = 0x1ff2
gendict(sub_, "addrrax")
sub_["addrrax"]["al"] = 0x1ff5
sub_["al"]["addrrax"] = 0x1ff8
gendict(sub_, "addrrbx")
sub_["addrrbx"]["al"] = 0x1ffb
sub_["al"]["addrrbx"] = 0x1ffe
gendict(sub_, "addrrcx")
sub_["addrrcx"]["al"] = 0x2001
sub_["al"]["addrrcx"] = 0x2004
gendict(sub_, "addrrdx")
sub_["addrrdx"]["al"] = 0x2007
sub_["al"]["addrrdx"] = 0x200a
gendict(sub_, "addrrsi")
sub_["addrrsi"]["al"] = 0x200d
sub_["al"]["addrrsi"] = 0x2010
gendict(sub_, "addrrdi")
sub_["addrrdi"]["al"] = 0x2013
sub_["al"]["addrrdi"] = 0x2016
gendict(sub_, "addrrbp")
sub_["addrrbp"]["al"] = 0x2019
sub_["al"]["addrrbp"] = 0x201d
gendict(sub_, "addrrsp")
sub_["addrrsp"]["al"] = 0x2021
sub_["al"]["addrrsp"] = 0x2025
gendict(sub_, "bl")
sub_["bl"]["al"] = 0x2029
sub_["bl"]["cl"] = 0x202c
sub_["bl"]["dl"] = 0x202f
gendict(sub_, "addrrax")
sub_["addrrax"]["bl"] = 0x2032
sub_["bl"]["addrrax"] = 0x2035
gendict(sub_, "addrrbx")
sub_["addrrbx"]["bl"] = 0x2038
sub_["bl"]["addrrbx"] = 0x203b
gendict(sub_, "addrrcx")
sub_["addrrcx"]["bl"] = 0x203e
sub_["bl"]["addrrcx"] = 0x2041
gendict(sub_, "addrrdx")
sub_["addrrdx"]["bl"] = 0x2044
sub_["bl"]["addrrdx"] = 0x2047
gendict(sub_, "addrrsi")
sub_["addrrsi"]["bl"] = 0x204a
sub_["bl"]["addrrsi"] = 0x204d
gendict(sub_, "addrrdi")
sub_["addrrdi"]["bl"] = 0x2050
sub_["bl"]["addrrdi"] = 0x2053
gendict(sub_, "addrrbp")
sub_["addrrbp"]["bl"] = 0x2056
sub_["bl"]["addrrbp"] = 0x205a
gendict(sub_, "addrrsp")
sub_["addrrsp"]["bl"] = 0x205e
sub_["bl"]["addrrsp"] = 0x2062
gendict(sub_, "cl")
sub_["cl"]["al"] = 0x2066
sub_["cl"]["bl"] = 0x2069
sub_["cl"]["dl"] = 0x206c
gendict(sub_, "addrrax")
sub_["addrrax"]["cl"] = 0x206f
sub_["cl"]["addrrax"] = 0x2072
gendict(sub_, "addrrbx")
sub_["addrrbx"]["cl"] = 0x2075
sub_["cl"]["addrrbx"] = 0x2078
gendict(sub_, "addrrcx")
sub_["addrrcx"]["cl"] = 0x207b
sub_["cl"]["addrrcx"] = 0x207e
gendict(sub_, "addrrdx")
sub_["addrrdx"]["cl"] = 0x2081
sub_["cl"]["addrrdx"] = 0x2084
gendict(sub_, "addrrsi")
sub_["addrrsi"]["cl"] = 0x2087
sub_["cl"]["addrrsi"] = 0x208a
gendict(sub_, "addrrdi")
sub_["addrrdi"]["cl"] = 0x208d
sub_["cl"]["addrrdi"] = 0x2090
gendict(sub_, "addrrbp")
sub_["addrrbp"]["cl"] = 0x2093
sub_["cl"]["addrrbp"] = 0x2097
gendict(sub_, "addrrsp")
sub_["addrrsp"]["cl"] = 0x209b
sub_["cl"]["addrrsp"] = 0x209f
gendict(sub_, "dl")
sub_["dl"]["al"] = 0x20a3
sub_["dl"]["bl"] = 0x20a6
sub_["dl"]["cl"] = 0x20a9
gendict(sub_, "addrrax")
sub_["addrrax"]["dl"] = 0x20ac
sub_["dl"]["addrrax"] = 0x20af
gendict(sub_, "addrrbx")
sub_["addrrbx"]["dl"] = 0x20b2
sub_["dl"]["addrrbx"] = 0x20b5
gendict(sub_, "addrrcx")
sub_["addrrcx"]["dl"] = 0x20b8
sub_["dl"]["addrrcx"] = 0x20bb
gendict(sub_, "addrrdx")
sub_["addrrdx"]["dl"] = 0x20be
sub_["dl"]["addrrdx"] = 0x20c1
gendict(sub_, "addrrsi")
sub_["addrrsi"]["dl"] = 0x20c4
sub_["dl"]["addrrsi"] = 0x20c7
gendict(sub_, "addrrdi")
sub_["addrrdi"]["dl"] = 0x20ca
sub_["dl"]["addrrdi"] = 0x20cd
gendict(sub_, "addrrbp")
sub_["addrrbp"]["dl"] = 0x20d0
sub_["dl"]["addrrbp"] = 0x20d4
gendict(sub_, "addrrsp")
sub_["addrrsp"]["dl"] = 0x20d8
sub_["dl"]["addrrsp"] = 0x20dc
and_ = {}
gendict(and_, "rax")
and_["rax"]["rbx"] = 0x20e0
and_["rax"]["rcx"] = 0x20e4
and_["rax"]["rdx"] = 0x20e8
and_["rax"]["rsi"] = 0x20ec
and_["rax"]["rdi"] = 0x20f0
and_["rax"]["rbp"] = 0x20f4
and_["rax"]["rsp"] = 0x20f8
gendict(and_, "addrrax")
and_["addrrax"]["rax"] = 0x20fc
and_["rax"]["addrrax"] = 0x2100
gendict(and_, "addrrbx")
and_["addrrbx"]["rax"] = 0x2104
and_["rax"]["addrrbx"] = 0x2108
gendict(and_, "addrrcx")
and_["addrrcx"]["rax"] = 0x210c
and_["rax"]["addrrcx"] = 0x2110
gendict(and_, "addrrdx")
and_["addrrdx"]["rax"] = 0x2114
and_["rax"]["addrrdx"] = 0x2118
gendict(and_, "addrrsi")
and_["addrrsi"]["rax"] = 0x211c
and_["rax"]["addrrsi"] = 0x2120
gendict(and_, "addrrdi")
and_["addrrdi"]["rax"] = 0x2124
and_["rax"]["addrrdi"] = 0x2128
gendict(and_, "addrrbp")
and_["addrrbp"]["rax"] = 0x212c
and_["rax"]["addrrbp"] = 0x2131
gendict(and_, "addrrsp")
and_["addrrsp"]["rax"] = 0x2136
and_["rax"]["addrrsp"] = 0x213b
gendict(and_, "rbx")
and_["rbx"]["rax"] = 0x2140
and_["rbx"]["rcx"] = 0x2144
and_["rbx"]["rdx"] = 0x2148
and_["rbx"]["rsi"] = 0x214c
and_["rbx"]["rdi"] = 0x2150
and_["rbx"]["rbp"] = 0x2154
and_["rbx"]["rsp"] = 0x2158
gendict(and_, "addrrax")
and_["addrrax"]["rbx"] = 0x215c
and_["rbx"]["addrrax"] = 0x2160
gendict(and_, "addrrbx")
and_["addrrbx"]["rbx"] = 0x2164
and_["rbx"]["addrrbx"] = 0x2168
gendict(and_, "addrrcx")
and_["addrrcx"]["rbx"] = 0x216c
and_["rbx"]["addrrcx"] = 0x2170
gendict(and_, "addrrdx")
and_["addrrdx"]["rbx"] = 0x2174
and_["rbx"]["addrrdx"] = 0x2178
gendict(and_, "addrrsi")
and_["addrrsi"]["rbx"] = 0x217c
and_["rbx"]["addrrsi"] = 0x2180
gendict(and_, "addrrdi")
and_["addrrdi"]["rbx"] = 0x2184
and_["rbx"]["addrrdi"] = 0x2188
gendict(and_, "addrrbp")
and_["addrrbp"]["rbx"] = 0x218c
and_["rbx"]["addrrbp"] = 0x2191
gendict(and_, "addrrsp")
and_["addrrsp"]["rbx"] = 0x2196
and_["rbx"]["addrrsp"] = 0x219b
gendict(and_, "rcx")
and_["rcx"]["rax"] = 0x21a0
and_["rcx"]["rbx"] = 0x21a4
and_["rcx"]["rdx"] = 0x21a8
and_["rcx"]["rsi"] = 0x21ac
and_["rcx"]["rdi"] = 0x21b0
and_["rcx"]["rbp"] = 0x21b4
and_["rcx"]["rsp"] = 0x21b8
gendict(and_, "addrrax")
and_["addrrax"]["rcx"] = 0x21bc
and_["rcx"]["addrrax"] = 0x21c0
gendict(and_, "addrrbx")
and_["addrrbx"]["rcx"] = 0x21c4
and_["rcx"]["addrrbx"] = 0x21c8
gendict(and_, "addrrcx")
and_["addrrcx"]["rcx"] = 0x21cc
and_["rcx"]["addrrcx"] = 0x21d0
gendict(and_, "addrrdx")
and_["addrrdx"]["rcx"] = 0x21d4
and_["rcx"]["addrrdx"] = 0x21d8
gendict(and_, "addrrsi")
and_["addrrsi"]["rcx"] = 0x21dc
and_["rcx"]["addrrsi"] = 0x21e0
gendict(and_, "addrrdi")
and_["addrrdi"]["rcx"] = 0x21e4
and_["rcx"]["addrrdi"] = 0x21e8
gendict(and_, "addrrbp")
and_["addrrbp"]["rcx"] = 0x21ec
and_["rcx"]["addrrbp"] = 0x21f1
gendict(and_, "addrrsp")
and_["addrrsp"]["rcx"] = 0x21f6
and_["rcx"]["addrrsp"] = 0x21fb
gendict(and_, "rdx")
and_["rdx"]["rax"] = 0x2200
and_["rdx"]["rbx"] = 0x2204
and_["rdx"]["rcx"] = 0x2208
and_["rdx"]["rsi"] = 0x220c
and_["rdx"]["rdi"] = 0x2210
and_["rdx"]["rbp"] = 0x2214
and_["rdx"]["rsp"] = 0x2218
gendict(and_, "addrrax")
and_["addrrax"]["rdx"] = 0x221c
and_["rdx"]["addrrax"] = 0x2220
gendict(and_, "addrrbx")
and_["addrrbx"]["rdx"] = 0x2224
and_["rdx"]["addrrbx"] = 0x2228
gendict(and_, "addrrcx")
and_["addrrcx"]["rdx"] = 0x222c
and_["rdx"]["addrrcx"] = 0x2230
gendict(and_, "addrrdx")
and_["addrrdx"]["rdx"] = 0x2234
and_["rdx"]["addrrdx"] = 0x2238
gendict(and_, "addrrsi")
and_["addrrsi"]["rdx"] = 0x223c
and_["rdx"]["addrrsi"] = 0x2240
gendict(and_, "addrrdi")
and_["addrrdi"]["rdx"] = 0x2244
and_["rdx"]["addrrdi"] = 0x2248
gendict(and_, "addrrbp")
and_["addrrbp"]["rdx"] = 0x224c
and_["rdx"]["addrrbp"] = 0x2251
gendict(and_, "addrrsp")
and_["addrrsp"]["rdx"] = 0x2256
and_["rdx"]["addrrsp"] = 0x225b
gendict(and_, "rsi")
and_["rsi"]["rax"] = 0x2260
and_["rsi"]["rbx"] = 0x2264
and_["rsi"]["rcx"] = 0x2268
and_["rsi"]["rdx"] = 0x226c
and_["rsi"]["rdi"] = 0x2270
and_["rsi"]["rbp"] = 0x2274
and_["rsi"]["rsp"] = 0x2278
gendict(and_, "addrrax")
and_["addrrax"]["rsi"] = 0x227c
and_["rsi"]["addrrax"] = 0x2280
gendict(and_, "addrrbx")
and_["addrrbx"]["rsi"] = 0x2284
and_["rsi"]["addrrbx"] = 0x2288
gendict(and_, "addrrcx")
and_["addrrcx"]["rsi"] = 0x228c
and_["rsi"]["addrrcx"] = 0x2290
gendict(and_, "addrrdx")
and_["addrrdx"]["rsi"] = 0x2294
and_["rsi"]["addrrdx"] = 0x2298
gendict(and_, "addrrsi")
and_["addrrsi"]["rsi"] = 0x229c
and_["rsi"]["addrrsi"] = 0x22a0
gendict(and_, "addrrdi")
and_["addrrdi"]["rsi"] = 0x22a4
and_["rsi"]["addrrdi"] = 0x22a8
gendict(and_, "addrrbp")
and_["addrrbp"]["rsi"] = 0x22ac
and_["rsi"]["addrrbp"] = 0x22b1
gendict(and_, "addrrsp")
and_["addrrsp"]["rsi"] = 0x22b6
and_["rsi"]["addrrsp"] = 0x22bb
gendict(and_, "rdi")
and_["rdi"]["rax"] = 0x22c0
and_["rdi"]["rbx"] = 0x22c4
and_["rdi"]["rcx"] = 0x22c8
and_["rdi"]["rdx"] = 0x22cc
and_["rdi"]["rsi"] = 0x22d0
and_["rdi"]["rbp"] = 0x22d4
and_["rdi"]["rsp"] = 0x22d8
gendict(and_, "addrrax")
and_["addrrax"]["rdi"] = 0x22dc
and_["rdi"]["addrrax"] = 0x22e0
gendict(and_, "addrrbx")
and_["addrrbx"]["rdi"] = 0x22e4
and_["rdi"]["addrrbx"] = 0x22e8
gendict(and_, "addrrcx")
and_["addrrcx"]["rdi"] = 0x22ec
and_["rdi"]["addrrcx"] = 0x22f0
gendict(and_, "addrrdx")
and_["addrrdx"]["rdi"] = 0x22f4
and_["rdi"]["addrrdx"] = 0x22f8
gendict(and_, "addrrsi")
and_["addrrsi"]["rdi"] = 0x22fc
and_["rdi"]["addrrsi"] = 0x2300
gendict(and_, "addrrdi")
and_["addrrdi"]["rdi"] = 0x2304
and_["rdi"]["addrrdi"] = 0x2308
gendict(and_, "addrrbp")
and_["addrrbp"]["rdi"] = 0x230c
and_["rdi"]["addrrbp"] = 0x2311
gendict(and_, "addrrsp")
and_["addrrsp"]["rdi"] = 0x2316
and_["rdi"]["addrrsp"] = 0x231b
gendict(and_, "rbp")
and_["rbp"]["rax"] = 0x2320
and_["rbp"]["rbx"] = 0x2324
and_["rbp"]["rcx"] = 0x2328
and_["rbp"]["rdx"] = 0x232c
and_["rbp"]["rsi"] = 0x2330
and_["rbp"]["rdi"] = 0x2334
and_["rbp"]["rsp"] = 0x2338
gendict(and_, "addrrax")
and_["addrrax"]["rbp"] = 0x233c
and_["rbp"]["addrrax"] = 0x2340
gendict(and_, "addrrbx")
and_["addrrbx"]["rbp"] = 0x2344
and_["rbp"]["addrrbx"] = 0x2348
gendict(and_, "addrrcx")
and_["addrrcx"]["rbp"] = 0x234c
and_["rbp"]["addrrcx"] = 0x2350
gendict(and_, "addrrdx")
and_["addrrdx"]["rbp"] = 0x2354
and_["rbp"]["addrrdx"] = 0x2358
gendict(and_, "addrrsi")
and_["addrrsi"]["rbp"] = 0x235c
and_["rbp"]["addrrsi"] = 0x2360
gendict(and_, "addrrdi")
and_["addrrdi"]["rbp"] = 0x2364
and_["rbp"]["addrrdi"] = 0x2368
gendict(and_, "addrrbp")
and_["addrrbp"]["rbp"] = 0x236c
and_["rbp"]["addrrbp"] = 0x2371
gendict(and_, "addrrsp")
and_["addrrsp"]["rbp"] = 0x2376
and_["rbp"]["addrrsp"] = 0x237b
gendict(and_, "rsp")
and_["rsp"]["rax"] = 0x2380
and_["rsp"]["rbx"] = 0x2384
and_["rsp"]["rcx"] = 0x2388
and_["rsp"]["rdx"] = 0x238c
and_["rsp"]["rsi"] = 0x2390
and_["rsp"]["rdi"] = 0x2394
and_["rsp"]["rbp"] = 0x2398
gendict(and_, "addrrax")
and_["addrrax"]["rsp"] = 0x239c
and_["rsp"]["addrrax"] = 0x23a0
gendict(and_, "addrrbx")
and_["addrrbx"]["rsp"] = 0x23a4
and_["rsp"]["addrrbx"] = 0x23a8
gendict(and_, "addrrcx")
and_["addrrcx"]["rsp"] = 0x23ac
and_["rsp"]["addrrcx"] = 0x23b0
gendict(and_, "addrrdx")
and_["addrrdx"]["rsp"] = 0x23b4
and_["rsp"]["addrrdx"] = 0x23b8
gendict(and_, "addrrsi")
and_["addrrsi"]["rsp"] = 0x23bc
and_["rsp"]["addrrsi"] = 0x23c0
gendict(and_, "addrrdi")
and_["addrrdi"]["rsp"] = 0x23c4
and_["rsp"]["addrrdi"] = 0x23c8
gendict(and_, "addrrbp")
and_["addrrbp"]["rsp"] = 0x23cc
and_["rsp"]["addrrbp"] = 0x23d1
gendict(and_, "addrrsp")
and_["addrrsp"]["rsp"] = 0x23d6
and_["rsp"]["addrrsp"] = 0x23db
gendict(and_, "eax")
and_["eax"]["ebx"] = 0x23e0
and_["eax"]["ecx"] = 0x23e3
and_["eax"]["edx"] = 0x23e6
and_["eax"]["esi"] = 0x23e9
and_["eax"]["edi"] = 0x23ec
and_["eax"]["ebp"] = 0x23ef
and_["eax"]["esp"] = 0x23f2
gendict(and_, "addrrax")
and_["addrrax"]["eax"] = 0x23f5
and_["eax"]["addrrax"] = 0x23f8
gendict(and_, "addrrbx")
and_["addrrbx"]["eax"] = 0x23fb
and_["eax"]["addrrbx"] = 0x23fe
gendict(and_, "addrrcx")
and_["addrrcx"]["eax"] = 0x2401
and_["eax"]["addrrcx"] = 0x2404
gendict(and_, "addrrdx")
and_["addrrdx"]["eax"] = 0x2407
and_["eax"]["addrrdx"] = 0x240a
gendict(and_, "addrrsi")
and_["addrrsi"]["eax"] = 0x240d
and_["eax"]["addrrsi"] = 0x2410
gendict(and_, "addrrdi")
and_["addrrdi"]["eax"] = 0x2413
and_["eax"]["addrrdi"] = 0x2416
gendict(and_, "addrrbp")
and_["addrrbp"]["eax"] = 0x2419
and_["eax"]["addrrbp"] = 0x241d
gendict(and_, "addrrsp")
and_["addrrsp"]["eax"] = 0x2421
and_["eax"]["addrrsp"] = 0x2425
gendict(and_, "ebx")
and_["ebx"]["eax"] = 0x2429
and_["ebx"]["ecx"] = 0x242c
and_["ebx"]["edx"] = 0x242f
and_["ebx"]["esi"] = 0x2432
and_["ebx"]["edi"] = 0x2435
and_["ebx"]["ebp"] = 0x2438
and_["ebx"]["esp"] = 0x243b
gendict(and_, "addrrax")
and_["addrrax"]["ebx"] = 0x243e
and_["ebx"]["addrrax"] = 0x2441
gendict(and_, "addrrbx")
and_["addrrbx"]["ebx"] = 0x2444
and_["ebx"]["addrrbx"] = 0x2447
gendict(and_, "addrrcx")
and_["addrrcx"]["ebx"] = 0x244a
and_["ebx"]["addrrcx"] = 0x244d
gendict(and_, "addrrdx")
and_["addrrdx"]["ebx"] = 0x2450
and_["ebx"]["addrrdx"] = 0x2453
gendict(and_, "addrrsi")
and_["addrrsi"]["ebx"] = 0x2456
and_["ebx"]["addrrsi"] = 0x2459
gendict(and_, "addrrdi")
and_["addrrdi"]["ebx"] = 0x245c
and_["ebx"]["addrrdi"] = 0x245f
gendict(and_, "addrrbp")
and_["addrrbp"]["ebx"] = 0x2462
and_["ebx"]["addrrbp"] = 0x2466
gendict(and_, "addrrsp")
and_["addrrsp"]["ebx"] = 0x246a
and_["ebx"]["addrrsp"] = 0x246e
gendict(and_, "ecx")
and_["ecx"]["eax"] = 0x2472
and_["ecx"]["ebx"] = 0x2475
and_["ecx"]["edx"] = 0x2478
and_["ecx"]["esi"] = 0x247b
and_["ecx"]["edi"] = 0x247e
and_["ecx"]["ebp"] = 0x2481
and_["ecx"]["esp"] = 0x2484
gendict(and_, "addrrax")
and_["addrrax"]["ecx"] = 0x2487
and_["ecx"]["addrrax"] = 0x248a
gendict(and_, "addrrbx")
and_["addrrbx"]["ecx"] = 0x248d
and_["ecx"]["addrrbx"] = 0x2490
gendict(and_, "addrrcx")
and_["addrrcx"]["ecx"] = 0x2493
and_["ecx"]["addrrcx"] = 0x2496
gendict(and_, "addrrdx")
and_["addrrdx"]["ecx"] = 0x2499
and_["ecx"]["addrrdx"] = 0x249c
gendict(and_, "addrrsi")
and_["addrrsi"]["ecx"] = 0x249f
and_["ecx"]["addrrsi"] = 0x24a2
gendict(and_, "addrrdi")
and_["addrrdi"]["ecx"] = 0x24a5
and_["ecx"]["addrrdi"] = 0x24a8
gendict(and_, "addrrbp")
and_["addrrbp"]["ecx"] = 0x24ab
and_["ecx"]["addrrbp"] = 0x24af
gendict(and_, "addrrsp")
and_["addrrsp"]["ecx"] = 0x24b3
and_["ecx"]["addrrsp"] = 0x24b7
gendict(and_, "edx")
and_["edx"]["eax"] = 0x24bb
and_["edx"]["ebx"] = 0x24be
and_["edx"]["ecx"] = 0x24c1
and_["edx"]["esi"] = 0x24c4
and_["edx"]["edi"] = 0x24c7
and_["edx"]["ebp"] = 0x24ca
and_["edx"]["esp"] = 0x24cd
gendict(and_, "addrrax")
and_["addrrax"]["edx"] = 0x24d0
and_["edx"]["addrrax"] = 0x24d3
gendict(and_, "addrrbx")
and_["addrrbx"]["edx"] = 0x24d6
and_["edx"]["addrrbx"] = 0x24d9
gendict(and_, "addrrcx")
and_["addrrcx"]["edx"] = 0x24dc
and_["edx"]["addrrcx"] = 0x24df
gendict(and_, "addrrdx")
and_["addrrdx"]["edx"] = 0x24e2
and_["edx"]["addrrdx"] = 0x24e5
gendict(and_, "addrrsi")
and_["addrrsi"]["edx"] = 0x24e8
and_["edx"]["addrrsi"] = 0x24eb
gendict(and_, "addrrdi")
and_["addrrdi"]["edx"] = 0x24ee
and_["edx"]["addrrdi"] = 0x24f1
gendict(and_, "addrrbp")
and_["addrrbp"]["edx"] = 0x24f4
and_["edx"]["addrrbp"] = 0x24f8
gendict(and_, "addrrsp")
and_["addrrsp"]["edx"] = 0x24fc
and_["edx"]["addrrsp"] = 0x2500
gendict(and_, "esi")
and_["esi"]["eax"] = 0x2504
and_["esi"]["ebx"] = 0x2507
and_["esi"]["ecx"] = 0x250a
and_["esi"]["edx"] = 0x250d
and_["esi"]["edi"] = 0x2510
and_["esi"]["ebp"] = 0x2513
and_["esi"]["esp"] = 0x2516
gendict(and_, "addrrax")
and_["addrrax"]["esi"] = 0x2519
and_["esi"]["addrrax"] = 0x251c
gendict(and_, "addrrbx")
and_["addrrbx"]["esi"] = 0x251f
and_["esi"]["addrrbx"] = 0x2522
gendict(and_, "addrrcx")
and_["addrrcx"]["esi"] = 0x2525
and_["esi"]["addrrcx"] = 0x2528
gendict(and_, "addrrdx")
and_["addrrdx"]["esi"] = 0x252b
and_["esi"]["addrrdx"] = 0x252e
gendict(and_, "addrrsi")
and_["addrrsi"]["esi"] = 0x2531
and_["esi"]["addrrsi"] = 0x2534
gendict(and_, "addrrdi")
and_["addrrdi"]["esi"] = 0x2537
and_["esi"]["addrrdi"] = 0x253a
gendict(and_, "addrrbp")
and_["addrrbp"]["esi"] = 0x253d
and_["esi"]["addrrbp"] = 0x2541
gendict(and_, "addrrsp")
and_["addrrsp"]["esi"] = 0x2545
and_["esi"]["addrrsp"] = 0x2549
gendict(and_, "edi")
and_["edi"]["eax"] = 0x254d
and_["edi"]["ebx"] = 0x2550
and_["edi"]["ecx"] = 0x2553
and_["edi"]["edx"] = 0x2556
and_["edi"]["esi"] = 0x2559
and_["edi"]["ebp"] = 0x255c
and_["edi"]["esp"] = 0x255f
gendict(and_, "addrrax")
and_["addrrax"]["edi"] = 0x2562
and_["edi"]["addrrax"] = 0x2565
gendict(and_, "addrrbx")
and_["addrrbx"]["edi"] = 0x2568
and_["edi"]["addrrbx"] = 0x256b
gendict(and_, "addrrcx")
and_["addrrcx"]["edi"] = 0x256e
and_["edi"]["addrrcx"] = 0x2571
gendict(and_, "addrrdx")
and_["addrrdx"]["edi"] = 0x2574
and_["edi"]["addrrdx"] = 0x2577
gendict(and_, "addrrsi")
and_["addrrsi"]["edi"] = 0x257a
and_["edi"]["addrrsi"] = 0x257d
gendict(and_, "addrrdi")
and_["addrrdi"]["edi"] = 0x2580
and_["edi"]["addrrdi"] = 0x2583
gendict(and_, "addrrbp")
and_["addrrbp"]["edi"] = 0x2586
and_["edi"]["addrrbp"] = 0x258a
gendict(and_, "addrrsp")
and_["addrrsp"]["edi"] = 0x258e
and_["edi"]["addrrsp"] = 0x2592
gendict(and_, "ebp")
and_["ebp"]["eax"] = 0x2596
and_["ebp"]["ebx"] = 0x2599
and_["ebp"]["ecx"] = 0x259c
and_["ebp"]["edx"] = 0x259f
and_["ebp"]["esi"] = 0x25a2
and_["ebp"]["edi"] = 0x25a5
and_["ebp"]["esp"] = 0x25a8
gendict(and_, "addrrax")
and_["addrrax"]["ebp"] = 0x25ab
and_["ebp"]["addrrax"] = 0x25ae
gendict(and_, "addrrbx")
and_["addrrbx"]["ebp"] = 0x25b1
and_["ebp"]["addrrbx"] = 0x25b4
gendict(and_, "addrrcx")
and_["addrrcx"]["ebp"] = 0x25b7
and_["ebp"]["addrrcx"] = 0x25ba
gendict(and_, "addrrdx")
and_["addrrdx"]["ebp"] = 0x25bd
and_["ebp"]["addrrdx"] = 0x25c0
gendict(and_, "addrrsi")
and_["addrrsi"]["ebp"] = 0x25c3
and_["ebp"]["addrrsi"] = 0x25c6
gendict(and_, "addrrdi")
and_["addrrdi"]["ebp"] = 0x25c9
and_["ebp"]["addrrdi"] = 0x25cc
gendict(and_, "addrrbp")
and_["addrrbp"]["ebp"] = 0x25cf
and_["ebp"]["addrrbp"] = 0x25d3
gendict(and_, "addrrsp")
and_["addrrsp"]["ebp"] = 0x25d7
and_["ebp"]["addrrsp"] = 0x25db
gendict(and_, "esp")
and_["esp"]["eax"] = 0x25df
and_["esp"]["ebx"] = 0x25e2
and_["esp"]["ecx"] = 0x25e5
and_["esp"]["edx"] = 0x25e8
and_["esp"]["esi"] = 0x25eb
and_["esp"]["edi"] = 0x25ee
and_["esp"]["ebp"] = 0x25f1
gendict(and_, "addrrax")
and_["addrrax"]["esp"] = 0x25f4
and_["esp"]["addrrax"] = 0x25f7
gendict(and_, "addrrbx")
and_["addrrbx"]["esp"] = 0x25fa
and_["esp"]["addrrbx"] = 0x25fd
gendict(and_, "addrrcx")
and_["addrrcx"]["esp"] = 0x2600
and_["esp"]["addrrcx"] = 0x2603
gendict(and_, "addrrdx")
and_["addrrdx"]["esp"] = 0x2606
and_["esp"]["addrrdx"] = 0x2609
gendict(and_, "addrrsi")
and_["addrrsi"]["esp"] = 0x260c
and_["esp"]["addrrsi"] = 0x260f
gendict(and_, "addrrdi")
and_["addrrdi"]["esp"] = 0x2612
and_["esp"]["addrrdi"] = 0x2615
gendict(and_, "addrrbp")
and_["addrrbp"]["esp"] = 0x2618
and_["esp"]["addrrbp"] = 0x261c
gendict(and_, "addrrsp")
and_["addrrsp"]["esp"] = 0x2620
and_["esp"]["addrrsp"] = 0x2624
gendict(and_, "ax")
and_["ax"]["bx"] = 0x2628
and_["ax"]["cx"] = 0x262c
and_["ax"]["dx"] = 0x2630
and_["ax"]["si"] = 0x2634
and_["ax"]["di"] = 0x2638
and_["ax"]["bp"] = 0x263c
and_["ax"]["sp"] = 0x2640
gendict(and_, "addrrax")
and_["addrrax"]["ax"] = 0x2644
and_["ax"]["addrrax"] = 0x2648
gendict(and_, "addrrbx")
and_["addrrbx"]["ax"] = 0x264c
and_["ax"]["addrrbx"] = 0x2650
gendict(and_, "addrrcx")
and_["addrrcx"]["ax"] = 0x2654
and_["ax"]["addrrcx"] = 0x2658
gendict(and_, "addrrdx")
and_["addrrdx"]["ax"] = 0x265c
and_["ax"]["addrrdx"] = 0x2660
gendict(and_, "addrrsi")
and_["addrrsi"]["ax"] = 0x2664
and_["ax"]["addrrsi"] = 0x2668
gendict(and_, "addrrdi")
and_["addrrdi"]["ax"] = 0x266c
and_["ax"]["addrrdi"] = 0x2670
gendict(and_, "addrrbp")
and_["addrrbp"]["ax"] = 0x2674
and_["ax"]["addrrbp"] = 0x2679
gendict(and_, "addrrsp")
and_["addrrsp"]["ax"] = 0x267e
and_["ax"]["addrrsp"] = 0x2683
gendict(and_, "bx")
and_["bx"]["ax"] = 0x2688
and_["bx"]["cx"] = 0x268c
and_["bx"]["dx"] = 0x2690
and_["bx"]["si"] = 0x2694
and_["bx"]["di"] = 0x2698
and_["bx"]["bp"] = 0x269c
and_["bx"]["sp"] = 0x26a0
gendict(and_, "addrrax")
and_["addrrax"]["bx"] = 0x26a4
and_["bx"]["addrrax"] = 0x26a8
gendict(and_, "addrrbx")
and_["addrrbx"]["bx"] = 0x26ac
and_["bx"]["addrrbx"] = 0x26b0
gendict(and_, "addrrcx")
and_["addrrcx"]["bx"] = 0x26b4
and_["bx"]["addrrcx"] = 0x26b8
gendict(and_, "addrrdx")
and_["addrrdx"]["bx"] = 0x26bc
and_["bx"]["addrrdx"] = 0x26c0
gendict(and_, "addrrsi")
and_["addrrsi"]["bx"] = 0x26c4
and_["bx"]["addrrsi"] = 0x26c8
gendict(and_, "addrrdi")
and_["addrrdi"]["bx"] = 0x26cc
and_["bx"]["addrrdi"] = 0x26d0
gendict(and_, "addrrbp")
and_["addrrbp"]["bx"] = 0x26d4
and_["bx"]["addrrbp"] = 0x26d9
gendict(and_, "addrrsp")
and_["addrrsp"]["bx"] = 0x26de
and_["bx"]["addrrsp"] = 0x26e3
gendict(and_, "cx")
and_["cx"]["ax"] = 0x26e8
and_["cx"]["bx"] = 0x26ec
and_["cx"]["dx"] = 0x26f0
and_["cx"]["si"] = 0x26f4
and_["cx"]["di"] = 0x26f8
and_["cx"]["bp"] = 0x26fc
and_["cx"]["sp"] = 0x2700
gendict(and_, "addrrax")
and_["addrrax"]["cx"] = 0x2704
and_["cx"]["addrrax"] = 0x2708
gendict(and_, "addrrbx")
and_["addrrbx"]["cx"] = 0x270c
and_["cx"]["addrrbx"] = 0x2710
gendict(and_, "addrrcx")
and_["addrrcx"]["cx"] = 0x2714
and_["cx"]["addrrcx"] = 0x2718
gendict(and_, "addrrdx")
and_["addrrdx"]["cx"] = 0x271c
and_["cx"]["addrrdx"] = 0x2720
gendict(and_, "addrrsi")
and_["addrrsi"]["cx"] = 0x2724
and_["cx"]["addrrsi"] = 0x2728
gendict(and_, "addrrdi")
and_["addrrdi"]["cx"] = 0x272c
and_["cx"]["addrrdi"] = 0x2730
gendict(and_, "addrrbp")
and_["addrrbp"]["cx"] = 0x2734
and_["cx"]["addrrbp"] = 0x2739
gendict(and_, "addrrsp")
and_["addrrsp"]["cx"] = 0x273e
and_["cx"]["addrrsp"] = 0x2743
gendict(and_, "dx")
and_["dx"]["ax"] = 0x2748
and_["dx"]["bx"] = 0x274c
and_["dx"]["cx"] = 0x2750
and_["dx"]["si"] = 0x2754
and_["dx"]["di"] = 0x2758
and_["dx"]["bp"] = 0x275c
and_["dx"]["sp"] = 0x2760
gendict(and_, "addrrax")
and_["addrrax"]["dx"] = 0x2764
and_["dx"]["addrrax"] = 0x2768
gendict(and_, "addrrbx")
and_["addrrbx"]["dx"] = 0x276c
and_["dx"]["addrrbx"] = 0x2770
gendict(and_, "addrrcx")
and_["addrrcx"]["dx"] = 0x2774
and_["dx"]["addrrcx"] = 0x2778
gendict(and_, "addrrdx")
and_["addrrdx"]["dx"] = 0x277c
and_["dx"]["addrrdx"] = 0x2780
gendict(and_, "addrrsi")
and_["addrrsi"]["dx"] = 0x2784
and_["dx"]["addrrsi"] = 0x2788
gendict(and_, "addrrdi")
and_["addrrdi"]["dx"] = 0x278c
and_["dx"]["addrrdi"] = 0x2790
gendict(and_, "addrrbp")
and_["addrrbp"]["dx"] = 0x2794
and_["dx"]["addrrbp"] = 0x2799
gendict(and_, "addrrsp")
and_["addrrsp"]["dx"] = 0x279e
and_["dx"]["addrrsp"] = 0x27a3
gendict(and_, "si")
and_["si"]["ax"] = 0x27a8
and_["si"]["bx"] = 0x27ac
and_["si"]["cx"] = 0x27b0
and_["si"]["dx"] = 0x27b4
and_["si"]["di"] = 0x27b8
and_["si"]["bp"] = 0x27bc
and_["si"]["sp"] = 0x27c0
gendict(and_, "addrrax")
and_["addrrax"]["si"] = 0x27c4
and_["si"]["addrrax"] = 0x27c8
gendict(and_, "addrrbx")
and_["addrrbx"]["si"] = 0x27cc
and_["si"]["addrrbx"] = 0x27d0
gendict(and_, "addrrcx")
and_["addrrcx"]["si"] = 0x27d4
and_["si"]["addrrcx"] = 0x27d8
gendict(and_, "addrrdx")
and_["addrrdx"]["si"] = 0x27dc
and_["si"]["addrrdx"] = 0x27e0
gendict(and_, "addrrsi")
and_["addrrsi"]["si"] = 0x27e4
and_["si"]["addrrsi"] = 0x27e8
gendict(and_, "addrrdi")
and_["addrrdi"]["si"] = 0x27ec
and_["si"]["addrrdi"] = 0x27f0
gendict(and_, "addrrbp")
and_["addrrbp"]["si"] = 0x27f4
and_["si"]["addrrbp"] = 0x27f9
gendict(and_, "addrrsp")
and_["addrrsp"]["si"] = 0x27fe
and_["si"]["addrrsp"] = 0x2803
gendict(and_, "di")
and_["di"]["ax"] = 0x2808
and_["di"]["bx"] = 0x280c
and_["di"]["cx"] = 0x2810
and_["di"]["dx"] = 0x2814
and_["di"]["si"] = 0x2818
and_["di"]["bp"] = 0x281c
and_["di"]["sp"] = 0x2820
gendict(and_, "addrrax")
and_["addrrax"]["di"] = 0x2824
and_["di"]["addrrax"] = 0x2828
gendict(and_, "addrrbx")
and_["addrrbx"]["di"] = 0x282c
and_["di"]["addrrbx"] = 0x2830
gendict(and_, "addrrcx")
and_["addrrcx"]["di"] = 0x2834
and_["di"]["addrrcx"] = 0x2838
gendict(and_, "addrrdx")
and_["addrrdx"]["di"] = 0x283c
and_["di"]["addrrdx"] = 0x2840
gendict(and_, "addrrsi")
and_["addrrsi"]["di"] = 0x2844
and_["di"]["addrrsi"] = 0x2848
gendict(and_, "addrrdi")
and_["addrrdi"]["di"] = 0x284c
and_["di"]["addrrdi"] = 0x2850
gendict(and_, "addrrbp")
and_["addrrbp"]["di"] = 0x2854
and_["di"]["addrrbp"] = 0x2859
gendict(and_, "addrrsp")
and_["addrrsp"]["di"] = 0x285e
and_["di"]["addrrsp"] = 0x2863
gendict(and_, "bp")
and_["bp"]["ax"] = 0x2868
and_["bp"]["bx"] = 0x286c
and_["bp"]["cx"] = 0x2870
and_["bp"]["dx"] = 0x2874
and_["bp"]["si"] = 0x2878
and_["bp"]["di"] = 0x287c
and_["bp"]["sp"] = 0x2880
gendict(and_, "addrrax")
and_["addrrax"]["bp"] = 0x2884
and_["bp"]["addrrax"] = 0x2888
gendict(and_, "addrrbx")
and_["addrrbx"]["bp"] = 0x288c
and_["bp"]["addrrbx"] = 0x2890
gendict(and_, "addrrcx")
and_["addrrcx"]["bp"] = 0x2894
and_["bp"]["addrrcx"] = 0x2898
gendict(and_, "addrrdx")
and_["addrrdx"]["bp"] = 0x289c
and_["bp"]["addrrdx"] = 0x28a0
gendict(and_, "addrrsi")
and_["addrrsi"]["bp"] = 0x28a4
and_["bp"]["addrrsi"] = 0x28a8
gendict(and_, "addrrdi")
and_["addrrdi"]["bp"] = 0x28ac
and_["bp"]["addrrdi"] = 0x28b0
gendict(and_, "addrrbp")
and_["addrrbp"]["bp"] = 0x28b4
and_["bp"]["addrrbp"] = 0x28b9
gendict(and_, "addrrsp")
and_["addrrsp"]["bp"] = 0x28be
and_["bp"]["addrrsp"] = 0x28c3
gendict(and_, "sp")
and_["sp"]["ax"] = 0x28c8
and_["sp"]["bx"] = 0x28cc
and_["sp"]["cx"] = 0x28d0
and_["sp"]["dx"] = 0x28d4
and_["sp"]["si"] = 0x28d8
and_["sp"]["di"] = 0x28dc
and_["sp"]["bp"] = 0x28e0
gendict(and_, "addrrax")
and_["addrrax"]["sp"] = 0x28e4
and_["sp"]["addrrax"] = 0x28e8
gendict(and_, "addrrbx")
and_["addrrbx"]["sp"] = 0x28ec
and_["sp"]["addrrbx"] = 0x28f0
gendict(and_, "addrrcx")
and_["addrrcx"]["sp"] = 0x28f4
and_["sp"]["addrrcx"] = 0x28f8
gendict(and_, "addrrdx")
and_["addrrdx"]["sp"] = 0x28fc
and_["sp"]["addrrdx"] = 0x2900
gendict(and_, "addrrsi")
and_["addrrsi"]["sp"] = 0x2904
and_["sp"]["addrrsi"] = 0x2908
gendict(and_, "addrrdi")
and_["addrrdi"]["sp"] = 0x290c
and_["sp"]["addrrdi"] = 0x2910
gendict(and_, "addrrbp")
and_["addrrbp"]["sp"] = 0x2914
and_["sp"]["addrrbp"] = 0x2919
gendict(and_, "addrrsp")
and_["addrrsp"]["sp"] = 0x291e
and_["sp"]["addrrsp"] = 0x2923
gendict(and_, "ah")
and_["ah"]["bh"] = 0x2928
and_["ah"]["ch"] = 0x292b
and_["ah"]["dh"] = 0x292e
gendict(and_, "addrrax")
and_["addrrax"]["ah"] = 0x2931
and_["ah"]["addrrax"] = 0x2934
gendict(and_, "addrrbx")
and_["addrrbx"]["ah"] = 0x2937
and_["ah"]["addrrbx"] = 0x293a
gendict(and_, "addrrcx")
and_["addrrcx"]["ah"] = 0x293d
and_["ah"]["addrrcx"] = 0x2940
gendict(and_, "addrrdx")
and_["addrrdx"]["ah"] = 0x2943
and_["ah"]["addrrdx"] = 0x2946
gendict(and_, "addrrsi")
and_["addrrsi"]["ah"] = 0x2949
and_["ah"]["addrrsi"] = 0x294c
gendict(and_, "addrrdi")
and_["addrrdi"]["ah"] = 0x294f
and_["ah"]["addrrdi"] = 0x2952
gendict(and_, "addrrbp")
and_["addrrbp"]["ah"] = 0x2955
and_["ah"]["addrrbp"] = 0x2959
gendict(and_, "addrrsp")
and_["addrrsp"]["ah"] = 0x295d
and_["ah"]["addrrsp"] = 0x2961
gendict(and_, "bh")
and_["bh"]["ah"] = 0x2965
and_["bh"]["ch"] = 0x2968
and_["bh"]["dh"] = 0x296b
gendict(and_, "addrrax")
and_["addrrax"]["bh"] = 0x296e
and_["bh"]["addrrax"] = 0x2971
gendict(and_, "addrrbx")
and_["addrrbx"]["bh"] = 0x2974
and_["bh"]["addrrbx"] = 0x2977
gendict(and_, "addrrcx")
and_["addrrcx"]["bh"] = 0x297a
and_["bh"]["addrrcx"] = 0x297d
gendict(and_, "addrrdx")
and_["addrrdx"]["bh"] = 0x2980
and_["bh"]["addrrdx"] = 0x2983
gendict(and_, "addrrsi")
and_["addrrsi"]["bh"] = 0x2986
and_["bh"]["addrrsi"] = 0x2989
gendict(and_, "addrrdi")
and_["addrrdi"]["bh"] = 0x298c
and_["bh"]["addrrdi"] = 0x298f
gendict(and_, "addrrbp")
and_["addrrbp"]["bh"] = 0x2992
and_["bh"]["addrrbp"] = 0x2996
gendict(and_, "addrrsp")
and_["addrrsp"]["bh"] = 0x299a
and_["bh"]["addrrsp"] = 0x299e
gendict(and_, "ch")
and_["ch"]["ah"] = 0x29a2
and_["ch"]["bh"] = 0x29a5
and_["ch"]["dh"] = 0x29a8
gendict(and_, "addrrax")
and_["addrrax"]["ch"] = 0x29ab
and_["ch"]["addrrax"] = 0x29ae
gendict(and_, "addrrbx")
and_["addrrbx"]["ch"] = 0x29b1
and_["ch"]["addrrbx"] = 0x29b4
gendict(and_, "addrrcx")
and_["addrrcx"]["ch"] = 0x29b7
and_["ch"]["addrrcx"] = 0x29ba
gendict(and_, "addrrdx")
and_["addrrdx"]["ch"] = 0x29bd
and_["ch"]["addrrdx"] = 0x29c0
gendict(and_, "addrrsi")
and_["addrrsi"]["ch"] = 0x29c3
and_["ch"]["addrrsi"] = 0x29c6
gendict(and_, "addrrdi")
and_["addrrdi"]["ch"] = 0x29c9
and_["ch"]["addrrdi"] = 0x29cc
gendict(and_, "addrrbp")
and_["addrrbp"]["ch"] = 0x29cf
and_["ch"]["addrrbp"] = 0x29d3
gendict(and_, "addrrsp")
and_["addrrsp"]["ch"] = 0x29d7
and_["ch"]["addrrsp"] = 0x29db
gendict(and_, "dh")
and_["dh"]["ah"] = 0x29df
and_["dh"]["bh"] = 0x29e2
and_["dh"]["ch"] = 0x29e5
gendict(and_, "addrrax")
and_["addrrax"]["dh"] = 0x29e8
and_["dh"]["addrrax"] = 0x29eb
gendict(and_, "addrrbx")
and_["addrrbx"]["dh"] = 0x29ee
and_["dh"]["addrrbx"] = 0x29f1
gendict(and_, "addrrcx")
and_["addrrcx"]["dh"] = 0x29f4
and_["dh"]["addrrcx"] = 0x29f7
gendict(and_, "addrrdx")
and_["addrrdx"]["dh"] = 0x29fa
and_["dh"]["addrrdx"] = 0x29fd
gendict(and_, "addrrsi")
and_["addrrsi"]["dh"] = 0x2a00
and_["dh"]["addrrsi"] = 0x2a03
gendict(and_, "addrrdi")
and_["addrrdi"]["dh"] = 0x2a06
and_["dh"]["addrrdi"] = 0x2a09
gendict(and_, "addrrbp")
and_["addrrbp"]["dh"] = 0x2a0c
and_["dh"]["addrrbp"] = 0x2a10
gendict(and_, "addrrsp")
and_["addrrsp"]["dh"] = 0x2a14
and_["dh"]["addrrsp"] = 0x2a18
gendict(and_, "al")
and_["al"]["bl"] = 0x2a1c
and_["al"]["cl"] = 0x2a1f
and_["al"]["dl"] = 0x2a22
gendict(and_, "addrrax")
and_["addrrax"]["al"] = 0x2a25
and_["al"]["addrrax"] = 0x2a28
gendict(and_, "addrrbx")
and_["addrrbx"]["al"] = 0x2a2b
and_["al"]["addrrbx"] = 0x2a2e
gendict(and_, "addrrcx")
and_["addrrcx"]["al"] = 0x2a31
and_["al"]["addrrcx"] = 0x2a34
gendict(and_, "addrrdx")
and_["addrrdx"]["al"] = 0x2a37
and_["al"]["addrrdx"] = 0x2a3a
gendict(and_, "addrrsi")
and_["addrrsi"]["al"] = 0x2a3d
and_["al"]["addrrsi"] = 0x2a40
gendict(and_, "addrrdi")
and_["addrrdi"]["al"] = 0x2a43
and_["al"]["addrrdi"] = 0x2a46
gendict(and_, "addrrbp")
and_["addrrbp"]["al"] = 0x2a49
and_["al"]["addrrbp"] = 0x2a4d
gendict(and_, "addrrsp")
and_["addrrsp"]["al"] = 0x2a51
and_["al"]["addrrsp"] = 0x2a55
gendict(and_, "bl")
and_["bl"]["al"] = 0x2a59
and_["bl"]["cl"] = 0x2a5c
and_["bl"]["dl"] = 0x2a5f
gendict(and_, "addrrax")
and_["addrrax"]["bl"] = 0x2a62
and_["bl"]["addrrax"] = 0x2a65
gendict(and_, "addrrbx")
and_["addrrbx"]["bl"] = 0x2a68
and_["bl"]["addrrbx"] = 0x2a6b
gendict(and_, "addrrcx")
and_["addrrcx"]["bl"] = 0x2a6e
and_["bl"]["addrrcx"] = 0x2a71
gendict(and_, "addrrdx")
and_["addrrdx"]["bl"] = 0x2a74
and_["bl"]["addrrdx"] = 0x2a77
gendict(and_, "addrrsi")
and_["addrrsi"]["bl"] = 0x2a7a
and_["bl"]["addrrsi"] = 0x2a7d
gendict(and_, "addrrdi")
and_["addrrdi"]["bl"] = 0x2a80
and_["bl"]["addrrdi"] = 0x2a83
gendict(and_, "addrrbp")
and_["addrrbp"]["bl"] = 0x2a86
and_["bl"]["addrrbp"] = 0x2a8a
gendict(and_, "addrrsp")
and_["addrrsp"]["bl"] = 0x2a8e
and_["bl"]["addrrsp"] = 0x2a92
gendict(and_, "cl")
and_["cl"]["al"] = 0x2a96
and_["cl"]["bl"] = 0x2a99
and_["cl"]["dl"] = 0x2a9c
gendict(and_, "addrrax")
and_["addrrax"]["cl"] = 0x2a9f
and_["cl"]["addrrax"] = 0x2aa2
gendict(and_, "addrrbx")
and_["addrrbx"]["cl"] = 0x2aa5
and_["cl"]["addrrbx"] = 0x2aa8
gendict(and_, "addrrcx")
and_["addrrcx"]["cl"] = 0x2aab
and_["cl"]["addrrcx"] = 0x2aae
gendict(and_, "addrrdx")
and_["addrrdx"]["cl"] = 0x2ab1
and_["cl"]["addrrdx"] = 0x2ab4
gendict(and_, "addrrsi")
and_["addrrsi"]["cl"] = 0x2ab7
and_["cl"]["addrrsi"] = 0x2aba
gendict(and_, "addrrdi")
and_["addrrdi"]["cl"] = 0x2abd
and_["cl"]["addrrdi"] = 0x2ac0
gendict(and_, "addrrbp")
and_["addrrbp"]["cl"] = 0x2ac3
and_["cl"]["addrrbp"] = 0x2ac7
gendict(and_, "addrrsp")
and_["addrrsp"]["cl"] = 0x2acb
and_["cl"]["addrrsp"] = 0x2acf
gendict(and_, "dl")
and_["dl"]["al"] = 0x2ad3
and_["dl"]["bl"] = 0x2ad6
and_["dl"]["cl"] = 0x2ad9
gendict(and_, "addrrax")
and_["addrrax"]["dl"] = 0x2adc
and_["dl"]["addrrax"] = 0x2adf
gendict(and_, "addrrbx")
and_["addrrbx"]["dl"] = 0x2ae2
and_["dl"]["addrrbx"] = 0x2ae5
gendict(and_, "addrrcx")
and_["addrrcx"]["dl"] = 0x2ae8
and_["dl"]["addrrcx"] = 0x2aeb
gendict(and_, "addrrdx")
and_["addrrdx"]["dl"] = 0x2aee
and_["dl"]["addrrdx"] = 0x2af1
gendict(and_, "addrrsi")
and_["addrrsi"]["dl"] = 0x2af4
and_["dl"]["addrrsi"] = 0x2af7
gendict(and_, "addrrdi")
and_["addrrdi"]["dl"] = 0x2afa
and_["dl"]["addrrdi"] = 0x2afd
gendict(and_, "addrrbp")
and_["addrrbp"]["dl"] = 0x2b00
and_["dl"]["addrrbp"] = 0x2b04
gendict(and_, "addrrsp")
and_["addrrsp"]["dl"] = 0x2b08
and_["dl"]["addrrsp"] = 0x2b0c
or_ = {}
gendict(or_, "rax")
or_["rax"]["rbx"] = 0x2b10
or_["rax"]["rcx"] = 0x2b14
or_["rax"]["rdx"] = 0x2b18
or_["rax"]["rsi"] = 0x2b1c
or_["rax"]["rdi"] = 0x2b20
or_["rax"]["rbp"] = 0x2b24
or_["rax"]["rsp"] = 0x2b28
gendict(or_, "addrrax")
or_["addrrax"]["rax"] = 0x2b2c
or_["rax"]["addrrax"] = 0x2b30
gendict(or_, "addrrbx")
or_["addrrbx"]["rax"] = 0x2b34
or_["rax"]["addrrbx"] = 0x2b38
gendict(or_, "addrrcx")
or_["addrrcx"]["rax"] = 0x2b3c
or_["rax"]["addrrcx"] = 0x2b40
gendict(or_, "addrrdx")
or_["addrrdx"]["rax"] = 0x2b44
or_["rax"]["addrrdx"] = 0x2b48
gendict(or_, "addrrsi")
or_["addrrsi"]["rax"] = 0x2b4c
or_["rax"]["addrrsi"] = 0x2b50
gendict(or_, "addrrdi")
or_["addrrdi"]["rax"] = 0x2b54
or_["rax"]["addrrdi"] = 0x2b58
gendict(or_, "addrrbp")
or_["addrrbp"]["rax"] = 0x2b5c
or_["rax"]["addrrbp"] = 0x2b61
gendict(or_, "addrrsp")
or_["addrrsp"]["rax"] = 0x2b66
or_["rax"]["addrrsp"] = 0x2b6b
gendict(or_, "rbx")
or_["rbx"]["rax"] = 0x2b70
or_["rbx"]["rcx"] = 0x2b74
or_["rbx"]["rdx"] = 0x2b78
or_["rbx"]["rsi"] = 0x2b7c
or_["rbx"]["rdi"] = 0x2b80
or_["rbx"]["rbp"] = 0x2b84
or_["rbx"]["rsp"] = 0x2b88
gendict(or_, "addrrax")
or_["addrrax"]["rbx"] = 0x2b8c
or_["rbx"]["addrrax"] = 0x2b90
gendict(or_, "addrrbx")
or_["addrrbx"]["rbx"] = 0x2b94
or_["rbx"]["addrrbx"] = 0x2b98
gendict(or_, "addrrcx")
or_["addrrcx"]["rbx"] = 0x2b9c
or_["rbx"]["addrrcx"] = 0x2ba0
gendict(or_, "addrrdx")
or_["addrrdx"]["rbx"] = 0x2ba4
or_["rbx"]["addrrdx"] = 0x2ba8
gendict(or_, "addrrsi")
or_["addrrsi"]["rbx"] = 0x2bac
or_["rbx"]["addrrsi"] = 0x2bb0
gendict(or_, "addrrdi")
or_["addrrdi"]["rbx"] = 0x2bb4
or_["rbx"]["addrrdi"] = 0x2bb8
gendict(or_, "addrrbp")
or_["addrrbp"]["rbx"] = 0x2bbc
or_["rbx"]["addrrbp"] = 0x2bc1
gendict(or_, "addrrsp")
or_["addrrsp"]["rbx"] = 0x2bc6
or_["rbx"]["addrrsp"] = 0x2bcb
gendict(or_, "rcx")
or_["rcx"]["rax"] = 0x2bd0
or_["rcx"]["rbx"] = 0x2bd4
or_["rcx"]["rdx"] = 0x2bd8
or_["rcx"]["rsi"] = 0x2bdc
or_["rcx"]["rdi"] = 0x2be0
or_["rcx"]["rbp"] = 0x2be4
or_["rcx"]["rsp"] = 0x2be8
gendict(or_, "addrrax")
or_["addrrax"]["rcx"] = 0x2bec
or_["rcx"]["addrrax"] = 0x2bf0
gendict(or_, "addrrbx")
or_["addrrbx"]["rcx"] = 0x2bf4
or_["rcx"]["addrrbx"] = 0x2bf8
gendict(or_, "addrrcx")
or_["addrrcx"]["rcx"] = 0x2bfc
or_["rcx"]["addrrcx"] = 0x2c00
gendict(or_, "addrrdx")
or_["addrrdx"]["rcx"] = 0x2c04
or_["rcx"]["addrrdx"] = 0x2c08
gendict(or_, "addrrsi")
or_["addrrsi"]["rcx"] = 0x2c0c
or_["rcx"]["addrrsi"] = 0x2c10
gendict(or_, "addrrdi")
or_["addrrdi"]["rcx"] = 0x2c14
or_["rcx"]["addrrdi"] = 0x2c18
gendict(or_, "addrrbp")
or_["addrrbp"]["rcx"] = 0x2c1c
or_["rcx"]["addrrbp"] = 0x2c21
gendict(or_, "addrrsp")
or_["addrrsp"]["rcx"] = 0x2c26
or_["rcx"]["addrrsp"] = 0x2c2b
gendict(or_, "rdx")
or_["rdx"]["rax"] = 0x2c30
or_["rdx"]["rbx"] = 0x2c34
or_["rdx"]["rcx"] = 0x2c38
or_["rdx"]["rsi"] = 0x2c3c
or_["rdx"]["rdi"] = 0x2c40
or_["rdx"]["rbp"] = 0x2c44
or_["rdx"]["rsp"] = 0x2c48
gendict(or_, "addrrax")
or_["addrrax"]["rdx"] = 0x2c4c
or_["rdx"]["addrrax"] = 0x2c50
gendict(or_, "addrrbx")
or_["addrrbx"]["rdx"] = 0x2c54
or_["rdx"]["addrrbx"] = 0x2c58
gendict(or_, "addrrcx")
or_["addrrcx"]["rdx"] = 0x2c5c
or_["rdx"]["addrrcx"] = 0x2c60
gendict(or_, "addrrdx")
or_["addrrdx"]["rdx"] = 0x2c64
or_["rdx"]["addrrdx"] = 0x2c68
gendict(or_, "addrrsi")
or_["addrrsi"]["rdx"] = 0x2c6c
or_["rdx"]["addrrsi"] = 0x2c70
gendict(or_, "addrrdi")
or_["addrrdi"]["rdx"] = 0x2c74
or_["rdx"]["addrrdi"] = 0x2c78
gendict(or_, "addrrbp")
or_["addrrbp"]["rdx"] = 0x2c7c
or_["rdx"]["addrrbp"] = 0x2c81
gendict(or_, "addrrsp")
or_["addrrsp"]["rdx"] = 0x2c86
or_["rdx"]["addrrsp"] = 0x2c8b
gendict(or_, "rsi")
or_["rsi"]["rax"] = 0x2c90
or_["rsi"]["rbx"] = 0x2c94
or_["rsi"]["rcx"] = 0x2c98
or_["rsi"]["rdx"] = 0x2c9c
or_["rsi"]["rdi"] = 0x2ca0
or_["rsi"]["rbp"] = 0x2ca4
or_["rsi"]["rsp"] = 0x2ca8
gendict(or_, "addrrax")
or_["addrrax"]["rsi"] = 0x2cac
or_["rsi"]["addrrax"] = 0x2cb0
gendict(or_, "addrrbx")
or_["addrrbx"]["rsi"] = 0x2cb4
or_["rsi"]["addrrbx"] = 0x2cb8
gendict(or_, "addrrcx")
or_["addrrcx"]["rsi"] = 0x2cbc
or_["rsi"]["addrrcx"] = 0x2cc0
gendict(or_, "addrrdx")
or_["addrrdx"]["rsi"] = 0x2cc4
or_["rsi"]["addrrdx"] = 0x2cc8
gendict(or_, "addrrsi")
or_["addrrsi"]["rsi"] = 0x2ccc
or_["rsi"]["addrrsi"] = 0x2cd0
gendict(or_, "addrrdi")
or_["addrrdi"]["rsi"] = 0x2cd4
or_["rsi"]["addrrdi"] = 0x2cd8
gendict(or_, "addrrbp")
or_["addrrbp"]["rsi"] = 0x2cdc
or_["rsi"]["addrrbp"] = 0x2ce1
gendict(or_, "addrrsp")
or_["addrrsp"]["rsi"] = 0x2ce6
or_["rsi"]["addrrsp"] = 0x2ceb
gendict(or_, "rdi")
or_["rdi"]["rax"] = 0x2cf0
or_["rdi"]["rbx"] = 0x2cf4
or_["rdi"]["rcx"] = 0x2cf8
or_["rdi"]["rdx"] = 0x2cfc
or_["rdi"]["rsi"] = 0x2d00
or_["rdi"]["rbp"] = 0x2d04
or_["rdi"]["rsp"] = 0x2d08
gendict(or_, "addrrax")
or_["addrrax"]["rdi"] = 0x2d0c
or_["rdi"]["addrrax"] = 0x2d10
gendict(or_, "addrrbx")
or_["addrrbx"]["rdi"] = 0x2d14
or_["rdi"]["addrrbx"] = 0x2d18
gendict(or_, "addrrcx")
or_["addrrcx"]["rdi"] = 0x2d1c
or_["rdi"]["addrrcx"] = 0x2d20
gendict(or_, "addrrdx")
or_["addrrdx"]["rdi"] = 0x2d24
or_["rdi"]["addrrdx"] = 0x2d28
gendict(or_, "addrrsi")
or_["addrrsi"]["rdi"] = 0x2d2c
or_["rdi"]["addrrsi"] = 0x2d30
gendict(or_, "addrrdi")
or_["addrrdi"]["rdi"] = 0x2d34
or_["rdi"]["addrrdi"] = 0x2d38
gendict(or_, "addrrbp")
or_["addrrbp"]["rdi"] = 0x2d3c
or_["rdi"]["addrrbp"] = 0x2d41
gendict(or_, "addrrsp")
or_["addrrsp"]["rdi"] = 0x2d46
or_["rdi"]["addrrsp"] = 0x2d4b
gendict(or_, "rbp")
or_["rbp"]["rax"] = 0x2d50
or_["rbp"]["rbx"] = 0x2d54
or_["rbp"]["rcx"] = 0x2d58
or_["rbp"]["rdx"] = 0x2d5c
or_["rbp"]["rsi"] = 0x2d60
or_["rbp"]["rdi"] = 0x2d64
or_["rbp"]["rsp"] = 0x2d68
gendict(or_, "addrrax")
or_["addrrax"]["rbp"] = 0x2d6c
or_["rbp"]["addrrax"] = 0x2d70
gendict(or_, "addrrbx")
or_["addrrbx"]["rbp"] = 0x2d74
or_["rbp"]["addrrbx"] = 0x2d78
gendict(or_, "addrrcx")
or_["addrrcx"]["rbp"] = 0x2d7c
or_["rbp"]["addrrcx"] = 0x2d80
gendict(or_, "addrrdx")
or_["addrrdx"]["rbp"] = 0x2d84
or_["rbp"]["addrrdx"] = 0x2d88
gendict(or_, "addrrsi")
or_["addrrsi"]["rbp"] = 0x2d8c
or_["rbp"]["addrrsi"] = 0x2d90
gendict(or_, "addrrdi")
or_["addrrdi"]["rbp"] = 0x2d94
or_["rbp"]["addrrdi"] = 0x2d98
gendict(or_, "addrrbp")
or_["addrrbp"]["rbp"] = 0x2d9c
or_["rbp"]["addrrbp"] = 0x2da1
gendict(or_, "addrrsp")
or_["addrrsp"]["rbp"] = 0x2da6
or_["rbp"]["addrrsp"] = 0x2dab
gendict(or_, "rsp")
or_["rsp"]["rax"] = 0x2db0
or_["rsp"]["rbx"] = 0x2db4
or_["rsp"]["rcx"] = 0x2db8
or_["rsp"]["rdx"] = 0x2dbc
or_["rsp"]["rsi"] = 0x2dc0
or_["rsp"]["rdi"] = 0x2dc4
or_["rsp"]["rbp"] = 0x2dc8
gendict(or_, "addrrax")
or_["addrrax"]["rsp"] = 0x2dcc
or_["rsp"]["addrrax"] = 0x2dd0
gendict(or_, "addrrbx")
or_["addrrbx"]["rsp"] = 0x2dd4
or_["rsp"]["addrrbx"] = 0x2dd8
gendict(or_, "addrrcx")
or_["addrrcx"]["rsp"] = 0x2ddc
or_["rsp"]["addrrcx"] = 0x2de0
gendict(or_, "addrrdx")
or_["addrrdx"]["rsp"] = 0x2de4
or_["rsp"]["addrrdx"] = 0x2de8
gendict(or_, "addrrsi")
or_["addrrsi"]["rsp"] = 0x2dec
or_["rsp"]["addrrsi"] = 0x2df0
gendict(or_, "addrrdi")
or_["addrrdi"]["rsp"] = 0x2df4
or_["rsp"]["addrrdi"] = 0x2df8
gendict(or_, "addrrbp")
or_["addrrbp"]["rsp"] = 0x2dfc
or_["rsp"]["addrrbp"] = 0x2e01
gendict(or_, "addrrsp")
or_["addrrsp"]["rsp"] = 0x2e06
or_["rsp"]["addrrsp"] = 0x2e0b
gendict(or_, "eax")
or_["eax"]["ebx"] = 0x2e10
or_["eax"]["ecx"] = 0x2e13
or_["eax"]["edx"] = 0x2e16
or_["eax"]["esi"] = 0x2e19
or_["eax"]["edi"] = 0x2e1c
or_["eax"]["ebp"] = 0x2e1f
or_["eax"]["esp"] = 0x2e22
gendict(or_, "addrrax")
or_["addrrax"]["eax"] = 0x2e25
or_["eax"]["addrrax"] = 0x2e28
gendict(or_, "addrrbx")
or_["addrrbx"]["eax"] = 0x2e2b
or_["eax"]["addrrbx"] = 0x2e2e
gendict(or_, "addrrcx")
or_["addrrcx"]["eax"] = 0x2e31
or_["eax"]["addrrcx"] = 0x2e34
gendict(or_, "addrrdx")
or_["addrrdx"]["eax"] = 0x2e37
or_["eax"]["addrrdx"] = 0x2e3a
gendict(or_, "addrrsi")
or_["addrrsi"]["eax"] = 0x2e3d
or_["eax"]["addrrsi"] = 0x2e40
gendict(or_, "addrrdi")
or_["addrrdi"]["eax"] = 0x2e43
or_["eax"]["addrrdi"] = 0x2e46
gendict(or_, "addrrbp")
or_["addrrbp"]["eax"] = 0x2e49
or_["eax"]["addrrbp"] = 0x2e4d
gendict(or_, "addrrsp")
or_["addrrsp"]["eax"] = 0x2e51
or_["eax"]["addrrsp"] = 0x2e55
gendict(or_, "ebx")
or_["ebx"]["eax"] = 0x2e59
or_["ebx"]["ecx"] = 0x2e5c
or_["ebx"]["edx"] = 0x2e5f
or_["ebx"]["esi"] = 0x2e62
or_["ebx"]["edi"] = 0x2e65
or_["ebx"]["ebp"] = 0x2e68
or_["ebx"]["esp"] = 0x2e6b
gendict(or_, "addrrax")
or_["addrrax"]["ebx"] = 0x2e6e
or_["ebx"]["addrrax"] = 0x2e71
gendict(or_, "addrrbx")
or_["addrrbx"]["ebx"] = 0x2e74
or_["ebx"]["addrrbx"] = 0x2e77
gendict(or_, "addrrcx")
or_["addrrcx"]["ebx"] = 0x2e7a
or_["ebx"]["addrrcx"] = 0x2e7d
gendict(or_, "addrrdx")
or_["addrrdx"]["ebx"] = 0x2e80
or_["ebx"]["addrrdx"] = 0x2e83
gendict(or_, "addrrsi")
or_["addrrsi"]["ebx"] = 0x2e86
or_["ebx"]["addrrsi"] = 0x2e89
gendict(or_, "addrrdi")
or_["addrrdi"]["ebx"] = 0x2e8c
or_["ebx"]["addrrdi"] = 0x2e8f
gendict(or_, "addrrbp")
or_["addrrbp"]["ebx"] = 0x2e92
or_["ebx"]["addrrbp"] = 0x2e96
gendict(or_, "addrrsp")
or_["addrrsp"]["ebx"] = 0x2e9a
or_["ebx"]["addrrsp"] = 0x2e9e
gendict(or_, "ecx")
or_["ecx"]["eax"] = 0x2ea2
or_["ecx"]["ebx"] = 0x2ea5
or_["ecx"]["edx"] = 0x2ea8
or_["ecx"]["esi"] = 0x2eab
or_["ecx"]["edi"] = 0x2eae
or_["ecx"]["ebp"] = 0x2eb1
or_["ecx"]["esp"] = 0x2eb4
gendict(or_, "addrrax")
or_["addrrax"]["ecx"] = 0x2eb7
or_["ecx"]["addrrax"] = 0x2eba
gendict(or_, "addrrbx")
or_["addrrbx"]["ecx"] = 0x2ebd
or_["ecx"]["addrrbx"] = 0x2ec0
gendict(or_, "addrrcx")
or_["addrrcx"]["ecx"] = 0x2ec3
or_["ecx"]["addrrcx"] = 0x2ec6
gendict(or_, "addrrdx")
or_["addrrdx"]["ecx"] = 0x2ec9
or_["ecx"]["addrrdx"] = 0x2ecc
gendict(or_, "addrrsi")
or_["addrrsi"]["ecx"] = 0x2ecf
or_["ecx"]["addrrsi"] = 0x2ed2
gendict(or_, "addrrdi")
or_["addrrdi"]["ecx"] = 0x2ed5
or_["ecx"]["addrrdi"] = 0x2ed8
gendict(or_, "addrrbp")
or_["addrrbp"]["ecx"] = 0x2edb
or_["ecx"]["addrrbp"] = 0x2edf
gendict(or_, "addrrsp")
or_["addrrsp"]["ecx"] = 0x2ee3
or_["ecx"]["addrrsp"] = 0x2ee7
gendict(or_, "edx")
or_["edx"]["eax"] = 0x2eeb
or_["edx"]["ebx"] = 0x2eee
or_["edx"]["ecx"] = 0x2ef1
or_["edx"]["esi"] = 0x2ef4
or_["edx"]["edi"] = 0x2ef7
or_["edx"]["ebp"] = 0x2efa
or_["edx"]["esp"] = 0x2efd
gendict(or_, "addrrax")
or_["addrrax"]["edx"] = 0x2f00
or_["edx"]["addrrax"] = 0x2f03
gendict(or_, "addrrbx")
or_["addrrbx"]["edx"] = 0x2f06
or_["edx"]["addrrbx"] = 0x2f09
gendict(or_, "addrrcx")
or_["addrrcx"]["edx"] = 0x2f0c
or_["edx"]["addrrcx"] = 0x2f0f
gendict(or_, "addrrdx")
or_["addrrdx"]["edx"] = 0x2f12
or_["edx"]["addrrdx"] = 0x2f15
gendict(or_, "addrrsi")
or_["addrrsi"]["edx"] = 0x2f18
or_["edx"]["addrrsi"] = 0x2f1b
gendict(or_, "addrrdi")
or_["addrrdi"]["edx"] = 0x2f1e
or_["edx"]["addrrdi"] = 0x2f21
gendict(or_, "addrrbp")
or_["addrrbp"]["edx"] = 0x2f24
or_["edx"]["addrrbp"] = 0x2f28
gendict(or_, "addrrsp")
or_["addrrsp"]["edx"] = 0x2f2c
or_["edx"]["addrrsp"] = 0x2f30
gendict(or_, "esi")
or_["esi"]["eax"] = 0x2f34
or_["esi"]["ebx"] = 0x2f37
or_["esi"]["ecx"] = 0x2f3a
or_["esi"]["edx"] = 0x2f3d
or_["esi"]["edi"] = 0x2f40
or_["esi"]["ebp"] = 0x2f43
or_["esi"]["esp"] = 0x2f46
gendict(or_, "addrrax")
or_["addrrax"]["esi"] = 0x2f49
or_["esi"]["addrrax"] = 0x2f4c
gendict(or_, "addrrbx")
or_["addrrbx"]["esi"] = 0x2f4f
or_["esi"]["addrrbx"] = 0x2f52
gendict(or_, "addrrcx")
or_["addrrcx"]["esi"] = 0x2f55
or_["esi"]["addrrcx"] = 0x2f58
gendict(or_, "addrrdx")
or_["addrrdx"]["esi"] = 0x2f5b
or_["esi"]["addrrdx"] = 0x2f5e
gendict(or_, "addrrsi")
or_["addrrsi"]["esi"] = 0x2f61
or_["esi"]["addrrsi"] = 0x2f64
gendict(or_, "addrrdi")
or_["addrrdi"]["esi"] = 0x2f67
or_["esi"]["addrrdi"] = 0x2f6a
gendict(or_, "addrrbp")
or_["addrrbp"]["esi"] = 0x2f6d
or_["esi"]["addrrbp"] = 0x2f71
gendict(or_, "addrrsp")
or_["addrrsp"]["esi"] = 0x2f75
or_["esi"]["addrrsp"] = 0x2f79
gendict(or_, "edi")
or_["edi"]["eax"] = 0x2f7d
or_["edi"]["ebx"] = 0x2f80
or_["edi"]["ecx"] = 0x2f83
or_["edi"]["edx"] = 0x2f86
or_["edi"]["esi"] = 0x2f89
or_["edi"]["ebp"] = 0x2f8c
or_["edi"]["esp"] = 0x2f8f
gendict(or_, "addrrax")
or_["addrrax"]["edi"] = 0x2f92
or_["edi"]["addrrax"] = 0x2f95
gendict(or_, "addrrbx")
or_["addrrbx"]["edi"] = 0x2f98
or_["edi"]["addrrbx"] = 0x2f9b
gendict(or_, "addrrcx")
or_["addrrcx"]["edi"] = 0x2f9e
or_["edi"]["addrrcx"] = 0x2fa1
gendict(or_, "addrrdx")
or_["addrrdx"]["edi"] = 0x2fa4
or_["edi"]["addrrdx"] = 0x2fa7
gendict(or_, "addrrsi")
or_["addrrsi"]["edi"] = 0x2faa
or_["edi"]["addrrsi"] = 0x2fad
gendict(or_, "addrrdi")
or_["addrrdi"]["edi"] = 0x2fb0
or_["edi"]["addrrdi"] = 0x2fb3
gendict(or_, "addrrbp")
or_["addrrbp"]["edi"] = 0x2fb6
or_["edi"]["addrrbp"] = 0x2fba
gendict(or_, "addrrsp")
or_["addrrsp"]["edi"] = 0x2fbe
or_["edi"]["addrrsp"] = 0x2fc2
gendict(or_, "ebp")
or_["ebp"]["eax"] = 0x2fc6
or_["ebp"]["ebx"] = 0x2fc9
or_["ebp"]["ecx"] = 0x2fcc
or_["ebp"]["edx"] = 0x2fcf
or_["ebp"]["esi"] = 0x2fd2
or_["ebp"]["edi"] = 0x2fd5
or_["ebp"]["esp"] = 0x2fd8
gendict(or_, "addrrax")
or_["addrrax"]["ebp"] = 0x2fdb
or_["ebp"]["addrrax"] = 0x2fde
gendict(or_, "addrrbx")
or_["addrrbx"]["ebp"] = 0x2fe1
or_["ebp"]["addrrbx"] = 0x2fe4
gendict(or_, "addrrcx")
or_["addrrcx"]["ebp"] = 0x2fe7
or_["ebp"]["addrrcx"] = 0x2fea
gendict(or_, "addrrdx")
or_["addrrdx"]["ebp"] = 0x2fed
or_["ebp"]["addrrdx"] = 0x2ff0
gendict(or_, "addrrsi")
or_["addrrsi"]["ebp"] = 0x2ff3
or_["ebp"]["addrrsi"] = 0x2ff6
gendict(or_, "addrrdi")
or_["addrrdi"]["ebp"] = 0x2ff9
or_["ebp"]["addrrdi"] = 0x2ffc
gendict(or_, "addrrbp")
or_["addrrbp"]["ebp"] = 0x2fff
or_["ebp"]["addrrbp"] = 0x3003
gendict(or_, "addrrsp")
or_["addrrsp"]["ebp"] = 0x3007
or_["ebp"]["addrrsp"] = 0x300b
gendict(or_, "esp")
or_["esp"]["eax"] = 0x300f
or_["esp"]["ebx"] = 0x3012
or_["esp"]["ecx"] = 0x3015
or_["esp"]["edx"] = 0x3018
or_["esp"]["esi"] = 0x301b
or_["esp"]["edi"] = 0x301e
or_["esp"]["ebp"] = 0x3021
gendict(or_, "addrrax")
or_["addrrax"]["esp"] = 0x3024
or_["esp"]["addrrax"] = 0x3027
gendict(or_, "addrrbx")
or_["addrrbx"]["esp"] = 0x302a
or_["esp"]["addrrbx"] = 0x302d
gendict(or_, "addrrcx")
or_["addrrcx"]["esp"] = 0x3030
or_["esp"]["addrrcx"] = 0x3033
gendict(or_, "addrrdx")
or_["addrrdx"]["esp"] = 0x3036
or_["esp"]["addrrdx"] = 0x3039
gendict(or_, "addrrsi")
or_["addrrsi"]["esp"] = 0x303c
or_["esp"]["addrrsi"] = 0x303f
gendict(or_, "addrrdi")
or_["addrrdi"]["esp"] = 0x3042
or_["esp"]["addrrdi"] = 0x3045
gendict(or_, "addrrbp")
or_["addrrbp"]["esp"] = 0x3048
or_["esp"]["addrrbp"] = 0x304c
gendict(or_, "addrrsp")
or_["addrrsp"]["esp"] = 0x3050
or_["esp"]["addrrsp"] = 0x3054
gendict(or_, "ax")
or_["ax"]["bx"] = 0x3058
or_["ax"]["cx"] = 0x305c
or_["ax"]["dx"] = 0x3060
or_["ax"]["si"] = 0x3064
or_["ax"]["di"] = 0x3068
or_["ax"]["bp"] = 0x306c
or_["ax"]["sp"] = 0x3070
gendict(or_, "addrrax")
or_["addrrax"]["ax"] = 0x3074
or_["ax"]["addrrax"] = 0x3078
gendict(or_, "addrrbx")
or_["addrrbx"]["ax"] = 0x307c
or_["ax"]["addrrbx"] = 0x3080
gendict(or_, "addrrcx")
or_["addrrcx"]["ax"] = 0x3084
or_["ax"]["addrrcx"] = 0x3088
gendict(or_, "addrrdx")
or_["addrrdx"]["ax"] = 0x308c
or_["ax"]["addrrdx"] = 0x3090
gendict(or_, "addrrsi")
or_["addrrsi"]["ax"] = 0x3094
or_["ax"]["addrrsi"] = 0x3098
gendict(or_, "addrrdi")
or_["addrrdi"]["ax"] = 0x309c
or_["ax"]["addrrdi"] = 0x30a0
gendict(or_, "addrrbp")
or_["addrrbp"]["ax"] = 0x30a4
or_["ax"]["addrrbp"] = 0x30a9
gendict(or_, "addrrsp")
or_["addrrsp"]["ax"] = 0x30ae
or_["ax"]["addrrsp"] = 0x30b3
gendict(or_, "bx")
or_["bx"]["ax"] = 0x30b8
or_["bx"]["cx"] = 0x30bc
or_["bx"]["dx"] = 0x30c0
or_["bx"]["si"] = 0x30c4
or_["bx"]["di"] = 0x30c8
or_["bx"]["bp"] = 0x30cc
or_["bx"]["sp"] = 0x30d0
gendict(or_, "addrrax")
or_["addrrax"]["bx"] = 0x30d4
or_["bx"]["addrrax"] = 0x30d8
gendict(or_, "addrrbx")
or_["addrrbx"]["bx"] = 0x30dc
or_["bx"]["addrrbx"] = 0x30e0
gendict(or_, "addrrcx")
or_["addrrcx"]["bx"] = 0x30e4
or_["bx"]["addrrcx"] = 0x30e8
gendict(or_, "addrrdx")
or_["addrrdx"]["bx"] = 0x30ec
or_["bx"]["addrrdx"] = 0x30f0
gendict(or_, "addrrsi")
or_["addrrsi"]["bx"] = 0x30f4
or_["bx"]["addrrsi"] = 0x30f8
gendict(or_, "addrrdi")
or_["addrrdi"]["bx"] = 0x30fc
or_["bx"]["addrrdi"] = 0x3100
gendict(or_, "addrrbp")
or_["addrrbp"]["bx"] = 0x3104
or_["bx"]["addrrbp"] = 0x3109
gendict(or_, "addrrsp")
or_["addrrsp"]["bx"] = 0x310e
or_["bx"]["addrrsp"] = 0x3113
gendict(or_, "cx")
or_["cx"]["ax"] = 0x3118
or_["cx"]["bx"] = 0x311c
or_["cx"]["dx"] = 0x3120
or_["cx"]["si"] = 0x3124
or_["cx"]["di"] = 0x3128
or_["cx"]["bp"] = 0x312c
or_["cx"]["sp"] = 0x3130
gendict(or_, "addrrax")
or_["addrrax"]["cx"] = 0x3134
or_["cx"]["addrrax"] = 0x3138
gendict(or_, "addrrbx")
or_["addrrbx"]["cx"] = 0x313c
or_["cx"]["addrrbx"] = 0x3140
gendict(or_, "addrrcx")
or_["addrrcx"]["cx"] = 0x3144
or_["cx"]["addrrcx"] = 0x3148
gendict(or_, "addrrdx")
or_["addrrdx"]["cx"] = 0x314c
or_["cx"]["addrrdx"] = 0x3150
gendict(or_, "addrrsi")
or_["addrrsi"]["cx"] = 0x3154
or_["cx"]["addrrsi"] = 0x3158
gendict(or_, "addrrdi")
or_["addrrdi"]["cx"] = 0x315c
or_["cx"]["addrrdi"] = 0x3160
gendict(or_, "addrrbp")
or_["addrrbp"]["cx"] = 0x3164
or_["cx"]["addrrbp"] = 0x3169
gendict(or_, "addrrsp")
or_["addrrsp"]["cx"] = 0x316e
or_["cx"]["addrrsp"] = 0x3173
gendict(or_, "dx")
or_["dx"]["ax"] = 0x3178
or_["dx"]["bx"] = 0x317c
or_["dx"]["cx"] = 0x3180
or_["dx"]["si"] = 0x3184
or_["dx"]["di"] = 0x3188
or_["dx"]["bp"] = 0x318c
or_["dx"]["sp"] = 0x3190
gendict(or_, "addrrax")
or_["addrrax"]["dx"] = 0x3194
or_["dx"]["addrrax"] = 0x3198
gendict(or_, "addrrbx")
or_["addrrbx"]["dx"] = 0x319c
or_["dx"]["addrrbx"] = 0x31a0
gendict(or_, "addrrcx")
or_["addrrcx"]["dx"] = 0x31a4
or_["dx"]["addrrcx"] = 0x31a8
gendict(or_, "addrrdx")
or_["addrrdx"]["dx"] = 0x31ac
or_["dx"]["addrrdx"] = 0x31b0
gendict(or_, "addrrsi")
or_["addrrsi"]["dx"] = 0x31b4
or_["dx"]["addrrsi"] = 0x31b8
gendict(or_, "addrrdi")
or_["addrrdi"]["dx"] = 0x31bc
or_["dx"]["addrrdi"] = 0x31c0
gendict(or_, "addrrbp")
or_["addrrbp"]["dx"] = 0x31c4
or_["dx"]["addrrbp"] = 0x31c9
gendict(or_, "addrrsp")
or_["addrrsp"]["dx"] = 0x31ce
or_["dx"]["addrrsp"] = 0x31d3
gendict(or_, "si")
or_["si"]["ax"] = 0x31d8
or_["si"]["bx"] = 0x31dc
or_["si"]["cx"] = 0x31e0
or_["si"]["dx"] = 0x31e4
or_["si"]["di"] = 0x31e8
or_["si"]["bp"] = 0x31ec
or_["si"]["sp"] = 0x31f0
gendict(or_, "addrrax")
or_["addrrax"]["si"] = 0x31f4
or_["si"]["addrrax"] = 0x31f8
gendict(or_, "addrrbx")
or_["addrrbx"]["si"] = 0x31fc
or_["si"]["addrrbx"] = 0x3200
gendict(or_, "addrrcx")
or_["addrrcx"]["si"] = 0x3204
or_["si"]["addrrcx"] = 0x3208
gendict(or_, "addrrdx")
or_["addrrdx"]["si"] = 0x320c
or_["si"]["addrrdx"] = 0x3210
gendict(or_, "addrrsi")
or_["addrrsi"]["si"] = 0x3214
or_["si"]["addrrsi"] = 0x3218
gendict(or_, "addrrdi")
or_["addrrdi"]["si"] = 0x321c
or_["si"]["addrrdi"] = 0x3220
gendict(or_, "addrrbp")
or_["addrrbp"]["si"] = 0x3224
or_["si"]["addrrbp"] = 0x3229
gendict(or_, "addrrsp")
or_["addrrsp"]["si"] = 0x322e
or_["si"]["addrrsp"] = 0x3233
gendict(or_, "di")
or_["di"]["ax"] = 0x3238
or_["di"]["bx"] = 0x323c
or_["di"]["cx"] = 0x3240
or_["di"]["dx"] = 0x3244
or_["di"]["si"] = 0x3248
or_["di"]["bp"] = 0x324c
or_["di"]["sp"] = 0x3250
gendict(or_, "addrrax")
or_["addrrax"]["di"] = 0x3254
or_["di"]["addrrax"] = 0x3258
gendict(or_, "addrrbx")
or_["addrrbx"]["di"] = 0x325c
or_["di"]["addrrbx"] = 0x3260
gendict(or_, "addrrcx")
or_["addrrcx"]["di"] = 0x3264
or_["di"]["addrrcx"] = 0x3268
gendict(or_, "addrrdx")
or_["addrrdx"]["di"] = 0x326c
or_["di"]["addrrdx"] = 0x3270
gendict(or_, "addrrsi")
or_["addrrsi"]["di"] = 0x3274
or_["di"]["addrrsi"] = 0x3278
gendict(or_, "addrrdi")
or_["addrrdi"]["di"] = 0x327c
or_["di"]["addrrdi"] = 0x3280
gendict(or_, "addrrbp")
or_["addrrbp"]["di"] = 0x3284
or_["di"]["addrrbp"] = 0x3289
gendict(or_, "addrrsp")
or_["addrrsp"]["di"] = 0x328e
or_["di"]["addrrsp"] = 0x3293
gendict(or_, "bp")
or_["bp"]["ax"] = 0x3298
or_["bp"]["bx"] = 0x329c
or_["bp"]["cx"] = 0x32a0
or_["bp"]["dx"] = 0x32a4
or_["bp"]["si"] = 0x32a8
or_["bp"]["di"] = 0x32ac
or_["bp"]["sp"] = 0x32b0
gendict(or_, "addrrax")
or_["addrrax"]["bp"] = 0x32b4
or_["bp"]["addrrax"] = 0x32b8
gendict(or_, "addrrbx")
or_["addrrbx"]["bp"] = 0x32bc
or_["bp"]["addrrbx"] = 0x32c0
gendict(or_, "addrrcx")
or_["addrrcx"]["bp"] = 0x32c4
or_["bp"]["addrrcx"] = 0x32c8
gendict(or_, "addrrdx")
or_["addrrdx"]["bp"] = 0x32cc
or_["bp"]["addrrdx"] = 0x32d0
gendict(or_, "addrrsi")
or_["addrrsi"]["bp"] = 0x32d4
or_["bp"]["addrrsi"] = 0x32d8
gendict(or_, "addrrdi")
or_["addrrdi"]["bp"] = 0x32dc
or_["bp"]["addrrdi"] = 0x32e0
gendict(or_, "addrrbp")
or_["addrrbp"]["bp"] = 0x32e4
or_["bp"]["addrrbp"] = 0x32e9
gendict(or_, "addrrsp")
or_["addrrsp"]["bp"] = 0x32ee
or_["bp"]["addrrsp"] = 0x32f3
gendict(or_, "sp")
or_["sp"]["ax"] = 0x32f8
or_["sp"]["bx"] = 0x32fc
or_["sp"]["cx"] = 0x3300
or_["sp"]["dx"] = 0x3304
or_["sp"]["si"] = 0x3308
or_["sp"]["di"] = 0x330c
or_["sp"]["bp"] = 0x3310
gendict(or_, "addrrax")
or_["addrrax"]["sp"] = 0x3314
or_["sp"]["addrrax"] = 0x3318
gendict(or_, "addrrbx")
or_["addrrbx"]["sp"] = 0x331c
or_["sp"]["addrrbx"] = 0x3320
gendict(or_, "addrrcx")
or_["addrrcx"]["sp"] = 0x3324
or_["sp"]["addrrcx"] = 0x3328
gendict(or_, "addrrdx")
or_["addrrdx"]["sp"] = 0x332c
or_["sp"]["addrrdx"] = 0x3330
gendict(or_, "addrrsi")
or_["addrrsi"]["sp"] = 0x3334
or_["sp"]["addrrsi"] = 0x3338
gendict(or_, "addrrdi")
or_["addrrdi"]["sp"] = 0x333c
or_["sp"]["addrrdi"] = 0x3340
gendict(or_, "addrrbp")
or_["addrrbp"]["sp"] = 0x3344
or_["sp"]["addrrbp"] = 0x3349
gendict(or_, "addrrsp")
or_["addrrsp"]["sp"] = 0x334e
or_["sp"]["addrrsp"] = 0x3353
gendict(or_, "ah")
or_["ah"]["bh"] = 0x3358
or_["ah"]["ch"] = 0x335b
or_["ah"]["dh"] = 0x335e
gendict(or_, "addrrax")
or_["addrrax"]["ah"] = 0x3361
or_["ah"]["addrrax"] = 0x3364
gendict(or_, "addrrbx")
or_["addrrbx"]["ah"] = 0x3367
or_["ah"]["addrrbx"] = 0x336a
gendict(or_, "addrrcx")
or_["addrrcx"]["ah"] = 0x336d
or_["ah"]["addrrcx"] = 0x3370
gendict(or_, "addrrdx")
or_["addrrdx"]["ah"] = 0x3373
or_["ah"]["addrrdx"] = 0x3376
gendict(or_, "addrrsi")
or_["addrrsi"]["ah"] = 0x3379
or_["ah"]["addrrsi"] = 0x337c
gendict(or_, "addrrdi")
or_["addrrdi"]["ah"] = 0x337f
or_["ah"]["addrrdi"] = 0x3382
gendict(or_, "addrrbp")
or_["addrrbp"]["ah"] = 0x3385
or_["ah"]["addrrbp"] = 0x3389
gendict(or_, "addrrsp")
or_["addrrsp"]["ah"] = 0x338d
or_["ah"]["addrrsp"] = 0x3391
gendict(or_, "bh")
or_["bh"]["ah"] = 0x3395
or_["bh"]["ch"] = 0x3398
or_["bh"]["dh"] = 0x339b
gendict(or_, "addrrax")
or_["addrrax"]["bh"] = 0x339e
or_["bh"]["addrrax"] = 0x33a1
gendict(or_, "addrrbx")
or_["addrrbx"]["bh"] = 0x33a4
or_["bh"]["addrrbx"] = 0x33a7
gendict(or_, "addrrcx")
or_["addrrcx"]["bh"] = 0x33aa
or_["bh"]["addrrcx"] = 0x33ad
gendict(or_, "addrrdx")
or_["addrrdx"]["bh"] = 0x33b0
or_["bh"]["addrrdx"] = 0x33b3
gendict(or_, "addrrsi")
or_["addrrsi"]["bh"] = 0x33b6
or_["bh"]["addrrsi"] = 0x33b9
gendict(or_, "addrrdi")
or_["addrrdi"]["bh"] = 0x33bc
or_["bh"]["addrrdi"] = 0x33bf
gendict(or_, "addrrbp")
or_["addrrbp"]["bh"] = 0x33c2
or_["bh"]["addrrbp"] = 0x33c6
gendict(or_, "addrrsp")
or_["addrrsp"]["bh"] = 0x33ca
or_["bh"]["addrrsp"] = 0x33ce
gendict(or_, "ch")
or_["ch"]["ah"] = 0x33d2
or_["ch"]["bh"] = 0x33d5
or_["ch"]["dh"] = 0x33d8
gendict(or_, "addrrax")
or_["addrrax"]["ch"] = 0x33db
or_["ch"]["addrrax"] = 0x33de
gendict(or_, "addrrbx")
or_["addrrbx"]["ch"] = 0x33e1
or_["ch"]["addrrbx"] = 0x33e4
gendict(or_, "addrrcx")
or_["addrrcx"]["ch"] = 0x33e7
or_["ch"]["addrrcx"] = 0x33ea
gendict(or_, "addrrdx")
or_["addrrdx"]["ch"] = 0x33ed
or_["ch"]["addrrdx"] = 0x33f0
gendict(or_, "addrrsi")
or_["addrrsi"]["ch"] = 0x33f3
or_["ch"]["addrrsi"] = 0x33f6
gendict(or_, "addrrdi")
or_["addrrdi"]["ch"] = 0x33f9
or_["ch"]["addrrdi"] = 0x33fc
gendict(or_, "addrrbp")
or_["addrrbp"]["ch"] = 0x33ff
or_["ch"]["addrrbp"] = 0x3403
gendict(or_, "addrrsp")
or_["addrrsp"]["ch"] = 0x3407
or_["ch"]["addrrsp"] = 0x340b
gendict(or_, "dh")
or_["dh"]["ah"] = 0x340f
or_["dh"]["bh"] = 0x3412
or_["dh"]["ch"] = 0x3415
gendict(or_, "addrrax")
or_["addrrax"]["dh"] = 0x3418
or_["dh"]["addrrax"] = 0x341b
gendict(or_, "addrrbx")
or_["addrrbx"]["dh"] = 0x341e
or_["dh"]["addrrbx"] = 0x3421
gendict(or_, "addrrcx")
or_["addrrcx"]["dh"] = 0x3424
or_["dh"]["addrrcx"] = 0x3427
gendict(or_, "addrrdx")
or_["addrrdx"]["dh"] = 0x342a
or_["dh"]["addrrdx"] = 0x342d
gendict(or_, "addrrsi")
or_["addrrsi"]["dh"] = 0x3430
or_["dh"]["addrrsi"] = 0x3433
gendict(or_, "addrrdi")
or_["addrrdi"]["dh"] = 0x3436
or_["dh"]["addrrdi"] = 0x3439
gendict(or_, "addrrbp")
or_["addrrbp"]["dh"] = 0x343c
or_["dh"]["addrrbp"] = 0x3440
gendict(or_, "addrrsp")
or_["addrrsp"]["dh"] = 0x3444
or_["dh"]["addrrsp"] = 0x3448
gendict(or_, "al")
or_["al"]["bl"] = 0x344c
or_["al"]["cl"] = 0x344f
or_["al"]["dl"] = 0x3452
gendict(or_, "addrrax")
or_["addrrax"]["al"] = 0x3455
or_["al"]["addrrax"] = 0x3458
gendict(or_, "addrrbx")
or_["addrrbx"]["al"] = 0x345b
or_["al"]["addrrbx"] = 0x345e
gendict(or_, "addrrcx")
or_["addrrcx"]["al"] = 0x3461
or_["al"]["addrrcx"] = 0x3464
gendict(or_, "addrrdx")
or_["addrrdx"]["al"] = 0x3467
or_["al"]["addrrdx"] = 0x346a
gendict(or_, "addrrsi")
or_["addrrsi"]["al"] = 0x346d
or_["al"]["addrrsi"] = 0x3470
gendict(or_, "addrrdi")
or_["addrrdi"]["al"] = 0x3473
or_["al"]["addrrdi"] = 0x3476
gendict(or_, "addrrbp")
or_["addrrbp"]["al"] = 0x3479
or_["al"]["addrrbp"] = 0x347d
gendict(or_, "addrrsp")
or_["addrrsp"]["al"] = 0x3481
or_["al"]["addrrsp"] = 0x3485
gendict(or_, "bl")
or_["bl"]["al"] = 0x3489
or_["bl"]["cl"] = 0x348c
or_["bl"]["dl"] = 0x348f
gendict(or_, "addrrax")
or_["addrrax"]["bl"] = 0x3492
or_["bl"]["addrrax"] = 0x3495
gendict(or_, "addrrbx")
or_["addrrbx"]["bl"] = 0x3498
or_["bl"]["addrrbx"] = 0x349b
gendict(or_, "addrrcx")
or_["addrrcx"]["bl"] = 0x349e
or_["bl"]["addrrcx"] = 0x34a1
gendict(or_, "addrrdx")
or_["addrrdx"]["bl"] = 0x34a4
or_["bl"]["addrrdx"] = 0x34a7
gendict(or_, "addrrsi")
or_["addrrsi"]["bl"] = 0x34aa
or_["bl"]["addrrsi"] = 0x34ad
gendict(or_, "addrrdi")
or_["addrrdi"]["bl"] = 0x34b0
or_["bl"]["addrrdi"] = 0x34b3
gendict(or_, "addrrbp")
or_["addrrbp"]["bl"] = 0x34b6
or_["bl"]["addrrbp"] = 0x34ba
gendict(or_, "addrrsp")
or_["addrrsp"]["bl"] = 0x34be
or_["bl"]["addrrsp"] = 0x34c2
gendict(or_, "cl")
or_["cl"]["al"] = 0x34c6
or_["cl"]["bl"] = 0x34c9
or_["cl"]["dl"] = 0x34cc
gendict(or_, "addrrax")
or_["addrrax"]["cl"] = 0x34cf
or_["cl"]["addrrax"] = 0x34d2
gendict(or_, "addrrbx")
or_["addrrbx"]["cl"] = 0x34d5
or_["cl"]["addrrbx"] = 0x34d8
gendict(or_, "addrrcx")
or_["addrrcx"]["cl"] = 0x34db
or_["cl"]["addrrcx"] = 0x34de
gendict(or_, "addrrdx")
or_["addrrdx"]["cl"] = 0x34e1
or_["cl"]["addrrdx"] = 0x34e4
gendict(or_, "addrrsi")
or_["addrrsi"]["cl"] = 0x34e7
or_["cl"]["addrrsi"] = 0x34ea
gendict(or_, "addrrdi")
or_["addrrdi"]["cl"] = 0x34ed
or_["cl"]["addrrdi"] = 0x34f0
gendict(or_, "addrrbp")
or_["addrrbp"]["cl"] = 0x34f3
or_["cl"]["addrrbp"] = 0x34f7
gendict(or_, "addrrsp")
or_["addrrsp"]["cl"] = 0x34fb
or_["cl"]["addrrsp"] = 0x34ff
gendict(or_, "dl")
or_["dl"]["al"] = 0x3503
or_["dl"]["bl"] = 0x3506
or_["dl"]["cl"] = 0x3509
gendict(or_, "addrrax")
or_["addrrax"]["dl"] = 0x350c
or_["dl"]["addrrax"] = 0x350f
gendict(or_, "addrrbx")
or_["addrrbx"]["dl"] = 0x3512
or_["dl"]["addrrbx"] = 0x3515
gendict(or_, "addrrcx")
or_["addrrcx"]["dl"] = 0x3518
or_["dl"]["addrrcx"] = 0x351b
gendict(or_, "addrrdx")
or_["addrrdx"]["dl"] = 0x351e
or_["dl"]["addrrdx"] = 0x3521
gendict(or_, "addrrsi")
or_["addrrsi"]["dl"] = 0x3524
or_["dl"]["addrrsi"] = 0x3527
gendict(or_, "addrrdi")
or_["addrrdi"]["dl"] = 0x352a
or_["dl"]["addrrdi"] = 0x352d
gendict(or_, "addrrbp")
or_["addrrbp"]["dl"] = 0x3530
or_["dl"]["addrrbp"] = 0x3534
gendict(or_, "addrrsp")
or_["addrrsp"]["dl"] = 0x3538
or_["dl"]["addrrsp"] = 0x353c
xor_ = {}
gendict(xor_, "rax")
xor_["rax"]["rbx"] = 0x3540
xor_["rax"]["rcx"] = 0x3544
xor_["rax"]["rdx"] = 0x3548
xor_["rax"]["rsi"] = 0x354c
xor_["rax"]["rdi"] = 0x3550
xor_["rax"]["rbp"] = 0x3554
xor_["rax"]["rsp"] = 0x3558
gendict(xor_, "addrrax")
xor_["addrrax"]["rax"] = 0x355c
xor_["rax"]["addrrax"] = 0x3560
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rax"] = 0x3564
xor_["rax"]["addrrbx"] = 0x3568
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rax"] = 0x356c
xor_["rax"]["addrrcx"] = 0x3570
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rax"] = 0x3574
xor_["rax"]["addrrdx"] = 0x3578
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rax"] = 0x357c
xor_["rax"]["addrrsi"] = 0x3580
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rax"] = 0x3584
xor_["rax"]["addrrdi"] = 0x3588
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rax"] = 0x358c
xor_["rax"]["addrrbp"] = 0x3591
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rax"] = 0x3596
xor_["rax"]["addrrsp"] = 0x359b
gendict(xor_, "rbx")
xor_["rbx"]["rax"] = 0x35a0
xor_["rbx"]["rcx"] = 0x35a4
xor_["rbx"]["rdx"] = 0x35a8
xor_["rbx"]["rsi"] = 0x35ac
xor_["rbx"]["rdi"] = 0x35b0
xor_["rbx"]["rbp"] = 0x35b4
xor_["rbx"]["rsp"] = 0x35b8
gendict(xor_, "addrrax")
xor_["addrrax"]["rbx"] = 0x35bc
xor_["rbx"]["addrrax"] = 0x35c0
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rbx"] = 0x35c4
xor_["rbx"]["addrrbx"] = 0x35c8
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rbx"] = 0x35cc
xor_["rbx"]["addrrcx"] = 0x35d0
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rbx"] = 0x35d4
xor_["rbx"]["addrrdx"] = 0x35d8
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rbx"] = 0x35dc
xor_["rbx"]["addrrsi"] = 0x35e0
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rbx"] = 0x35e4
xor_["rbx"]["addrrdi"] = 0x35e8
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rbx"] = 0x35ec
xor_["rbx"]["addrrbp"] = 0x35f1
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rbx"] = 0x35f6
xor_["rbx"]["addrrsp"] = 0x35fb
gendict(xor_, "rcx")
xor_["rcx"]["rax"] = 0x3600
xor_["rcx"]["rbx"] = 0x3604
xor_["rcx"]["rdx"] = 0x3608
xor_["rcx"]["rsi"] = 0x360c
xor_["rcx"]["rdi"] = 0x3610
xor_["rcx"]["rbp"] = 0x3614
xor_["rcx"]["rsp"] = 0x3618
gendict(xor_, "addrrax")
xor_["addrrax"]["rcx"] = 0x361c
xor_["rcx"]["addrrax"] = 0x3620
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rcx"] = 0x3624
xor_["rcx"]["addrrbx"] = 0x3628
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rcx"] = 0x362c
xor_["rcx"]["addrrcx"] = 0x3630
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rcx"] = 0x3634
xor_["rcx"]["addrrdx"] = 0x3638
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rcx"] = 0x363c
xor_["rcx"]["addrrsi"] = 0x3640
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rcx"] = 0x3644
xor_["rcx"]["addrrdi"] = 0x3648
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rcx"] = 0x364c
xor_["rcx"]["addrrbp"] = 0x3651
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rcx"] = 0x3656
xor_["rcx"]["addrrsp"] = 0x365b
gendict(xor_, "rdx")
xor_["rdx"]["rax"] = 0x3660
xor_["rdx"]["rbx"] = 0x3664
xor_["rdx"]["rcx"] = 0x3668
xor_["rdx"]["rsi"] = 0x366c
xor_["rdx"]["rdi"] = 0x3670
xor_["rdx"]["rbp"] = 0x3674
xor_["rdx"]["rsp"] = 0x3678
gendict(xor_, "addrrax")
xor_["addrrax"]["rdx"] = 0x367c
xor_["rdx"]["addrrax"] = 0x3680
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rdx"] = 0x3684
xor_["rdx"]["addrrbx"] = 0x3688
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rdx"] = 0x368c
xor_["rdx"]["addrrcx"] = 0x3690
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rdx"] = 0x3694
xor_["rdx"]["addrrdx"] = 0x3698
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rdx"] = 0x369c
xor_["rdx"]["addrrsi"] = 0x36a0
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rdx"] = 0x36a4
xor_["rdx"]["addrrdi"] = 0x36a8
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rdx"] = 0x36ac
xor_["rdx"]["addrrbp"] = 0x36b1
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rdx"] = 0x36b6
xor_["rdx"]["addrrsp"] = 0x36bb
gendict(xor_, "rsi")
xor_["rsi"]["rax"] = 0x36c0
xor_["rsi"]["rbx"] = 0x36c4
xor_["rsi"]["rcx"] = 0x36c8
xor_["rsi"]["rdx"] = 0x36cc
xor_["rsi"]["rdi"] = 0x36d0
xor_["rsi"]["rbp"] = 0x36d4
xor_["rsi"]["rsp"] = 0x36d8
gendict(xor_, "addrrax")
xor_["addrrax"]["rsi"] = 0x36dc
xor_["rsi"]["addrrax"] = 0x36e0
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rsi"] = 0x36e4
xor_["rsi"]["addrrbx"] = 0x36e8
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rsi"] = 0x36ec
xor_["rsi"]["addrrcx"] = 0x36f0
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rsi"] = 0x36f4
xor_["rsi"]["addrrdx"] = 0x36f8
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rsi"] = 0x36fc
xor_["rsi"]["addrrsi"] = 0x3700
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rsi"] = 0x3704
xor_["rsi"]["addrrdi"] = 0x3708
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rsi"] = 0x370c
xor_["rsi"]["addrrbp"] = 0x3711
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rsi"] = 0x3716
xor_["rsi"]["addrrsp"] = 0x371b
gendict(xor_, "rdi")
xor_["rdi"]["rax"] = 0x3720
xor_["rdi"]["rbx"] = 0x3724
xor_["rdi"]["rcx"] = 0x3728
xor_["rdi"]["rdx"] = 0x372c
xor_["rdi"]["rsi"] = 0x3730
xor_["rdi"]["rbp"] = 0x3734
xor_["rdi"]["rsp"] = 0x3738
gendict(xor_, "addrrax")
xor_["addrrax"]["rdi"] = 0x373c
xor_["rdi"]["addrrax"] = 0x3740
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rdi"] = 0x3744
xor_["rdi"]["addrrbx"] = 0x3748
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rdi"] = 0x374c
xor_["rdi"]["addrrcx"] = 0x3750
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rdi"] = 0x3754
xor_["rdi"]["addrrdx"] = 0x3758
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rdi"] = 0x375c
xor_["rdi"]["addrrsi"] = 0x3760
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rdi"] = 0x3764
xor_["rdi"]["addrrdi"] = 0x3768
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rdi"] = 0x376c
xor_["rdi"]["addrrbp"] = 0x3771
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rdi"] = 0x3776
xor_["rdi"]["addrrsp"] = 0x377b
gendict(xor_, "rbp")
xor_["rbp"]["rax"] = 0x3780
xor_["rbp"]["rbx"] = 0x3784
xor_["rbp"]["rcx"] = 0x3788
xor_["rbp"]["rdx"] = 0x378c
xor_["rbp"]["rsi"] = 0x3790
xor_["rbp"]["rdi"] = 0x3794
xor_["rbp"]["rsp"] = 0x3798
gendict(xor_, "addrrax")
xor_["addrrax"]["rbp"] = 0x379c
xor_["rbp"]["addrrax"] = 0x37a0
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rbp"] = 0x37a4
xor_["rbp"]["addrrbx"] = 0x37a8
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rbp"] = 0x37ac
xor_["rbp"]["addrrcx"] = 0x37b0
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rbp"] = 0x37b4
xor_["rbp"]["addrrdx"] = 0x37b8
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rbp"] = 0x37bc
xor_["rbp"]["addrrsi"] = 0x37c0
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rbp"] = 0x37c4
xor_["rbp"]["addrrdi"] = 0x37c8
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rbp"] = 0x37cc
xor_["rbp"]["addrrbp"] = 0x37d1
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rbp"] = 0x37d6
xor_["rbp"]["addrrsp"] = 0x37db
gendict(xor_, "rsp")
xor_["rsp"]["rax"] = 0x37e0
xor_["rsp"]["rbx"] = 0x37e4
xor_["rsp"]["rcx"] = 0x37e8
xor_["rsp"]["rdx"] = 0x37ec
xor_["rsp"]["rsi"] = 0x37f0
xor_["rsp"]["rdi"] = 0x37f4
xor_["rsp"]["rbp"] = 0x37f8
gendict(xor_, "addrrax")
xor_["addrrax"]["rsp"] = 0x37fc
xor_["rsp"]["addrrax"] = 0x3800
gendict(xor_, "addrrbx")
xor_["addrrbx"]["rsp"] = 0x3804
xor_["rsp"]["addrrbx"] = 0x3808
gendict(xor_, "addrrcx")
xor_["addrrcx"]["rsp"] = 0x380c
xor_["rsp"]["addrrcx"] = 0x3810
gendict(xor_, "addrrdx")
xor_["addrrdx"]["rsp"] = 0x3814
xor_["rsp"]["addrrdx"] = 0x3818
gendict(xor_, "addrrsi")
xor_["addrrsi"]["rsp"] = 0x381c
xor_["rsp"]["addrrsi"] = 0x3820
gendict(xor_, "addrrdi")
xor_["addrrdi"]["rsp"] = 0x3824
xor_["rsp"]["addrrdi"] = 0x3828
gendict(xor_, "addrrbp")
xor_["addrrbp"]["rsp"] = 0x382c
xor_["rsp"]["addrrbp"] = 0x3831
gendict(xor_, "addrrsp")
xor_["addrrsp"]["rsp"] = 0x3836
xor_["rsp"]["addrrsp"] = 0x383b
gendict(xor_, "eax")
xor_["eax"]["ebx"] = 0x3840
xor_["eax"]["ecx"] = 0x3843
xor_["eax"]["edx"] = 0x3846
xor_["eax"]["esi"] = 0x3849
xor_["eax"]["edi"] = 0x384c
xor_["eax"]["ebp"] = 0x384f
xor_["eax"]["esp"] = 0x3852
gendict(xor_, "addrrax")
xor_["addrrax"]["eax"] = 0x3855
xor_["eax"]["addrrax"] = 0x3858
gendict(xor_, "addrrbx")
xor_["addrrbx"]["eax"] = 0x385b
xor_["eax"]["addrrbx"] = 0x385e
gendict(xor_, "addrrcx")
xor_["addrrcx"]["eax"] = 0x3861
xor_["eax"]["addrrcx"] = 0x3864
gendict(xor_, "addrrdx")
xor_["addrrdx"]["eax"] = 0x3867
xor_["eax"]["addrrdx"] = 0x386a
gendict(xor_, "addrrsi")
xor_["addrrsi"]["eax"] = 0x386d
xor_["eax"]["addrrsi"] = 0x3870
gendict(xor_, "addrrdi")
xor_["addrrdi"]["eax"] = 0x3873
xor_["eax"]["addrrdi"] = 0x3876
gendict(xor_, "addrrbp")
xor_["addrrbp"]["eax"] = 0x3879
xor_["eax"]["addrrbp"] = 0x387d
gendict(xor_, "addrrsp")
xor_["addrrsp"]["eax"] = 0x3881
xor_["eax"]["addrrsp"] = 0x3885
gendict(xor_, "ebx")
xor_["ebx"]["eax"] = 0x3889
xor_["ebx"]["ecx"] = 0x388c
xor_["ebx"]["edx"] = 0x388f
xor_["ebx"]["esi"] = 0x3892
xor_["ebx"]["edi"] = 0x3895
xor_["ebx"]["ebp"] = 0x3898
xor_["ebx"]["esp"] = 0x389b
gendict(xor_, "addrrax")
xor_["addrrax"]["ebx"] = 0x389e
xor_["ebx"]["addrrax"] = 0x38a1
gendict(xor_, "addrrbx")
xor_["addrrbx"]["ebx"] = 0x38a4
xor_["ebx"]["addrrbx"] = 0x38a7
gendict(xor_, "addrrcx")
xor_["addrrcx"]["ebx"] = 0x38aa
xor_["ebx"]["addrrcx"] = 0x38ad
gendict(xor_, "addrrdx")
xor_["addrrdx"]["ebx"] = 0x38b0
xor_["ebx"]["addrrdx"] = 0x38b3
gendict(xor_, "addrrsi")
xor_["addrrsi"]["ebx"] = 0x38b6
xor_["ebx"]["addrrsi"] = 0x38b9
gendict(xor_, "addrrdi")
xor_["addrrdi"]["ebx"] = 0x38bc
xor_["ebx"]["addrrdi"] = 0x38bf
gendict(xor_, "addrrbp")
xor_["addrrbp"]["ebx"] = 0x38c2
xor_["ebx"]["addrrbp"] = 0x38c6
gendict(xor_, "addrrsp")
xor_["addrrsp"]["ebx"] = 0x38ca
xor_["ebx"]["addrrsp"] = 0x38ce
gendict(xor_, "ecx")
xor_["ecx"]["eax"] = 0x38d2
xor_["ecx"]["ebx"] = 0x38d5
xor_["ecx"]["edx"] = 0x38d8
xor_["ecx"]["esi"] = 0x38db
xor_["ecx"]["edi"] = 0x38de
xor_["ecx"]["ebp"] = 0x38e1
xor_["ecx"]["esp"] = 0x38e4
gendict(xor_, "addrrax")
xor_["addrrax"]["ecx"] = 0x38e7
xor_["ecx"]["addrrax"] = 0x38ea
gendict(xor_, "addrrbx")
xor_["addrrbx"]["ecx"] = 0x38ed
xor_["ecx"]["addrrbx"] = 0x38f0
gendict(xor_, "addrrcx")
xor_["addrrcx"]["ecx"] = 0x38f3
xor_["ecx"]["addrrcx"] = 0x38f6
gendict(xor_, "addrrdx")
xor_["addrrdx"]["ecx"] = 0x38f9
xor_["ecx"]["addrrdx"] = 0x38fc
gendict(xor_, "addrrsi")
xor_["addrrsi"]["ecx"] = 0x38ff
xor_["ecx"]["addrrsi"] = 0x3902
gendict(xor_, "addrrdi")
xor_["addrrdi"]["ecx"] = 0x3905
xor_["ecx"]["addrrdi"] = 0x3908
gendict(xor_, "addrrbp")
xor_["addrrbp"]["ecx"] = 0x390b
xor_["ecx"]["addrrbp"] = 0x390f
gendict(xor_, "addrrsp")
xor_["addrrsp"]["ecx"] = 0x3913
xor_["ecx"]["addrrsp"] = 0x3917
gendict(xor_, "edx")
xor_["edx"]["eax"] = 0x391b
xor_["edx"]["ebx"] = 0x391e
xor_["edx"]["ecx"] = 0x3921
xor_["edx"]["esi"] = 0x3924
xor_["edx"]["edi"] = 0x3927
xor_["edx"]["ebp"] = 0x392a
xor_["edx"]["esp"] = 0x392d
gendict(xor_, "addrrax")
xor_["addrrax"]["edx"] = 0x3930
xor_["edx"]["addrrax"] = 0x3933
gendict(xor_, "addrrbx")
xor_["addrrbx"]["edx"] = 0x3936
xor_["edx"]["addrrbx"] = 0x3939
gendict(xor_, "addrrcx")
xor_["addrrcx"]["edx"] = 0x393c
xor_["edx"]["addrrcx"] = 0x393f
gendict(xor_, "addrrdx")
xor_["addrrdx"]["edx"] = 0x3942
xor_["edx"]["addrrdx"] = 0x3945
gendict(xor_, "addrrsi")
xor_["addrrsi"]["edx"] = 0x3948
xor_["edx"]["addrrsi"] = 0x394b
gendict(xor_, "addrrdi")
xor_["addrrdi"]["edx"] = 0x394e
xor_["edx"]["addrrdi"] = 0x3951
gendict(xor_, "addrrbp")
xor_["addrrbp"]["edx"] = 0x3954
xor_["edx"]["addrrbp"] = 0x3958
gendict(xor_, "addrrsp")
xor_["addrrsp"]["edx"] = 0x395c
xor_["edx"]["addrrsp"] = 0x3960
gendict(xor_, "esi")
xor_["esi"]["eax"] = 0x3964
xor_["esi"]["ebx"] = 0x3967
xor_["esi"]["ecx"] = 0x396a
xor_["esi"]["edx"] = 0x396d
xor_["esi"]["edi"] = 0x3970
xor_["esi"]["ebp"] = 0x3973
xor_["esi"]["esp"] = 0x3976
gendict(xor_, "addrrax")
xor_["addrrax"]["esi"] = 0x3979
xor_["esi"]["addrrax"] = 0x397c
gendict(xor_, "addrrbx")
xor_["addrrbx"]["esi"] = 0x397f
xor_["esi"]["addrrbx"] = 0x3982
gendict(xor_, "addrrcx")
xor_["addrrcx"]["esi"] = 0x3985
xor_["esi"]["addrrcx"] = 0x3988
gendict(xor_, "addrrdx")
xor_["addrrdx"]["esi"] = 0x398b
xor_["esi"]["addrrdx"] = 0x398e
gendict(xor_, "addrrsi")
xor_["addrrsi"]["esi"] = 0x3991
xor_["esi"]["addrrsi"] = 0x3994
gendict(xor_, "addrrdi")
xor_["addrrdi"]["esi"] = 0x3997
xor_["esi"]["addrrdi"] = 0x399a
gendict(xor_, "addrrbp")
xor_["addrrbp"]["esi"] = 0x399d
xor_["esi"]["addrrbp"] = 0x39a1
gendict(xor_, "addrrsp")
xor_["addrrsp"]["esi"] = 0x39a5
xor_["esi"]["addrrsp"] = 0x39a9
gendict(xor_, "edi")
xor_["edi"]["eax"] = 0x39ad
xor_["edi"]["ebx"] = 0x39b0
xor_["edi"]["ecx"] = 0x39b3
xor_["edi"]["edx"] = 0x39b6
xor_["edi"]["esi"] = 0x39b9
xor_["edi"]["ebp"] = 0x39bc
xor_["edi"]["esp"] = 0x39bf
gendict(xor_, "addrrax")
xor_["addrrax"]["edi"] = 0x39c2
xor_["edi"]["addrrax"] = 0x39c5
gendict(xor_, "addrrbx")
xor_["addrrbx"]["edi"] = 0x39c8
xor_["edi"]["addrrbx"] = 0x39cb
gendict(xor_, "addrrcx")
xor_["addrrcx"]["edi"] = 0x39ce
xor_["edi"]["addrrcx"] = 0x39d1
gendict(xor_, "addrrdx")
xor_["addrrdx"]["edi"] = 0x39d4
xor_["edi"]["addrrdx"] = 0x39d7
gendict(xor_, "addrrsi")
xor_["addrrsi"]["edi"] = 0x39da
xor_["edi"]["addrrsi"] = 0x39dd
gendict(xor_, "addrrdi")
xor_["addrrdi"]["edi"] = 0x39e0
xor_["edi"]["addrrdi"] = 0x39e3
gendict(xor_, "addrrbp")
xor_["addrrbp"]["edi"] = 0x39e6
xor_["edi"]["addrrbp"] = 0x39ea
gendict(xor_, "addrrsp")
xor_["addrrsp"]["edi"] = 0x39ee
xor_["edi"]["addrrsp"] = 0x39f2
gendict(xor_, "ebp")
xor_["ebp"]["eax"] = 0x39f6
xor_["ebp"]["ebx"] = 0x39f9
xor_["ebp"]["ecx"] = 0x39fc
xor_["ebp"]["edx"] = 0x39ff
xor_["ebp"]["esi"] = 0x3a02
xor_["ebp"]["edi"] = 0x3a05
xor_["ebp"]["esp"] = 0x3a08
gendict(xor_, "addrrax")
xor_["addrrax"]["ebp"] = 0x3a0b
xor_["ebp"]["addrrax"] = 0x3a0e
gendict(xor_, "addrrbx")
xor_["addrrbx"]["ebp"] = 0x3a11
xor_["ebp"]["addrrbx"] = 0x3a14
gendict(xor_, "addrrcx")
xor_["addrrcx"]["ebp"] = 0x3a17
xor_["ebp"]["addrrcx"] = 0x3a1a
gendict(xor_, "addrrdx")
xor_["addrrdx"]["ebp"] = 0x3a1d
xor_["ebp"]["addrrdx"] = 0x3a20
gendict(xor_, "addrrsi")
xor_["addrrsi"]["ebp"] = 0x3a23
xor_["ebp"]["addrrsi"] = 0x3a26
gendict(xor_, "addrrdi")
xor_["addrrdi"]["ebp"] = 0x3a29
xor_["ebp"]["addrrdi"] = 0x3a2c
gendict(xor_, "addrrbp")
xor_["addrrbp"]["ebp"] = 0x3a2f
xor_["ebp"]["addrrbp"] = 0x3a33
gendict(xor_, "addrrsp")
xor_["addrrsp"]["ebp"] = 0x3a37
xor_["ebp"]["addrrsp"] = 0x3a3b
gendict(xor_, "esp")
xor_["esp"]["eax"] = 0x3a3f
xor_["esp"]["ebx"] = 0x3a42
xor_["esp"]["ecx"] = 0x3a45
xor_["esp"]["edx"] = 0x3a48
xor_["esp"]["esi"] = 0x3a4b
xor_["esp"]["edi"] = 0x3a4e
xor_["esp"]["ebp"] = 0x3a51
gendict(xor_, "addrrax")
xor_["addrrax"]["esp"] = 0x3a54
xor_["esp"]["addrrax"] = 0x3a57
gendict(xor_, "addrrbx")
xor_["addrrbx"]["esp"] = 0x3a5a
xor_["esp"]["addrrbx"] = 0x3a5d
gendict(xor_, "addrrcx")
xor_["addrrcx"]["esp"] = 0x3a60
xor_["esp"]["addrrcx"] = 0x3a63
gendict(xor_, "addrrdx")
xor_["addrrdx"]["esp"] = 0x3a66
xor_["esp"]["addrrdx"] = 0x3a69
gendict(xor_, "addrrsi")
xor_["addrrsi"]["esp"] = 0x3a6c
xor_["esp"]["addrrsi"] = 0x3a6f
gendict(xor_, "addrrdi")
xor_["addrrdi"]["esp"] = 0x3a72
xor_["esp"]["addrrdi"] = 0x3a75
gendict(xor_, "addrrbp")
xor_["addrrbp"]["esp"] = 0x3a78
xor_["esp"]["addrrbp"] = 0x3a7c
gendict(xor_, "addrrsp")
xor_["addrrsp"]["esp"] = 0x3a80
xor_["esp"]["addrrsp"] = 0x3a84
gendict(xor_, "ax")
xor_["ax"]["bx"] = 0x3a88
xor_["ax"]["cx"] = 0x3a8c
xor_["ax"]["dx"] = 0x3a90
xor_["ax"]["si"] = 0x3a94
xor_["ax"]["di"] = 0x3a98
xor_["ax"]["bp"] = 0x3a9c
xor_["ax"]["sp"] = 0x3aa0
gendict(xor_, "addrrax")
xor_["addrrax"]["ax"] = 0x3aa4
xor_["ax"]["addrrax"] = 0x3aa8
gendict(xor_, "addrrbx")
xor_["addrrbx"]["ax"] = 0x3aac
xor_["ax"]["addrrbx"] = 0x3ab0
gendict(xor_, "addrrcx")
xor_["addrrcx"]["ax"] = 0x3ab4
xor_["ax"]["addrrcx"] = 0x3ab8
gendict(xor_, "addrrdx")
xor_["addrrdx"]["ax"] = 0x3abc
xor_["ax"]["addrrdx"] = 0x3ac0
gendict(xor_, "addrrsi")
xor_["addrrsi"]["ax"] = 0x3ac4
xor_["ax"]["addrrsi"] = 0x3ac8
gendict(xor_, "addrrdi")
xor_["addrrdi"]["ax"] = 0x3acc
xor_["ax"]["addrrdi"] = 0x3ad0
gendict(xor_, "addrrbp")
xor_["addrrbp"]["ax"] = 0x3ad4
xor_["ax"]["addrrbp"] = 0x3ad9
gendict(xor_, "addrrsp")
xor_["addrrsp"]["ax"] = 0x3ade
xor_["ax"]["addrrsp"] = 0x3ae3
gendict(xor_, "bx")
xor_["bx"]["ax"] = 0x3ae8
xor_["bx"]["cx"] = 0x3aec
xor_["bx"]["dx"] = 0x3af0
xor_["bx"]["si"] = 0x3af4
xor_["bx"]["di"] = 0x3af8
xor_["bx"]["bp"] = 0x3afc
xor_["bx"]["sp"] = 0x3b00
gendict(xor_, "addrrax")
xor_["addrrax"]["bx"] = 0x3b04
xor_["bx"]["addrrax"] = 0x3b08
gendict(xor_, "addrrbx")
xor_["addrrbx"]["bx"] = 0x3b0c
xor_["bx"]["addrrbx"] = 0x3b10
gendict(xor_, "addrrcx")
xor_["addrrcx"]["bx"] = 0x3b14
xor_["bx"]["addrrcx"] = 0x3b18
gendict(xor_, "addrrdx")
xor_["addrrdx"]["bx"] = 0x3b1c
xor_["bx"]["addrrdx"] = 0x3b20
gendict(xor_, "addrrsi")
xor_["addrrsi"]["bx"] = 0x3b24
xor_["bx"]["addrrsi"] = 0x3b28
gendict(xor_, "addrrdi")
xor_["addrrdi"]["bx"] = 0x3b2c
xor_["bx"]["addrrdi"] = 0x3b30
gendict(xor_, "addrrbp")
xor_["addrrbp"]["bx"] = 0x3b34
xor_["bx"]["addrrbp"] = 0x3b39
gendict(xor_, "addrrsp")
xor_["addrrsp"]["bx"] = 0x3b3e
xor_["bx"]["addrrsp"] = 0x3b43
gendict(xor_, "cx")
xor_["cx"]["ax"] = 0x3b48
xor_["cx"]["bx"] = 0x3b4c
xor_["cx"]["dx"] = 0x3b50
xor_["cx"]["si"] = 0x3b54
xor_["cx"]["di"] = 0x3b58
xor_["cx"]["bp"] = 0x3b5c
xor_["cx"]["sp"] = 0x3b60
gendict(xor_, "addrrax")
xor_["addrrax"]["cx"] = 0x3b64
xor_["cx"]["addrrax"] = 0x3b68
gendict(xor_, "addrrbx")
xor_["addrrbx"]["cx"] = 0x3b6c
xor_["cx"]["addrrbx"] = 0x3b70
gendict(xor_, "addrrcx")
xor_["addrrcx"]["cx"] = 0x3b74
xor_["cx"]["addrrcx"] = 0x3b78
gendict(xor_, "addrrdx")
xor_["addrrdx"]["cx"] = 0x3b7c
xor_["cx"]["addrrdx"] = 0x3b80
gendict(xor_, "addrrsi")
xor_["addrrsi"]["cx"] = 0x3b84
xor_["cx"]["addrrsi"] = 0x3b88
gendict(xor_, "addrrdi")
xor_["addrrdi"]["cx"] = 0x3b8c
xor_["cx"]["addrrdi"] = 0x3b90
gendict(xor_, "addrrbp")
xor_["addrrbp"]["cx"] = 0x3b94
xor_["cx"]["addrrbp"] = 0x3b99
gendict(xor_, "addrrsp")
xor_["addrrsp"]["cx"] = 0x3b9e
xor_["cx"]["addrrsp"] = 0x3ba3
gendict(xor_, "dx")
xor_["dx"]["ax"] = 0x3ba8
xor_["dx"]["bx"] = 0x3bac
xor_["dx"]["cx"] = 0x3bb0
xor_["dx"]["si"] = 0x3bb4
xor_["dx"]["di"] = 0x3bb8
xor_["dx"]["bp"] = 0x3bbc
xor_["dx"]["sp"] = 0x3bc0
gendict(xor_, "addrrax")
xor_["addrrax"]["dx"] = 0x3bc4
xor_["dx"]["addrrax"] = 0x3bc8
gendict(xor_, "addrrbx")
xor_["addrrbx"]["dx"] = 0x3bcc
xor_["dx"]["addrrbx"] = 0x3bd0
gendict(xor_, "addrrcx")
xor_["addrrcx"]["dx"] = 0x3bd4
xor_["dx"]["addrrcx"] = 0x3bd8
gendict(xor_, "addrrdx")
xor_["addrrdx"]["dx"] = 0x3bdc
xor_["dx"]["addrrdx"] = 0x3be0
gendict(xor_, "addrrsi")
xor_["addrrsi"]["dx"] = 0x3be4
xor_["dx"]["addrrsi"] = 0x3be8
gendict(xor_, "addrrdi")
xor_["addrrdi"]["dx"] = 0x3bec
xor_["dx"]["addrrdi"] = 0x3bf0
gendict(xor_, "addrrbp")
xor_["addrrbp"]["dx"] = 0x3bf4
xor_["dx"]["addrrbp"] = 0x3bf9
gendict(xor_, "addrrsp")
xor_["addrrsp"]["dx"] = 0x3bfe
xor_["dx"]["addrrsp"] = 0x3c03
gendict(xor_, "si")
xor_["si"]["ax"] = 0x3c08
xor_["si"]["bx"] = 0x3c0c
xor_["si"]["cx"] = 0x3c10
xor_["si"]["dx"] = 0x3c14
xor_["si"]["di"] = 0x3c18
xor_["si"]["bp"] = 0x3c1c
xor_["si"]["sp"] = 0x3c20
gendict(xor_, "addrrax")
xor_["addrrax"]["si"] = 0x3c24
xor_["si"]["addrrax"] = 0x3c28
gendict(xor_, "addrrbx")
xor_["addrrbx"]["si"] = 0x3c2c
xor_["si"]["addrrbx"] = 0x3c30
gendict(xor_, "addrrcx")
xor_["addrrcx"]["si"] = 0x3c34
xor_["si"]["addrrcx"] = 0x3c38
gendict(xor_, "addrrdx")
xor_["addrrdx"]["si"] = 0x3c3c
xor_["si"]["addrrdx"] = 0x3c40
gendict(xor_, "addrrsi")
xor_["addrrsi"]["si"] = 0x3c44
xor_["si"]["addrrsi"] = 0x3c48
gendict(xor_, "addrrdi")
xor_["addrrdi"]["si"] = 0x3c4c
xor_["si"]["addrrdi"] = 0x3c50
gendict(xor_, "addrrbp")
xor_["addrrbp"]["si"] = 0x3c54
xor_["si"]["addrrbp"] = 0x3c59
gendict(xor_, "addrrsp")
xor_["addrrsp"]["si"] = 0x3c5e
xor_["si"]["addrrsp"] = 0x3c63
gendict(xor_, "di")
xor_["di"]["ax"] = 0x3c68
xor_["di"]["bx"] = 0x3c6c
xor_["di"]["cx"] = 0x3c70
xor_["di"]["dx"] = 0x3c74
xor_["di"]["si"] = 0x3c78
xor_["di"]["bp"] = 0x3c7c
xor_["di"]["sp"] = 0x3c80
gendict(xor_, "addrrax")
xor_["addrrax"]["di"] = 0x3c84
xor_["di"]["addrrax"] = 0x3c88
gendict(xor_, "addrrbx")
xor_["addrrbx"]["di"] = 0x3c8c
xor_["di"]["addrrbx"] = 0x3c90
gendict(xor_, "addrrcx")
xor_["addrrcx"]["di"] = 0x3c94
xor_["di"]["addrrcx"] = 0x3c98
gendict(xor_, "addrrdx")
xor_["addrrdx"]["di"] = 0x3c9c
xor_["di"]["addrrdx"] = 0x3ca0
gendict(xor_, "addrrsi")
xor_["addrrsi"]["di"] = 0x3ca4
xor_["di"]["addrrsi"] = 0x3ca8
gendict(xor_, "addrrdi")
xor_["addrrdi"]["di"] = 0x3cac
xor_["di"]["addrrdi"] = 0x3cb0
gendict(xor_, "addrrbp")
xor_["addrrbp"]["di"] = 0x3cb4
xor_["di"]["addrrbp"] = 0x3cb9
gendict(xor_, "addrrsp")
xor_["addrrsp"]["di"] = 0x3cbe
xor_["di"]["addrrsp"] = 0x3cc3
gendict(xor_, "bp")
xor_["bp"]["ax"] = 0x3cc8
xor_["bp"]["bx"] = 0x3ccc
xor_["bp"]["cx"] = 0x3cd0
xor_["bp"]["dx"] = 0x3cd4
xor_["bp"]["si"] = 0x3cd8
xor_["bp"]["di"] = 0x3cdc
xor_["bp"]["sp"] = 0x3ce0
gendict(xor_, "addrrax")
xor_["addrrax"]["bp"] = 0x3ce4
xor_["bp"]["addrrax"] = 0x3ce8
gendict(xor_, "addrrbx")
xor_["addrrbx"]["bp"] = 0x3cec
xor_["bp"]["addrrbx"] = 0x3cf0
gendict(xor_, "addrrcx")
xor_["addrrcx"]["bp"] = 0x3cf4
xor_["bp"]["addrrcx"] = 0x3cf8
gendict(xor_, "addrrdx")
xor_["addrrdx"]["bp"] = 0x3cfc
xor_["bp"]["addrrdx"] = 0x3d00
gendict(xor_, "addrrsi")
xor_["addrrsi"]["bp"] = 0x3d04
xor_["bp"]["addrrsi"] = 0x3d08
gendict(xor_, "addrrdi")
xor_["addrrdi"]["bp"] = 0x3d0c
xor_["bp"]["addrrdi"] = 0x3d10
gendict(xor_, "addrrbp")
xor_["addrrbp"]["bp"] = 0x3d14
xor_["bp"]["addrrbp"] = 0x3d19
gendict(xor_, "addrrsp")
xor_["addrrsp"]["bp"] = 0x3d1e
xor_["bp"]["addrrsp"] = 0x3d23
gendict(xor_, "sp")
xor_["sp"]["ax"] = 0x3d28
xor_["sp"]["bx"] = 0x3d2c
xor_["sp"]["cx"] = 0x3d30
xor_["sp"]["dx"] = 0x3d34
xor_["sp"]["si"] = 0x3d38
xor_["sp"]["di"] = 0x3d3c
xor_["sp"]["bp"] = 0x3d40
gendict(xor_, "addrrax")
xor_["addrrax"]["sp"] = 0x3d44
xor_["sp"]["addrrax"] = 0x3d48
gendict(xor_, "addrrbx")
xor_["addrrbx"]["sp"] = 0x3d4c
xor_["sp"]["addrrbx"] = 0x3d50
gendict(xor_, "addrrcx")
xor_["addrrcx"]["sp"] = 0x3d54
xor_["sp"]["addrrcx"] = 0x3d58
gendict(xor_, "addrrdx")
xor_["addrrdx"]["sp"] = 0x3d5c
xor_["sp"]["addrrdx"] = 0x3d60
gendict(xor_, "addrrsi")
xor_["addrrsi"]["sp"] = 0x3d64
xor_["sp"]["addrrsi"] = 0x3d68
gendict(xor_, "addrrdi")
xor_["addrrdi"]["sp"] = 0x3d6c
xor_["sp"]["addrrdi"] = 0x3d70
gendict(xor_, "addrrbp")
xor_["addrrbp"]["sp"] = 0x3d74
xor_["sp"]["addrrbp"] = 0x3d79
gendict(xor_, "addrrsp")
xor_["addrrsp"]["sp"] = 0x3d7e
xor_["sp"]["addrrsp"] = 0x3d83
gendict(xor_, "ah")
xor_["ah"]["bh"] = 0x3d88
xor_["ah"]["ch"] = 0x3d8b
xor_["ah"]["dh"] = 0x3d8e
gendict(xor_, "addrrax")
xor_["addrrax"]["ah"] = 0x3d91
xor_["ah"]["addrrax"] = 0x3d94
gendict(xor_, "addrrbx")
xor_["addrrbx"]["ah"] = 0x3d97
xor_["ah"]["addrrbx"] = 0x3d9a
gendict(xor_, "addrrcx")
xor_["addrrcx"]["ah"] = 0x3d9d
xor_["ah"]["addrrcx"] = 0x3da0
gendict(xor_, "addrrdx")
xor_["addrrdx"]["ah"] = 0x3da3
xor_["ah"]["addrrdx"] = 0x3da6
gendict(xor_, "addrrsi")
xor_["addrrsi"]["ah"] = 0x3da9
xor_["ah"]["addrrsi"] = 0x3dac
gendict(xor_, "addrrdi")
xor_["addrrdi"]["ah"] = 0x3daf
xor_["ah"]["addrrdi"] = 0x3db2
gendict(xor_, "addrrbp")
xor_["addrrbp"]["ah"] = 0x3db5
xor_["ah"]["addrrbp"] = 0x3db9
gendict(xor_, "addrrsp")
xor_["addrrsp"]["ah"] = 0x3dbd
xor_["ah"]["addrrsp"] = 0x3dc1
gendict(xor_, "bh")
xor_["bh"]["ah"] = 0x3dc5
xor_["bh"]["ch"] = 0x3dc8
xor_["bh"]["dh"] = 0x3dcb
gendict(xor_, "addrrax")
xor_["addrrax"]["bh"] = 0x3dce
xor_["bh"]["addrrax"] = 0x3dd1
gendict(xor_, "addrrbx")
xor_["addrrbx"]["bh"] = 0x3dd4
xor_["bh"]["addrrbx"] = 0x3dd7
gendict(xor_, "addrrcx")
xor_["addrrcx"]["bh"] = 0x3dda
xor_["bh"]["addrrcx"] = 0x3ddd
gendict(xor_, "addrrdx")
xor_["addrrdx"]["bh"] = 0x3de0
xor_["bh"]["addrrdx"] = 0x3de3
gendict(xor_, "addrrsi")
xor_["addrrsi"]["bh"] = 0x3de6
xor_["bh"]["addrrsi"] = 0x3de9
gendict(xor_, "addrrdi")
xor_["addrrdi"]["bh"] = 0x3dec
xor_["bh"]["addrrdi"] = 0x3def
gendict(xor_, "addrrbp")
xor_["addrrbp"]["bh"] = 0x3df2
xor_["bh"]["addrrbp"] = 0x3df6
gendict(xor_, "addrrsp")
xor_["addrrsp"]["bh"] = 0x3dfa
xor_["bh"]["addrrsp"] = 0x3dfe
gendict(xor_, "ch")
xor_["ch"]["ah"] = 0x3e02
xor_["ch"]["bh"] = 0x3e05
xor_["ch"]["dh"] = 0x3e08
gendict(xor_, "addrrax")
xor_["addrrax"]["ch"] = 0x3e0b
xor_["ch"]["addrrax"] = 0x3e0e
gendict(xor_, "addrrbx")
xor_["addrrbx"]["ch"] = 0x3e11
xor_["ch"]["addrrbx"] = 0x3e14
gendict(xor_, "addrrcx")
xor_["addrrcx"]["ch"] = 0x3e17
xor_["ch"]["addrrcx"] = 0x3e1a
gendict(xor_, "addrrdx")
xor_["addrrdx"]["ch"] = 0x3e1d
xor_["ch"]["addrrdx"] = 0x3e20
gendict(xor_, "addrrsi")
xor_["addrrsi"]["ch"] = 0x3e23
xor_["ch"]["addrrsi"] = 0x3e26
gendict(xor_, "addrrdi")
xor_["addrrdi"]["ch"] = 0x3e29
xor_["ch"]["addrrdi"] = 0x3e2c
gendict(xor_, "addrrbp")
xor_["addrrbp"]["ch"] = 0x3e2f
xor_["ch"]["addrrbp"] = 0x3e33
gendict(xor_, "addrrsp")
xor_["addrrsp"]["ch"] = 0x3e37
xor_["ch"]["addrrsp"] = 0x3e3b
gendict(xor_, "dh")
xor_["dh"]["ah"] = 0x3e3f
xor_["dh"]["bh"] = 0x3e42
xor_["dh"]["ch"] = 0x3e45
gendict(xor_, "addrrax")
xor_["addrrax"]["dh"] = 0x3e48
xor_["dh"]["addrrax"] = 0x3e4b
gendict(xor_, "addrrbx")
xor_["addrrbx"]["dh"] = 0x3e4e
xor_["dh"]["addrrbx"] = 0x3e51
gendict(xor_, "addrrcx")
xor_["addrrcx"]["dh"] = 0x3e54
xor_["dh"]["addrrcx"] = 0x3e57
gendict(xor_, "addrrdx")
xor_["addrrdx"]["dh"] = 0x3e5a
xor_["dh"]["addrrdx"] = 0x3e5d
gendict(xor_, "addrrsi")
xor_["addrrsi"]["dh"] = 0x3e60
xor_["dh"]["addrrsi"] = 0x3e63
gendict(xor_, "addrrdi")
xor_["addrrdi"]["dh"] = 0x3e66
xor_["dh"]["addrrdi"] = 0x3e69
gendict(xor_, "addrrbp")
xor_["addrrbp"]["dh"] = 0x3e6c
xor_["dh"]["addrrbp"] = 0x3e70
gendict(xor_, "addrrsp")
xor_["addrrsp"]["dh"] = 0x3e74
xor_["dh"]["addrrsp"] = 0x3e78
gendict(xor_, "al")
xor_["al"]["bl"] = 0x3e7c
xor_["al"]["cl"] = 0x3e7f
xor_["al"]["dl"] = 0x3e82
gendict(xor_, "addrrax")
xor_["addrrax"]["al"] = 0x3e85
xor_["al"]["addrrax"] = 0x3e88
gendict(xor_, "addrrbx")
xor_["addrrbx"]["al"] = 0x3e8b
xor_["al"]["addrrbx"] = 0x3e8e
gendict(xor_, "addrrcx")
xor_["addrrcx"]["al"] = 0x3e91
xor_["al"]["addrrcx"] = 0x3e94
gendict(xor_, "addrrdx")
xor_["addrrdx"]["al"] = 0x3e97
xor_["al"]["addrrdx"] = 0x3e9a
gendict(xor_, "addrrsi")
xor_["addrrsi"]["al"] = 0x3e9d
xor_["al"]["addrrsi"] = 0x3ea0
gendict(xor_, "addrrdi")
xor_["addrrdi"]["al"] = 0x3ea3
xor_["al"]["addrrdi"] = 0x3ea6
gendict(xor_, "addrrbp")
xor_["addrrbp"]["al"] = 0x3ea9
xor_["al"]["addrrbp"] = 0x3ead
gendict(xor_, "addrrsp")
xor_["addrrsp"]["al"] = 0x3eb1
xor_["al"]["addrrsp"] = 0x3eb5
gendict(xor_, "bl")
xor_["bl"]["al"] = 0x3eb9
xor_["bl"]["cl"] = 0x3ebc
xor_["bl"]["dl"] = 0x3ebf
gendict(xor_, "addrrax")
xor_["addrrax"]["bl"] = 0x3ec2
xor_["bl"]["addrrax"] = 0x3ec5
gendict(xor_, "addrrbx")
xor_["addrrbx"]["bl"] = 0x3ec8
xor_["bl"]["addrrbx"] = 0x3ecb
gendict(xor_, "addrrcx")
xor_["addrrcx"]["bl"] = 0x3ece
xor_["bl"]["addrrcx"] = 0x3ed1
gendict(xor_, "addrrdx")
xor_["addrrdx"]["bl"] = 0x3ed4
xor_["bl"]["addrrdx"] = 0x3ed7
gendict(xor_, "addrrsi")
xor_["addrrsi"]["bl"] = 0x3eda
xor_["bl"]["addrrsi"] = 0x3edd
gendict(xor_, "addrrdi")
xor_["addrrdi"]["bl"] = 0x3ee0
xor_["bl"]["addrrdi"] = 0x3ee3
gendict(xor_, "addrrbp")
xor_["addrrbp"]["bl"] = 0x3ee6
xor_["bl"]["addrrbp"] = 0x3eea
gendict(xor_, "addrrsp")
xor_["addrrsp"]["bl"] = 0x3eee
xor_["bl"]["addrrsp"] = 0x3ef2
gendict(xor_, "cl")
xor_["cl"]["al"] = 0x3ef6
xor_["cl"]["bl"] = 0x3ef9
xor_["cl"]["dl"] = 0x3efc
gendict(xor_, "addrrax")
xor_["addrrax"]["cl"] = 0x3eff
xor_["cl"]["addrrax"] = 0x3f02
gendict(xor_, "addrrbx")
xor_["addrrbx"]["cl"] = 0x3f05
xor_["cl"]["addrrbx"] = 0x3f08
gendict(xor_, "addrrcx")
xor_["addrrcx"]["cl"] = 0x3f0b
xor_["cl"]["addrrcx"] = 0x3f0e
gendict(xor_, "addrrdx")
xor_["addrrdx"]["cl"] = 0x3f11
xor_["cl"]["addrrdx"] = 0x3f14
gendict(xor_, "addrrsi")
xor_["addrrsi"]["cl"] = 0x3f17
xor_["cl"]["addrrsi"] = 0x3f1a
gendict(xor_, "addrrdi")
xor_["addrrdi"]["cl"] = 0x3f1d
xor_["cl"]["addrrdi"] = 0x3f20
gendict(xor_, "addrrbp")
xor_["addrrbp"]["cl"] = 0x3f23
xor_["cl"]["addrrbp"] = 0x3f27
gendict(xor_, "addrrsp")
xor_["addrrsp"]["cl"] = 0x3f2b
xor_["cl"]["addrrsp"] = 0x3f2f
gendict(xor_, "dl")
xor_["dl"]["al"] = 0x3f33
xor_["dl"]["bl"] = 0x3f36
xor_["dl"]["cl"] = 0x3f39
gendict(xor_, "addrrax")
xor_["addrrax"]["dl"] = 0x3f3c
xor_["dl"]["addrrax"] = 0x3f3f
gendict(xor_, "addrrbx")
xor_["addrrbx"]["dl"] = 0x3f42
xor_["dl"]["addrrbx"] = 0x3f45
gendict(xor_, "addrrcx")
xor_["addrrcx"]["dl"] = 0x3f48
xor_["dl"]["addrrcx"] = 0x3f4b
gendict(xor_, "addrrdx")
xor_["addrrdx"]["dl"] = 0x3f4e
xor_["dl"]["addrrdx"] = 0x3f51
gendict(xor_, "addrrsi")
xor_["addrrsi"]["dl"] = 0x3f54
xor_["dl"]["addrrsi"] = 0x3f57
gendict(xor_, "addrrdi")
xor_["addrrdi"]["dl"] = 0x3f5a
xor_["dl"]["addrrdi"] = 0x3f5d
gendict(xor_, "addrrbp")
xor_["addrrbp"]["dl"] = 0x3f60
xor_["dl"]["addrrbp"] = 0x3f64
gendict(xor_, "addrrsp")
xor_["addrrsp"]["dl"] = 0x3f68
xor_["dl"]["addrrsp"] = 0x3f6c
