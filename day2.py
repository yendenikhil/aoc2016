pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pad2 = [
['x', 'x', '1', 'x', 'x'],
['x', '2', '3', '4', 'x'],
['5', '6', '7', '8', '9'],
['x', 'A', 'B', 'C', 'x'],
['x', 'x', 'D', 'x', 'x']
]        
rlen = 3
clen = 3
rlen2 = 5
clen2 = 5
r, c = 1, 1
r2, c2 = 2, 0
part1 = ''
part2 = ''
for line in open('2.in', 'r').read().splitlines():
    for x in line:
        if x == 'U':
            nr, nc = r - 1, c
            nr2, nc2 = r2 - 1, c2
        elif x == 'D':
            nr, nc = r + 1, c
            nr2, nc2 = r2 + 1, c2
        elif x == 'L':
            nr, nc = r, c - 1
            nr2, nc2 = r2, c2 - 1
        elif x == 'R':
            nr, nc = r, c + 1
            nr2, nc2 = r2, c2 + 1
        if 0 <= nr < rlen and 0 <= nc < clen:
            r, c = nr, nc
        if 0 <= nr2 < rlen2 and 0 <= nc2 < clen2 and pad2[nr2][nc2] != 'x':
            r2, c2 = nr2, nc2
    part1 += str(pad[r][c])
    part2 += pad2[r2][c2]

print(part1)
print(part2)
        

