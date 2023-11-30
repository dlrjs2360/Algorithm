def solution():
    N,K = map(int,input().split())
    arr = [0] * 1000001
    MAX = 0

    for _ in range(N):
        a,b = map(int,input().split())
        arr[a] += 1; arr[b] -= 1
        MAX = max(MAX,b)

    for i in range(1,MAX+1): arr[i] += arr[i-1]

    left = right = val = 0
    while right <= MAX:
        if val == K: return [left,right]
        elif val > K: val -= arr[left]; left += 1
        else: val += arr[right]; right += 1

    return [0,0]

print(*solution())