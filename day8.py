display = []
width = 50
height = 6
#width = 7
#height = 3
def draw(display):
    for line in display:
        arr = ''
        for c in line:
            if c == 1:
                arr += 'x'
            else:
                arr += '.'
        print(arr)
for _ in range(height):
    display.append([0] * width)

for line in open('8.in', 'r'):
    token = line.split()
    if token[0] == 'rect':
        c, r = token[1].split('x')
        r, c = int(r), int(c)
        for dr in range(r):
            for dc in range(c):
                display[dr][dc] = 1
    elif token[0] == 'rotate':
        if token[1] == 'row':
            r = int(token[2][2:])
            shift = int(token[4])
            l = display[r]
            display[r] = l[width - shift:] + l[0:width - shift]
        else:
            c = int(token[2][2:])
            shift = int(token[4])
            vals = []
            for dr in range(height):
                vals.append(display[dr][c])
            newvals = [0] * height
            for dr in range(height):
                newvals[(dr + shift) % height] = vals[dr]
            for dr in range(height):
                display[dr][c] = newvals[dr]

part1 = 0
    
draw(display)
for line in display:
    for c in line:
        if c == 1:
            part1 += 1

print(part1)
                


