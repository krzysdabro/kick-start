t = int(input())

for case in range(t):
    n, d = (int(i) for i in input().split(' '))
    x = [int(i) for i in input().split(' ')]

    for start_day in range(d, 0, -1):
        if start_day % x[0] != 0:
            continue

        bus = 1
        for day in range(start_day, d+1):
            for i in range(bus, n):
                if day % x[bus] != 0:
                    break
                bus = bus + 1

        if bus == n:
            print(f'Case #{case+1}: {start_day}')
            break
