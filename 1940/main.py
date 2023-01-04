import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

n = int(input())
m = int(input())
arr = sorted(list(map(int,input().split())))

ans = 0
start, end = 0, n-1
while start < end < n:
    sum = arr[start] + arr[end]
    print(start, end)
    if sum <= m:
        if sum == m:
            ans += 1
        start += 1
    else:
        end -= 1
print(ans)