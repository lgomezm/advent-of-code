class Node:
    def __init__(self, child_count, metadata_count, children, metadata):
        self.child_count = child_count
        self.metadata_count = metadata_count
        self.children = children
        self.metadata = metadata

def build_node(numbers, index):
    child_count = numbers[index]
    metadata_count = numbers[index+1]
    if child_count > 0:
        children, index = read_children(numbers, index+2, child_count)
    else:
        children = []
        index = index+2
    metadata = []
    i = index
    while i < index+metadata_count:
        metadata.append(numbers[i]) 
        i += 1
    node = Node(child_count, metadata_count, children, metadata)
    return node, i

def read_children(numbers, index, child_count):
    children = []
    for i in range(child_count):
        node, index = build_node(numbers, index)
        children.append(node)
    return children, index

def sum_metadata(node, acum):
    total_node = 0
    for m in node.metadata:
        total_node += m
    for c in node.children:
        total_node += sum_metadata(c, 0)
    return acum+total_node

with open('../input/day8.txt') as f:
    line = f.readline()
parts = line.strip().split(' ')
numbers = []
for s in parts:
    numbers.append(int(s))
root, _ = build_node(numbers, 0)
print(sum_metadata(root,0))