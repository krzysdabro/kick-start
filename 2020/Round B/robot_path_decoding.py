DMAP = {
    'N': [1, -1],
    'S': [1, 1],
    'W': [0, -1],
    'E': [0, 1]
}
DKEYS = DMAP.keys()
POS_MAX = 10**9
POS_MIN = 1

def decode(program):
    plen, i = len(program), 0
    result = []
    repeat, subprogram_start, unclosed_p = 1, 0, 0
    while i < plen:
        if program[i] == '(':
            if unclosed_p == 0:
                repeat, subprogram_start = int(program[i-1]), i+1
            unclosed_p = unclosed_p + 1
        elif program[i] == ')':
            unclosed_p = unclosed_p - 1
            if unclosed_p == 0:
                result.extend(repeat * decode(program[subprogram_start:i]))
        elif program[i] in DKEYS and unclosed_p == 0:
            result.append(program[i])
        i = i + 1

    return result

def move(d):
    x = DMAP[d]
    pos[x[0]] = pos[x[0]] + x[1]
    if pos[x[0]] < POS_MIN:
        pos[x[0]] = POS_MAX
    elif pos[x[0]] > POS_MAX:
        pos[x[0]] = POS_MIN


t = int(input())
for case in range(t):
    pos = [1, 1]
    program = input()

    for x in decode(program):
        move(x)

    print(f'Case #{case+1}: {pos[0]} {pos[1]}')
