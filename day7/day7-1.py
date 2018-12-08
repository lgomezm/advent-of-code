import re

def read_instructions():
    with open('../input/day7.txt') as f:
        lines = f.readlines()
    prog = re.compile(r'Step\s(\w+)\smust be finished before step (\w+) can begin.')
    steps_to_deps = {}
    all_steps = set()
    for line in lines:
        match = prog.search(line)
        groups = match.groups()
        all_steps.add(groups[0])
        all_steps.add(groups[1])
        if not groups[0] in steps_to_deps:
            steps_to_deps[groups[0]] = set()
        steps_to_deps[groups[0]].add(groups[1])
    no_next_steps = all_steps - steps_to_deps.keys()
    for s in no_next_steps:
        steps_to_deps[s] = set()
    return steps_to_deps

def get_available_steps(steps_to_deps):
    all_deps = set()
    for deps in steps_to_deps.values():
        all_deps |= deps
    diff = steps_to_deps.keys() - all_deps
    available = []
    for s in diff:
        available.append(s)
    return available

order = []
steps_to_deps = read_instructions()
while len(steps_to_deps) > 0:
    available = get_available_steps(steps_to_deps)
    available.sort()
    step = available.pop(0)
    order.append(step)
    del steps_to_deps[step]
print(''.join(order))