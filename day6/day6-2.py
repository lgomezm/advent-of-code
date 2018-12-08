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

def manhattan_distance(coord1, coord2):
    return abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])

coordinates = read_coordinates()
max_coordinates = find_max_coordinates(coordinates)
max_x = max_coordinates[0]
max_y = max_coordinates[1]
count = 0
distance = 10000
for y in range(max_y+1):
    for x in range(max_x+1):
        total = 0
        i = 0
        while i < len(coordinates) and total < distance:
            coord = coordinates[i]
            total += manhattan_distance((x, y), coord)
            i += 1
        if total < distance:
            count += 1
print(count)