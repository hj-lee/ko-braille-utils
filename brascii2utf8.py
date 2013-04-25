# -*- coding: utf-8 -*-

import sys

BR_ASCII = " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="
BR_UNICODE = ' ' + ''.join([chr(c) for c in range(0x2801, 0x2800+64)])

#           0         1          2         3         4         5         6
#           0123456789012345 678901234567890123456789012345678901234567890123
BR_LOUIS = " a1b'k2l`cif/msp\"e3h9o6r~djg>ntq,*5<-u8v.%{$+x!&;:4|0z7(_?w}#y)="

A2U_MAP = str.maketrans(BR_ASCII, BR_UNICODE)
U2A_MAP = str.maketrans(BR_UNICODE, BR_ASCII)
L2U_MAP = str.maketrans(BR_LOUIS, BR_UNICODE)

while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = line.translate(L2U_MAP)
    line = line.translate(A2U_MAP)
    sys.stdout.write(line)
