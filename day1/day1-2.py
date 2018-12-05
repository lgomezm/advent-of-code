with open('../input/day1.txt') as f:
    lines = f.readlines()
    s = set()
    s.add(0)
    frequency = 0
    i = 0
    foundDuplicate = False
    while not foundDuplicate and i < len(lines):
        line = lines[i]
        if line[0] == '+':
            frequency = frequency+int(line[1:])
        elif line[0] == '-':
            frequency = frequency-int(line[1:])
        if frequency in s:
            break
        s.add(frequency)
        i = i + 1
        if i == len(lines):
            i = 0
    print(frequency)