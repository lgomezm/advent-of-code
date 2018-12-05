class Claim:
  def __init__(self, id, margin_left, margin_top, width, height):
    self.id = id
    self.margin_left = margin_left
    self.margin_top = margin_top
    self.width = width
    self.height = height

def readClaim(text):
    parts = text.split(' ')
    id = parts[0][1:]
    margin = parts[2]
    comma_idx = margin.index(',')
    left = int(margin[:comma_idx])
    top = int(margin[comma_idx+1:-1])
    dim = parts[3]
    x_idx = dim.index('x')
    width = int(dim[:x_idx])
    height = int(dim[x_idx+1:])
    return Claim(id, left, top, width, height)

def readClaims():
    with open('../input/day3.txt') as f:
        lines = f.readlines()
        claims = []
        for line in lines:
            claims.append(readClaim(line.strip()))
        return claims

def buildMatrix(rows, columns):
    m = []
    for i in range(rows):
        m.append([])
        for _ in range(columns):
            m[i].append('.')
    return m

m = buildMatrix(1000, 1000)
claims = readClaims()
for claim in claims:
    j = claim.margin_left
    while j < claim.margin_left + claim.width:
        i = claim.margin_top
        while i < claim.margin_top + claim.height:
            if m[i][j] != '.':
                m[i][j] = 'X'
            else:   
                m[i][j] = claim.id
            i += 1
        j += 1
count = 0
for row in m:
    for c in row:
        if c == 'X':
            count += 1
print('Overlapped square inches:', count)
for claim in claims:
    j = claim.margin_left
    overlapped = False
    while j < claim.margin_left + claim.width and not overlapped:
        i = claim.margin_top
        while i < claim.margin_top + claim.height and not overlapped:
            if m[i][j] == 'X':
                overlapped = True
            i += 1
        j += 1
    if not overlapped:
        print('Not overlapped:', claim.id)
        break

    