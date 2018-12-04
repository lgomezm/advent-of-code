def editDistance(s1, s2):
    temp = []
    for i in range(len(s1) + 1):
        temp.append([i])
        for j in range(len(s2)):
            if i == 0:
                temp[i].append(j + 1)
            else:
                temp[i].append(0)
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                temp[i][j] = temp[i - 1][j - 1]
            else:
                temp[i][j] = 1 + min(temp[i-1][j-1], temp[i-1][j], temp[i][j-1])
    return temp[len(s1)][len(s2)]

with open('../input/day2.txt') as f:
    lines = f.readlines()
    i = 0
    found = False
    while i < len(lines) and not found:
        s1 = lines[i].strip()
        for j in range(i + 1, len(lines)):
            s2 = lines[j].strip()
            d = editDistance(s1, s2)
            if d == 1:
                print(s1)
                print(s2)
                found = True
                break
        i += 1
