class Node:
    def __init__(self, marble, previous=None, next=None):
        self.marble = marble
        self.previous = previous
        self.next = next

player_count = 452
scores = []
for _ in range(player_count):
    scores.append(0)
current_marble = Node(0)
current_marble.previous = current_marble
current_marble.next = current_marble
current_value = 1
current_player = 0
last_marble_worth = 7078400
while current_value <= last_marble_worth:
    if current_value % 23 == 0:
        for _ in range(7):
            current_marble = current_marble.previous
        previous = current_marble.previous
        next = current_marble.next
        previous.next = next
        next.previous = previous
        scores[current_player] += current_value + current_marble.marble
        current_marble = next
    else:
        new_marble = Node(current_value, current_marble.next, current_marble.next.next)
        current_marble.next.next.previous = new_marble
        current_marble.next.next = new_marble
        current_marble = new_marble
    current_value += 1
    current_player = (current_player + 1) % player_count
highest_score = 0
for s in scores:
    if s > highest_score:
        highest_score = s
print(highest_score)