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

def get_sorted_available_steps(steps_to_deps, workers):
    wip = set()
    for w in workers:
        if w[0] != '.':
            wip.add(w[0])
    all_deps = set()
    for deps in steps_to_deps.values():
        all_deps |= deps
    diff = steps_to_deps.keys() - all_deps - wip
    available = []
    for s in diff:
        available.append(s)
    available.sort()
    return available

steps_to_deps = read_instructions()
worker_count = 5
workers = []
for i in range(worker_count):
    workers.append(['.', 0])
counter = -1
while len(steps_to_deps) > 0:
    i = 0
    checked = set()
    while i < worker_count:
        if not i in checked:
            available = get_sorted_available_steps(steps_to_deps, workers)
            if workers[i][1] == 0:
                if len(available) > 0:
                    step = available.pop(0)
                    workers[i] = [step, ord(step)-4]
                    checked.add(i)
                i += 1
            else:
                workers[i][1] -= 1
                if workers[i][1] == 0:
                    del steps_to_deps[workers[i][0]]
                    workers[i][0] = '.'
                    i = 0
                else:
                    checked.add(i)
                    i += 1
        else:
            i += 1
    counter += 1
print(counter)