t = int(input())

for case in range(1, t+1):
    n, budget = (int(i) for i in input().split(' '))

    houses = [int(i) for i in input().split(' ')]
    houses.sort()

    bought_houses = 0
    total_cost = 0
    for house in houses:
        if total_cost + house > budget:
            break
        total_cost = total_cost + house
        bought_houses = bought_houses + 1

    print(f'Case #{case}: {bought_houses}')
