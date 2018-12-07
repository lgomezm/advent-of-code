with open('../input/day5.txt') as f:
    l = []
    length = 0
    byte = f.read(1)
    while byte:
        if length == 0 or abs(ord(byte)-ord(l[length-1])) != 32:
            l.append(byte)
            length += 1
        else:
            l.pop()
            length -= 1
        byte = f.read(1)
    print(length)