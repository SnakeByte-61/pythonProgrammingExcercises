# with open("binary","bw") as binFile:
# #    for i in range(17):
#     binFile.write(bytes(range(17)))
#
# #reading binary file
#
# with open("binary","br") as binFileRead :
#     for b in binFileRead:
#         print(b)

a = 65534 #FF FE
b = 65535 #FF FF
c = 65536 # 00 01 00 00
x = 2998302 # 02 2D C0 1E

with open("binary2","bw") as binFile:
    binFile.write(a.to_bytes(2,'big'))
    binFile.write(b.to_bytes(2,'big'))
    binFile.write(c.to_bytes(4,'big'))
    binFile.write(x.to_bytes(4,'big'))
    binFile.write(x.to_bytes(4,'little'))

with open("binary2","br") as binFileRead:
    e = int.from_bytes(binFileRead.read(2),'big')
    print(e)
    f = int.from_bytes(binFileRead.read(2),'big')
    print(f)
    g = int.from_bytes(binFileRead.read(4),'big')
    print(g)
    h = int.from_bytes(binFileRead.read(4),'big')
    print(h)
    i = int.from_bytes(binFileRead.read(4),'little')
    print(i)
