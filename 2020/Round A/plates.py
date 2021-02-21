def calc_sum(s, plates):
    if s >= len(stacks) or plates == 0:
        return 0

    result = 0
    for j in range(min(plates, len(stacks[s])), -1, -1):
        r = sum(stacks[s][:j]) + calc_sum(s+1, plates-j)
        result = r if r > result else result

    return result


def calc_sum2(s, plates):
    if s >= n or plates == 0:
        return 0

    if plates in dp[s]:
        return dp[s][plates]

    results = []
    for i in range(min(k, plates)+1):
        results.append(stack_sum[s][i] + calc_sum2(s+1, plates-i))

    dp[s][plates] = max(results)
    return dp[s][plates]


t = int(input())
for case in range(1, t+1):
    n, k, p = (int(i) for i in input().split(' '))
    stacks = [[int(v) for v in input().split(' ')] for i in range(n)]
    stack_sum = [[sum(s[:i]) for i in range(k+1)] for s in stacks]
    dp = {s: {} for s in range(n)}

    value = calc_sum2(0, p)
    print(f'Case #{case}: {value}')
