from hashlib import md5

doorid = 'reyedfim'
ctr = 0
part1 = ''
part2 = ['z'] * 8
print(part2)
while True: 
    m = md5()
    m.update(bytes(doorid + str(ctr), 'UTF-8'))
    h = m.hexdigest()
    if h[0:5] == '00000':
        five = h[5]
        six = h[6]
        if len(part1) < 8:
            part1 += five
        if five in '01234567' and part2[int(five)] == 'z':
            part2[int(five)] = six
        if 'z' not in part2:
            break
    ctr += 1
print(part1)
print(''.join(part2))

