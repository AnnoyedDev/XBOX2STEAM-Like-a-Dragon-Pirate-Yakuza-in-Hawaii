#!/usr/bin/env python3
"""Convert a savegame from LAD Pirate Yakuza Game Pass into Steam.
Xbox : XOR(msgpack) + XUID(8 o) + CRC32(msgpack) ; Steam : XOR(msgpack) + CRC32(msgpack).
Usage : xbox2steam.py <xbox_entry> <steam_output>"""
import struct, sys, zlib

KEY = b'STarYZgr3DL11'

def xor(d):
    return bytes(b ^ KEY[i % len(KEY)] for i, b in enumerate(d))

def convert(d):
    crc = struct.unpack('<I', d[-4:])[0]
    if zlib.crc32(xor(d[:-12])) != crc:
        raise ValueError('CRC Xbox invalid : Not a Game Pass file of this game.')
    out = d[:-12] + d[-4:]
    assert zlib.crc32(xor(out[:-4])) == crc
    return out

if __name__ == '__main__':
    src, dst = sys.argv[1:3]
    data = convert(open(src, 'rb').read())
    open(dst, 'wb').write(data)
    print(f'OK {src} -> {dst} ({len(data)} o)')
