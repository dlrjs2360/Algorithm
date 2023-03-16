import bisect

def LIS(arr):
    res = [arr[0]]
    for x in arr[1:]:
        if x < res[-1]:
            res[bisect.bisect_left(res,x)] = x
            continue
        res.append(x)
    return len(res)

n = int(input())
line = sorted([list(map(int,input().split())) for _ in range(n)])
print(n-LIS([x[1] for x in line]))
