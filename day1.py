x = 0
y = 0
deltas = [ *zip([-1, 0, 1, 0], [0, 1, 0, -1])]
v = 0
visited = set()
p2 = True
for dl in open('1.in', 'r').read().strip().split(', '):
    d = dl[0]
    l = int(dl[1:])
    if d == 'R':
        v += 5
    else:
        v += 3
    v %= 4
    dr, dc = deltas[v]
    for step in range(l):
        x, y = x + dr, y + dc
        if p2 and (x, y) in visited:
            print(abs(x) + abs(y))
            p2 = False
        elif p2:
            visited.add((x, y))
    
print(abs(x) + abs(y))
