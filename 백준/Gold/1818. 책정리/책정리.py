from bisect import bisect_left

N = int(input())
arr = list(map(int,input().split()))
lis = [arr[0]]
for x in arr[1:]:
    if x > lis[-1]:
        lis.append(x)
        continue
    lis[bisect_left(lis,x)] = x
print(N-len(lis))