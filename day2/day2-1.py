with open('../input/day2.txt') as f:
    lines = f.readlines()
    times2 = 0
    times3 = 0
    for line in lines:
        occurences = {}
        for c in line:
            if c in occurences:
                occurences[c] += 1
            else:
                occurences[c] = 1
        for c, n in occurences.items():
            if n == 2:
                times2 += 1
                break
        for c, n in occurences.items():
            if n == 3:
                times3 += 1
                break
    print(times2 * times3)
    