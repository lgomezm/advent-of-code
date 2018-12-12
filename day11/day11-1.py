def calculate_power_level(x, y, serial_number):
    rack_id = x + 10
    rack_id_power_level = (rack_id * y) + serial_number
    rack_id_power_level *= rack_id
    rack_id_power_level = int(rack_id_power_level / 100) % 10
    return rack_id_power_level - 5

serial_number = 5235
matrix = []
for i in range(300):
    matrix.append([])
    for j in range(300):
        matrix[i].append(calculate_power_level(i+1, j+1, serial_number))
max_total = float('-inf')
max_pwr_coord = [0,0]
for j in range(297):
    for i in range(297):
        total = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if total > max_total:
            max_pwr_coord = [i+1,j+1]
            max_total = total
print(max_pwr_coord)