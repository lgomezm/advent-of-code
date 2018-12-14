class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.next_intersection = 'L'
        self.active = True

    def update_next_intersection(self):
        if self.next_intersection == 'L':
            self.next_intersection = 'S'
        elif self.next_intersection == 'R':
            self.next_intersection = 'L'
        elif self.next_intersection == 'S':
            self.next_intersection = 'R'

def read_input():
    with open('../input/day13.txt') as f:
        lines = f.readlines()
    m = []
    carts = []
    j = 0
    path_segments = {'v': '|', '^': '|', '<': '-', '>': '-'}
    for line in lines:
        i = 0
        r = list(line.strip('\n'))
        for k in range(len(r)):
            if r[k] in ['v', '^', '<', '>']:
                carts.append(Cart(i, j, r[k]))
                r[k] = path_segments[r[k]]
            i += 1
        m.append(r)
        j += 1
    return carts, m

def move_down(cart, next_loc):
    cart.y = cart.y+1
    if next_loc == '\\':
        cart.direction = '>'
    elif next_loc == '/':
        cart.direction = '<'
    elif next_loc == '+':
        if cart.next_intersection == 'L':
            cart.direction = '>'
        elif cart.next_intersection == 'R':
            cart.direction = '<'

def move_up(cart, next_loc):
    cart.y = cart.y-1
    if next_loc == '\\':
        cart.direction = '<'
    elif next_loc == '/':
        cart.direction = '>'
    elif next_loc == '+':
        if cart.next_intersection == 'L':
            cart.direction = '<'
        elif cart.next_intersection == 'R':
            cart.direction = '>'

def move_left(cart, next_loc):
    cart.x = cart.x-1
    if next_loc == '\\':
        cart.direction = '^'
    elif next_loc == '/':
        cart.direction = 'v'
    elif next_loc == '+':
        if cart.next_intersection == 'L':
            cart.direction = 'v'
        elif cart.next_intersection == 'R':
            cart.direction = '^'

def move_right(cart, next_loc):
    cart.x = cart.x+1
    if next_loc == '\\':
        cart.direction = 'v'
    elif next_loc == '/':
        cart.direction = '^'
    elif next_loc == '+':
        if cart.next_intersection == 'L':
            cart.direction = '^'
        elif cart.next_intersection == 'R':
            cart.direction = 'v'

def move(cart, m):
    if cart.direction == 'v':
        move_down(cart, m[cart.y+1][cart.x])
    elif cart.direction == '^':
        move_up(cart, m[cart.y-1][cart.x])
    elif cart.direction == '<':
        move_left(cart, m[cart.y][cart.x-1])
    elif cart.direction == '>':
        move_right(cart, m[cart.y][cart.x+1])
    if m[cart.y][cart.x] == '+':
        cart.update_next_intersection()

def count_active(carts):
    count = 0
    for c in carts:
        if c.active:
            count += 1
    return count

carts, m = read_input()
active_count = count_active(carts)
while active_count > 1:
    for c in carts:
        if c.active:
            move(c, m)
            for c2 in carts:
                if c2.active and c2 != c and c2.x == c.x and c2.y == c.y:
                    print('Crash in:',(c.x,c.y))
                    c.active = False
                    c2.active = False
    active_count = count_active(carts)
for c in carts:
    if c.active:
        print(c.x,',',c.y)