import math

def read_coordinates():
    with open('../input/day6.txt') as f:
        lines = f.readlines()
    coordinates = []
    for line in lines:
        coord = line.strip().split(', ')
        coordinates.append((int(coord[0]), int(coord[1])))
    return coordinates

def find_max_coordinates(coordinates):
    max_x = coordinates[0][0]
    max_y = coordinates[0][1]
    for coord in coordinates:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
    return (max_x, max_y)

def build_matrix(max_coordinates):
    m = []
    for i in range(max_coordinates[1] + 1):
        m.append([])
        for _ in range(max_coordinates[0] + 1):
            m[i].append('.')
    return m

def manhattan_distance(coord1, coord2):
    return abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])

coordinates = read_coordinates()
max_coordinates = find_max_coordinates(coordinates)
matrix = build_matrix(max_coordinates)
max_x = max_coordinates[0]
max_y = max_coordinates[1]
for y in range(max_y+1):
    for x in range(max_x+1):
        min_d = math.inf
        for coord in coordinates:
            d = manhattan_distance((x, y), coord)
            if d < min_d:
                min_d = d
                matrix[y][x] = coord
            elif d == min_d:
                matrix[y][x] = '.'
infinite = set()
freq = {}
for y in range(max_y+1):
    for x in range(max_x+1):
        if matrix[y][x] == '.':
            continue
        if (x == 0 or y == 0 or x == max_x or y == max_y) and not matrix[y][x] in infinite:
            infinite.add(matrix[y][x])
        if not matrix[y][x] in freq:
            freq[matrix[y][x]] = 1
        else:
            freq[matrix[y][x]] += 1
max_freq = 0
for coord, f in freq.items():
    if not coord in infinite and max_freq < f:
        max_freq = f
print(max_freq)