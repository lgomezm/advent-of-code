recipes = '846021'
scores = '37'
idx1, idx2 = 0, 1
index = -1
while recipes not in scores[-7:]:
    val1 = int(scores[idx1])
    val2 = int(scores[idx2])
    scores += str(val1 + val2)
    idx1 = (idx1 + val1 + 1) % len(scores)
    idx2 = (idx2 + val2 + 1) % len(scores)
print(scores.index(recipes))