import gadget
import random
import sys
import os

enable_rotate = os.environ.get("ENABLE_ROTATE", "true") != "false"
enable_reg_randomize = os.environ.get("ENABLE_REG_RANDOMIZE", "true") != "false"
enable_calc_randomize = os.environ.get("ENABLE_CALC_RANDOMIZE", "true") != "false"
enable_flagtocheck_randomize = os.environ.get("ENABLE_FLAGTOCHECK_RANDOMIZE", "true") != "false"
enable_order_randomize = os.environ.get("ENABLE_ORDER_RANDOMIZE", "true") != "false"



socketmode = len(sys.argv) > 1 and sys.argv[1] == 'socket'

regpool = [('addrrax', 'rax', 'eax', 'ax', 'ah', 'al'),
           ('addrrbx', 'rbx', 'ebx', 'bx', 'bh', 'bl'),
           ('addrrdx', 'rdx', 'edx', 'dx', 'dh', 'dl')]

addrregpool = [('addrrsi', 'rsi', 'esi', 'si'),
               ('addrrdi', 'rdi', 'edi', 'di')]

with open("flag.txt", 'r') as f:
    ansflag = f.read().strip().encode()

gadgetindex = 0x12dd
mainindex = 0x56d7
leaveindex = 0x5254

def leftRotate(n, d, int_bits):
    return ((n << d)|(n >> (int_bits - d))) & (2**int_bits-1)

def rightRotate(n, d, int_bits):
    return ((n >> d)|(n << (int_bits - d))) & (2**int_bits-1)

def close():
    if socketmode:
        conn.close()
        server.close()

def gencalcchain(rotfunc, calcfunc, number):
    senddata = b''
    resultreg = random.choice(regpool) if enable_reg_randomize else regpool[0]
    addrreg = random.choice(addrregpool) if enable_reg_randomize else addrregpool[0]
    if calcfunc != None:
        calcreg = random.choice(regpool) if enable_reg_randomize else regpool[1]
        while calcreg[0] == resultreg[0]:
            calcreg = random.choice(regpool) if enable_reg_randomize else regpool[1]
        senddata += gadget._pop(addrreg[1], flag + checkindextoflag[a])
        senddata += gadget._mov(resultreg[5], addrreg[0])
        senddata += gadget._pop(calcreg[1], number)
        senddata += calcfunc(resultreg[5], calcreg[5])
    else:
        senddata += gadget._pop(resultreg[1], number)

    if rotfunc != None:
        senddata += rotfunc(resultreg[5], rottime)
    senddata += gadget._pop(addrreg[1], flagcheck + a)
    senddata += gadget._mov(addrreg[0], resultreg[5])
    return senddata

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
if enable_calc_randomize:
    random.shuffle(pool)
modelist = ["" for a in range(36)]
usemode = ["add", "sub", "xor", "null"] if enable_calc_randomize else ["add", "sub", "xor"]
for a in range(len(pool)):
    modelist[pool[a]] = usemode[int(a % len(usemode))]

flagtocheckindex = list(range(36))
checkindextoflag = list(range(48))

for a in range(48):
    if a < len(flagtocheckindex):
        checkindextoflag[a] = a
    else:
        checkindextoflag[a] = -1

if enable_flagtocheck_randomize:
    random.shuffle(checkindextoflag)

for a in range(48):
    if checkindextoflag[a] >= 0:
        flagtocheckindex[checkindextoflag[a]] = a

order = list(range(48))
if enable_order_randomize:
    random.shuffle(order)

senddata = b""
checkindex = 0
for a in order:
    rotfunc = None
    nowcheck = int(checkdata[a])
    if enable_rotate:
        rotfunc = random.choice([gadget._ror, gadget._rol])
        rrotfunc = leftRotate if rotfunc == gadget._ror else rightRotate
        rottime = random.randint(1, 7)
        nowcheck = rrotfunc(nowcheck, rottime, 8)

    if checkindextoflag[a] < 0:
        senddata += gencalcchain(rotfunc, None, nowcheck)
        continue

    if modelist[checkindextoflag[a]] not in ["add", "sub", "xor", "null"]:
        modelist[checkindextoflag[a]] = random.choice(["add", "sub", "xor", "null"])

    if modelist[checkindextoflag[a]] == "null":
        senddata += gencalcchain(rotfunc, None, nowcheck)
    elif modelist[checkindextoflag[a]] == "add":
        senddata += gencalcchain(rotfunc, gadget._add, (nowcheck - int(ansflag[checkindextoflag[a]]) + 0x100) & 0xff)
    elif modelist[checkindextoflag[a]] == "sub":
        senddata += gencalcchain(rotfunc, gadget._sub, (int(ansflag[checkindextoflag[a]]) - nowcheck + 0x100) & 0xff)
    elif modelist[checkindextoflag[a]] == "xor":
        senddata += gencalcchain(rotfunc, gadget._xor, (int(ansflag[checkindextoflag[a]]) ^ nowcheck) & 0xff)

senddata += gadget.leave()

send(senddata)
close()

