from collections import defaultdict

part1 = [defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)]
for line in open('6.in').read().splitlines():
    for i, e in enumerate(line):
        part1[i][e] += 1

part1ans = ''
part2ans = ''
for d in part1:
    m = 0
    m2 = 100000
    c = ''
    c2 = ''
    for k, v in d.items():
        if m < v:
            c = k
            m = v
        if m2 > v:
            c2 = k
            m2 = v
    part1ans += c
    part2ans += c2
print(part1ans)
print(part2ans)
            
        
    

