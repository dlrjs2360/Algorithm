

n = int(input())
arr = list(map(int,input().split()))

res = [arr[0]]
for i in range(1,n):
    x = arr[i]
    if x > res[-1]:
        res.append(x)
        continue

    left, right = 0, len(res)
    idx = 0
    while left <= right:
        mid = (left+right) // 2
        val = res[mid]
        if val >= x:
            right = mid - 1
            idx = mid
        else:
            left = mid + 1
    res[idx] = x

print(len(res))