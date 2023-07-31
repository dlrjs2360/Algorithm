import sys
input = sys.stdin.readline

C,N = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
MAX = int(1e9)

dp = [MAX] * (C+1)
for cost,count in city: dp[min(C,count)] = min(dp[min(C,count)],cost)

for i in range(C+1):
    if dp[i] == MAX: continue
    for cost,count in city:
        idx = min(C, count + i)
        dp[idx] = min(dp[idx], dp[i] + cost)

print(dp[C])