def scan(start, inp):
    thead = 0
    pos = start
    a = 0
    while a < len(inp) and inp[a] < start:
        a += 1
    r = sorted(inp[a:])
    l = sorted(inp[:a], reverse=True)
    for run in l:
        thead += abs(pos - run)
        pos = run
    pos = start
    for run in r:
        thead += abs(pos - run)
        pos = run
    return thead

def read(file):
    with open(file, 'r') as txt:
        return [int(line.strip()) for line in txt]

start = 1456
input = 'input.txt'
inp = read(input)
sortinp = sorted(inp)

tog = scan(start, inp)
print("Total head movements (SCAN):", tog)

tsort = scan(start, sortinp)
print("Total head movements sorted (SCAN):", tsort)