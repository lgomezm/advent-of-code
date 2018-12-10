player_count = 452
scores = []
for _ in range(player_count):
    scores.append(0)
circle = [0]
current_idx = 0
current_marble = 1
current_player = 0
last_marble_worth = 70784
while current_marble <= last_marble_worth:
    if current_marble % 23 == 0:
        if current_idx - 7 >= 0:
            current_idx = current_idx - 7
        else:
            current_idx = len(circle) - 7 + current_idx
        scores[current_player] += current_marble + circle.pop(current_idx)
    else:
        if current_idx + 2 == len(circle):
            circle.append(current_marble)
            current_idx += 2 
        elif current_idx + 2 > len(circle):
            circle.insert(1, current_marble)
            current_idx = 1
        else:
            circle.insert(current_idx + 2, current_marble)
            current_idx += 2 
    current_marble += 1
    current_player = (current_player + 1) % player_count
highest_score = 0
for s in scores:
    if s > highest_score:
        highest_score = s
print(highest_score)