def calculate_power_level(x, y, serial_number):
    rack_id = x + 10
    rack_id_power_level = (rack_id * y) + serial_number
    rack_id_power_level *= rack_id
    rack_id_power_level = int(rack_id_power_level / 100) % 10
    return rack_id_power_level - 5

def calculate_total_power(matrix, i, j, max_size):
    prev_total = matrix[j][i]
    size = 1
    max_power = 0
    max_coord = [j+1,i+1,size]
    for s in range(size, max_size):
        total = matrix[j+s][i+s] + prev_total
        for k in range(s):
            total += matrix[j+s][i+k] + matrix[j+k][i+s]
        prev_total = total
        if total > max_power:
            max_power = total
            max_coord = [j+1, i+1, s+1]
    return max_coord, max_power

serial_number = 5235
matrix = []
for i in range(300):
    matrix.append([])
    for j in range(300):
        power = calculate_power_level(i+1, j+1, serial_number)
        matrix[i].append(power)
max_coord = [1,1,0]
max_power = 0
for j in range(1, 300):
    for i in range(1, 300):
        max_size = min(300-i, 300-j)
        coord, power = calculate_total_power(matrix, i, j, max_size)
        if power > max_power:
            max_power = power
            max_coord = coord
print(max_coord)