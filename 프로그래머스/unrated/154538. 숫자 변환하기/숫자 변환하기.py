from collections import deque
def solution(x, y, n):
    MAX = 1e6
    dp = [MAX] * (y+1)
    q = deque([[x,0]])
    while q:
        num,cnt = q.popleft()
        if num > y:
            continue
        if dp[num] > cnt:
            dp[num] = cnt
            q.append([num+n,cnt+1])
            q.append([num*2,cnt+1])
            q.append([num*3,cnt+1])
    return dp[y] if dp[y] < MAX else -1