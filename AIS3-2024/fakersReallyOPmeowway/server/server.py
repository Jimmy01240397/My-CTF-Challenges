import gadget
import random
import sys

socketmode = len(sys.argv) > 1 and sys.argv[1] == 'socket'

def leftRotate(n, d, int_bits):
    return ((n << d)|(n >> (int_bits - d))) & (2**int_bits-1)

def rightRotate(n, d, int_bits):
    return ((n >> d)|(n << (int_bits - d))) & (2**int_bits-1)

def close():
    if socketmode:
        conn.close()
        server.close()

with open("flag.txt", 'r') as f:
    ansflag = f.read().strip().encode()

gadgetindex = 0x12ad
mainindex = 0x52b4
leaveindex = 0x5224

if socketmode:
    import socket
    import ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 8741))
    server.listen(0)
    conn, addr = server.accept()
    conn = context.wrap_socket(conn, server_side=True)
    send = conn.send
    recv = conn.recv
else:
    send = sys.stdout.buffer.write
    recv = sys.stdin.buffer.read

data = recv(8)
gadget.mainoffset = int.from_bytes(data, "little")
offset = gadget.mainoffset - mainindex
gadget.gadgetoffset = gadgetindex + offset + 4
gadget.leaveoffset = leaveindex + offset + 4

data = recv(8)
flagcheck = int.from_bytes(data, "little")
flag = flagcheck + 0x30

checkdata = recv(48)

pool = list(range(36))
random.shuffle(pool)
modelist = ["" for a in range(36)]
usemode = ["add", "sub", "xor", "null"]
for a in range(len(pool)):
    modelist[pool[a]] = usemode[int(a % len(usemode))]

flagtocheckindex = list(range(36))
checkindextoflag = list(range(48))

for a in range(48):
    if a < len(flagtocheckindex):
        checkindextoflag[a] = a
    else:
        checkindextoflag[a] = -1

random.shuffle(checkindextoflag)

for a in range(48):
    if checkindextoflag[a] >= 0:
        flagtocheckindex[checkindextoflag[a]] = a

order = list(range(48))
random.shuffle(order)

regpool = [('addrrax', 'rax', 'eax', 'ax', 'ah', 'al'),
           ('addrrbx', 'rbx', 'ebx', 'bx', 'bh', 'bl'),
           ('addrrdx', 'rdx', 'edx', 'dx', 'dh', 'dl')]

addrregpool = [('addrrsi', 'rsi', 'esi', 'si'),
               ('addrrdi', 'rdi', 'edi', 'di')]

senddata = b""
checkindex = 0
for a in order:
    rotfunc = random.choice([gadget._ror, gadget._rol])
    rrotfunc = leftRotate if rotfunc == gadget._ror else rightRotate
    rottime = random.randint(1, 7)
    nowcheck = rrotfunc(int(checkdata[a]), rottime, 8)
    if checkindextoflag[a] < 0:
        resultreg = random.choice(regpool)
        addrreg = random.choice(addrregpool)
        senddata += gadget._pop(resultreg[1], nowcheck)
        senddata += rotfunc(resultreg[5], rottime)
        senddata += gadget._pop(addrreg[1], flagcheck + a)
        senddata += gadget._mov(addrreg[0], resultreg[5])
        continue

    if modelist[checkindextoflag[a]] not in ["add", "sub", "xor", "null"]:
        modelist[checkindextoflag[a]] = random.choice(["add", "sub", "xor", "null"])

    if modelist[checkindextoflag[a]] == "null":
        resultreg = random.choice(regpool)
        addrreg = random.choice(addrregpool)
        senddata += gadget._pop(resultreg[1], nowcheck)
        senddata += rotfunc(resultreg[5], rottime)
        senddata += gadget._pop(addrreg[1], flagcheck + a)
        senddata += gadget._mov(addrreg[0], resultreg[5])
    elif modelist[checkindextoflag[a]] == "add":
        resultreg = random.choice(regpool)
        addrreg = random.choice(addrregpool)
        calcreg = random.choice(regpool)
        while calcreg[0] == resultreg[0]:
            calcreg = random.choice(regpool)
        senddata += gadget._pop(addrreg[1], flag + checkindextoflag[a])
        senddata += gadget._mov(resultreg[5], addrreg[0])
        senddata += gadget._pop(calcreg[1], (nowcheck - int(ansflag[checkindextoflag[a]]) + 0x100) & 0xff)
        senddata += gadget._add(resultreg[5], calcreg[5])
        senddata += rotfunc(resultreg[5], rottime)
        senddata += gadget._pop(addrreg[1], flagcheck + a)
        senddata += gadget._mov(addrreg[0], resultreg[5])
    elif modelist[checkindextoflag[a]] == "sub":
        resultreg = random.choice(regpool)
        addrreg = random.choice(addrregpool)
        calcreg = random.choice(regpool)
        while calcreg[0] == resultreg[0]:
            calcreg = random.choice(regpool)
        senddata += gadget._pop(addrreg[1], flag + checkindextoflag[a])
        senddata += gadget._mov(resultreg[5], addrreg[0])
        senddata += gadget._pop(calcreg[1], (int(ansflag[checkindextoflag[a]]) - nowcheck + 0x100) & 0xff)
        senddata += gadget._sub(resultreg[5], calcreg[5])
        senddata += rotfunc(resultreg[5], rottime)
        senddata += gadget._pop(addrreg[1], flagcheck + a)
        senddata += gadget._mov(addrreg[0], resultreg[5])
    elif modelist[checkindextoflag[a]] == "xor":
        resultreg = random.choice(regpool)
        addrreg = random.choice(addrregpool)
        calcreg = random.choice(regpool)
        while calcreg[0] == resultreg[0]:
            calcreg = random.choice(regpool)
        senddata += gadget._pop(addrreg[1], flag + checkindextoflag[a])
        senddata += gadget._mov(resultreg[5], addrreg[0])
        senddata += gadget._pop(calcreg[1], (int(ansflag[checkindextoflag[a]]) ^ nowcheck) & 0xff)
        senddata += gadget._xor(resultreg[5], calcreg[5])
        senddata += rotfunc(resultreg[5], rottime)
        senddata += gadget._pop(addrreg[1], flagcheck + a)
        senddata += gadget._mov(addrreg[0], resultreg[5])

senddata += gadget.leave()

send(senddata)
close()

