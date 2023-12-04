def toList(num):
    return list(x for x in range(1, N + 1) if num & (1 << x))

def dfs(i, tp, tf, ts, tv, total, visit):
    global answer, minPrice

    if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
        if total < minPrice:
            answer.clear()
            answer.append(toList(visit))
            minPrice = total
        elif total == minPrice:
            answer.append(toList(visit))
        return

    if i >= N: return

    dfs(i+1, tp+arr[i+1][0], tf+arr[i+1][1], ts+arr[i+1][2], tv+arr[i+1][3], total+arr[i+1][4], visit | (1 << i+1))
    dfs(i+1, tp, tf, ts, tv, total, visit)

    return 0

N = int(input())
mp,mf,ms,mv = map(int,input().split())
arr = [[]] + [list(map(int,input().split())) for _ in range(N)]

minPrice = 1e9
answer = []

dfs(1,0,0,0,0,0,0)
dfs(1, *arr[1], 1 << 1)

if minPrice < 1e9:
    print(minPrice)
    print(*sorted(answer)[0])
else:
    print(-1)