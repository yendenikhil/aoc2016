from copy import deepcopy
from itertools import combinations
from collections import defaultdict, deque
import re
L = []
for line in open('11.in', 'r').read().splitlines():
    T = line[:-1].replace(',', '').split()
    E = []
    for i, v in enumerate(T):
        if v == 'microchip':
            E.append(T[i - 1].replace('-compatible', '') + 'm')
        elif v == 'generator':
            E.append(T[i - 1] + 'g')
    #print(line)
    #print(E)
    L.append(E)


def valid(F):
    for N in F:
        M = []
        G = []
        for e in N:
            if e[-1] == 'g':
                G.append(e[:-1])
            elif e[-1] == 'm':
                M.append(e[:-1])
        if len(G) == 0:
            continue
        for chip in M:
            if chip not in G:
                return False
    return True


def next(e, F):
    a = e - 1
    b = e + 1
    up = []
    down = []
    NL = []
    if len(F[e]) > 0:
        for ele in combinations(F[e], 1):
            NL.append(ele)
    if len(F[e]) > 1:
        for ele in combinations(F[e], 2):
            NL.append(ele)
    if a >= 0:
        for N in NL:
            NF = deepcopy(F)
            for ele in N:
                if ele in NF[e]:
                    NF[e].remove(ele)
                NF[a].append(ele)
            down.append(NF)
    if b < len(F):
        for N in NL:
            NF = deepcopy(F)
            for ele in N:
                if ele in NF[e]:
                    NF[e].remove(ele)
                NF[b].append(ele)
            up.append(NF)
    return (up, down)
            

        

def solve(L):
    Q = deque()
    Q.append([0, 0, L])
    visited = set()
    while Q:
        e, steps, F = Q.popleft()
        for ele in F:
            ele.sort()
        if str((e, F)) in visited:
            continue
        visited.add(str((e, F)))
        if all(len(x) == 0 for x in F[:-1]):
            print('solution: ', steps)
            break
        up, down = next(e, F)
        for NF in up:
            if str((e + 1, NF)) in visited:
                continue
            if valid(NF) == True:
                Q.append([e + 1, steps + 1, NF])
        for NF in down:
            if str((e - 1, NF)) in visited:
                continue
            if valid(NF) == True:
                Q.append([e - 1, steps + 1, NF])

solve(deepcopy(L))
L[0].append('eleriumg')
L[0].append('eleriumm')
L[0].append('dilithiumm')
L[0].append('dilithiumg')
solve(deepcopy(L))


