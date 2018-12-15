recipes = 846021
scores = [3, 7]
idx1 = 0
idx2 = 1
while len(scores) < recipes+10:
    combined = scores[idx1] + scores[idx2]
    if combined >= 10:
        scores.append(1)
    scores.append(combined % 10)
    idx1 = (idx1 + scores[idx1] + 1) % len(scores)
    idx2 = (idx2 + scores[idx2] + 1) % len(scores)
print(''.join(str(x) for x in scores[recipes:recipes+10]))