import sys
input = sys.stdin.readline

N = int(input())

dp_max = list(map(int,input().split()))
dp_min = [dp_max[0],dp_max[1],dp_max[2]]

for _ in range(N-1):
    arr = list(map(int,input().split()))
    dp_max = [max(dp_max[:2])+arr[0], max(dp_max)+arr[1], max(dp_max[1:])+arr[2]]
    dp_min = [min(dp_min[:2])+arr[0], min(dp_min)+arr[1], min(dp_min[1:])+arr[2]]

print(max(dp_max),min(dp_min))