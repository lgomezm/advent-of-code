import re

class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    def update(self):
        self.x += self.dx
        self.y += self.dy
    def __str__(self):
        return str(self.x)+','+str(self.y)+';'+str(self.dx)+','+str(self.dy)

def read_points():
    with open('../input/day10.txt') as f:
        lines = f.readlines()
    prog = re.compile(r'position=<(\s*\-?\d+),(\s*\-?\d+)> velocity=<(\s*\-?\d+),(\s*\-?\d+)>')
    points = []
    for line in lines:
        match = prog.search(line)
        groups = match.groups()
        points.append(Point(int(groups[0]), int(groups[1]), int(groups[2]), int(groups[3])))
    return points

def print_points(points):
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    for p in points:
        if p.x < min_x:
            min_x = p.x
        if p.x > max_x:
            max_x = p.x
        if p.y < min_y:
            min_y = p.y
        if p.y > max_y:
            max_y = p.y
    if max_y - min_y > 10:
        return [['.']]
    center_x = -1 * min_x
    center_y = -1 * min_y
    matrix = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]
    for p in points:
        i = center_x + p.x
        j = center_y + p.y
        matrix[j][i] = '#'
    return matrix

points = read_points()
second_count = 500000
f = open('results.txt','w')
for i in range(second_count):
    matrix = print_points(points)
    if len(matrix) > 1:
        f.write('After '+str(i)+' seconds\n')
        for r in matrix:
            f.write(''.join(r)+'\n')
    for p in points:
        p.update()
f.close()