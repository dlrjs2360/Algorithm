n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for _ in range(k+1)]
for a in arr:
    w,v = a
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)

print(dp[-1])