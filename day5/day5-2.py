def process(excluded):
    with open('../input/day5.txt') as f:
        l = []
        length = 0
        byte = f.read(1)
        while byte:
            if byte != chr(excluded) and byte != chr(excluded + 32):
                if length == 0 or abs(ord(byte)-ord(l[length-1])) != 32:
                    l.append(byte)
                    length += 1
                else:
                    l.pop()
                    length -= 1
            byte = f.read(1)
        return length

def calculateMinPolymer():
    min_length = process(ord('A'))
    for i in range(ord('B'), ord('Z')+1):
        length = process(i)
        if length < min_length:
            min_length = length
    return min_length

print(calculateMinPolymer())