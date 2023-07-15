A, B = input(), input()
n,m = len(A),len(B)
dp = [[""]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        up,left = dp[i-1][j], dp[i][j-1]
        if A[i-1] != B[j-1]:
            dp[i][j] = up if len(up) >= len(left) else left
            continue
        dp[i][j] = dp[i-1][j-1] + A[i-1]
print(len(dp[-1][-1]))
print(dp[-1][-1])