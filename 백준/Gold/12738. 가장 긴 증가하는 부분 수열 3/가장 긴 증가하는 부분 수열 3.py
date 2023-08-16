from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))

arr = []
for x in A:
    if not arr:
        arr.append(x)
    elif x > arr[-1]:
        arr.append(x)
    elif x < arr[-1]:
        arr[bisect_left(arr,x)] = x

print(len(arr))