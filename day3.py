part1 = 0
part2 = 0
counter = 0
for line in open('3.in', 'r').read().splitlines():
    a, b, c = line.split()
    a, b, c = int(a), int(b), int(c)
    if (a + b) > c and (b + c) > a and (a + c) > b:
        part1 += 1
    if counter % 3 == 0:
        x1, x2, x3 = a, b, c
    elif counter % 3 == 1:
        y1, y2, y3 = a, b, c
    elif counter % 3 == 2:
        z1, z2, z3 = a, b, c
        if (x1 + y1) > z1 and (y1 + z1) > x1 and (x1 + z1) > y1:
            part2 += 1
        if (x2 + y2) > z2 and (y2 + z2) > x2 and (x2 + z2) > y2:
            part2 += 1
        if (x3 + y3) > z3 and (y3 + z3) > x3 and (x3 + z3) > y3:
            part2 += 1
    counter += 1

print(part1)
print(part2)
