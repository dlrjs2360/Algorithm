def solution():
    N,K = map(int,input().split())
    arr = [0] * 1000001
    for _ in range(N):
        a,b = map(int,input().split())
        for i in range(a,b): arr[i] += 1

    left,right,val = 0,0,0
    while left <= right < 1000001:
        if val == K: return [left,right]
        elif val > K: val -= arr[left]; left += 1
        else: val += arr[right]; right += 1

    return [0,0]

print(*solution())