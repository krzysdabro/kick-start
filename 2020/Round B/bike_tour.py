t = int(input())

for case in range(t):
    n = int(input())
    h = [int(x) for x in input().split(' ')]

    peaks = 0
    for i in range(1, n-1):
        if h[i] > h[i-1] and h[i] > h[i+1]:
            peaks = peaks + 1

    print(f'Case #{case+1}: {peaks}')
