import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    gem = [int(input()) for _ in range(N)]

    prefix = [gem[0]]
    for i in range(1, N): prefix.append(prefix[i - 1] + gem[i])

    dp = [prefix[0]]
    for i in range(1,N): dp.append(min(dp[i-1],prefix[i]))

    answer = 0 if M > 1 else prefix[0]
    for i in range(M,N):
        answer = max(prefix[i] - min(0,dp[i-M]), answer)

    return max(0,answer)

print(solution())