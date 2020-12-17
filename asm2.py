input1 = 0x4
input2 = 0x2d

while input1 <= 0x5fa1:
    input2 += 0x1
    input1 += 0xd1

print(hex(input2))