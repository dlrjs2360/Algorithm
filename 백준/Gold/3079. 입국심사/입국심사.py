import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]

answer = 0
left, right = 0, int(1e9)*m
while left <= right:
    cnt = 0
    mid = (left+right)//2
    for x in arr:
        cnt += mid // x
    if cnt >= m:
        answer = mid
        right = mid - 1
        continue
    left = mid + 1

print(answer)