part1 = 0
part2 = 0

def aba(line):
    results = []
    for i in range(len(line) - 2):
        a, b, c = line[i:i + 3]
        if a == c and a != b:
            results.append(b + a + b)
    return results

def abba(line):
    for i in range(len(line) - 3):
        a, b, c, d = line[i:i + 4]
        if a == d and b == c and a != b: 
            return True
    return False


for line in open('7.in').read().splitlines():
    outside = []
    inside = []
    v = ''
    first, *rest = line.split('[')
    outside.append(first)
    for r in rest:
        a, b = r.split(']')
        inside.append(a)
        outside.append(b)
    part2o = []
    for o in outside:
        for r in aba(o):
            part2o.append(r)

    p2 = False
    for i in inside:
        for o in part2o:
            if o in i:
                part2 += 1
                p2 = True
                break
        if p2:
            break

    check = False
    for mid in inside:
        check = check or abba(mid)
        if check:
            break
    if check:
        continue

    for left in outside:
        check = check or abba(left)
        if check:
            break
    if check:
        part1 += 1

print(part1)
print(part2)

