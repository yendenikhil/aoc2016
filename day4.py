part1 = 0
from collections import defaultdict
for line in open('4.in', 'r').read().splitlines():
    left, checksum = line[:-1].split('[')
    *rooms, sector = left.split('-')
    sector = int(sector)
    roomnames = rooms
    rooms = ''.join(rooms)
    reps = defaultdict(int)
    for x in rooms:
        reps[x] += 1
    rreps = defaultdict(list)
    for k, v in reps.items():
        rreps[v].append(k)
    reps = {}
    for k, v in rreps.items():
        reps[k] = ''.join(sorted(v))
    calc = ''
    for k in sorted(reps.keys(), reverse=True):
        calc += reps[k]
        if len(calc) >= 5:
            break
    calc = calc[:5]
    if checksum == calc:
        part1 += sector
        decs = []
        for room in roomnames:
            dec = ''
            for x in room:
                dec += chr((ord(x) - 97 + sector) % 26 + 97)
            decs.append(dec)
        if 'northpole' in decs:
            print('part2:', sector)

print('part1:', part1)
        
        

