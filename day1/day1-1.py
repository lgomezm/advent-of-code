with open('input/day1.txt') as f:
    lines = f.readlines()
    frequency = 0
    for line in lines:
        if line[0] == '+':
            frequency = frequency+int(line[1:])
        elif line[0] == '-':
            frequency = frequency-int(line[1:])
    print(frequency)
