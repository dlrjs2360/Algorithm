import bisect

def LIS(arr):
    res = []
    for x in arr:
        if not res:
            res.append(x)
            continue
        if x < res[-1]:
            idx = bisect.bisect_left(res,x)
            res[idx] = x
            continue
        res.append(x)
    return len(res)

n = int(input())
line = [list(map(int,input().split())) for _ in range(n)]
line.sort(key=lambda x:x[0])
print(n-LIS([x[1] for x in line]))
