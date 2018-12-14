import re

def read_input():
    with open('../input/day12.txt') as f:
        lines = f.readlines()
    m = re.search(r'initial state:\s([\.#]+)', lines[0])
    initial_state = m.groups()[0]
    prog = re.compile(r'([\.#]{5})\s=>\s([\.#])')
    rules = []
    for i in range(2, len(lines)):
        m = prog.search(lines[i])
        groups = m.groups()
        if groups[1] == '#':
            rules.append((groups[0], groups[1]))
    return initial_state, rules

def apply_gen(initial_state, rules, start):
    next_state = []
    initial_state = '....' + initial_state.strip('.') + '....'
    set_start_idx = False
    i = 2
    while i <= len(initial_state)-3:
        curr_str = initial_state[i-2:i+3]
        rule_matches = None
        for r in rules:
            if curr_str == r[0]:
                rule_matches = r
                break
        if rule_matches:
            if not set_start_idx:
                start_idx = i - 4
                set_start_idx = True
            next_state.append(rule_matches[1])
        else:
            next_state.append('.')
        i += 1
    return start + start_idx, ''.join(next_state).strip('.')

def sum_plants(state, start):
    i = start
    plant_count = 0
    for c in state:
        if c == '#':
            plant_count += i
        i += 1
    return plant_count

state, rules = read_input()
start = 0
for c in state:
    if c == '#':
        break
    start += 1
gen = 0
start_idx = -2
previos = sum_plants(state, start)
prev_diff = 0
same_diff_count = 0
while gen < 1000:
    start, state = apply_gen(state, rules, start)
    total = sum_plants(state, start)
    diff = total-previos
    gen += 1
    if diff == prev_diff:
        same_diff_count += 1
        if same_diff_count == 100:
            break
    previos = total
    prev_diff = diff
b = total - diff*gen
solution = diff * 50000000000 + b
print(solution)