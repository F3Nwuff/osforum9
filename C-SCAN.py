def c_scan(start, inp):
    thead = 0
    pos = start
    a = 0
    while a < len(inp) and inp[a] < start:
        a += 1
    r = sorted(inp[a:])
    l = sorted(inp[:a])
    for run in r:
        thead += abs(pos - run)
        pos = run
    if r:
        thead += abs(4999 - pos)
        pos = 0
        thead += 4999
    for run in l:
        thead += abs(pos - run)
        pos = run
    return thead

def read(file):
    with open(file, 'r') as txt:
        return [int(line.strip()) for line in txt]

start = 1234
input = 'input.txt'
inp = read(input)
sortinp = sorted(inp)

tog = c_scan(start, inp)
print("Total head movements (C-SCAN) with original input:", tog)

tsort = c_scan(start, sortinp)
print("Total head movements (C-SCAN) with rearranged input:", tsort)


