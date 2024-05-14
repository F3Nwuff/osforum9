def fcfs(start, inp):
    thead = 0
    pos = start
    for run in inp:
        thead += abs(run - pos)
        pos = run
    return thead

start = 1456
input = 'input.txt'

with open(input, 'r') as file:
    inp = [int(line.strip()) for line in file]

tog = fcfs(start, inp)
print("Total head movements (FCFS):", tog)

sortinp = sorted(inp)
tsort = fcfs(start, sortinp)
print("Total head movements rearranged (FCFS):", tsort)

