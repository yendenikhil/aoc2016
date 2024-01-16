import re 

C = open('9.in', 'r').read().strip()
C2 = C
part1 = 0

while C:
    marker = re.search(r'\((\d+)x(\d+)\)', C)
    if marker:
        a, b = marker.span()
        c, reps = map(int, marker.groups())
        part1 += a + c * reps
        C = C[b + c:]
    else:
        part1 += len(C)
        break

print(part1)

def decom(C):
    length = 0
    while C:
        marker = re.search(r'\((\d+)x(\d+)\)', C)
        if marker:
            a, b = marker.span()
            c, reps = map(int, marker.groups())
            length += a + decom(C[b:b + c]) * reps
            C = C[b + c:]
        else:
            length += len(C)
            break
    return length
print(decom(C2))
        


