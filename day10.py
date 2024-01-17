from collections import defaultdict, deque
L = defaultdict(list)
I = {}
for line in open('10.in', 'r').read().splitlines():
    T = line.split()
    if T[0] == 'value':
        v = int(T[1])
        b = int(T[-1])
        L[b].append(v)
    else:
        b = int(T[1] )
        if T[5] == 'bot':
            v1 = int(T[6])
            v2 = -1
        else:
            v1 = -1
            v2 = int(T[6])
        if T[-2] == 'bot':
            v3 = int(T[-1])
            v4 = -1
        else:
            v3 = -1
            v4 = int(T[-1])

        I[b] = (v1, v2, v3, v4)

Q = deque()
for k, v in L.items():
    if len(v) == 2:
        Q.append(k)
        break

p2 = 1
while Q:
    bot = Q.popleft()
    a, b = sorted(L[bot])
    if a == 17 and b == 61:
        print(bot)
    L[bot] = []
    b1, o1, b2, o2 = I[bot]
    if b1 > -1:
        L[b1].append(a)
    elif o1 > -1 and o1 < 3:
        p2 *= a
    if b2 > -1:
        L[b2].append(b)
    elif o2 > -1 and o2 < 3:
        p2 *= b
    #print(L[b1])
    #print(L[b2])

    if len(L[b1]) == 2:
        Q.append(b1)
    if len(L[b2]) == 2:
        Q.append(b2)

print(p2)
