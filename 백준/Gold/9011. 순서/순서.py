def solution(n, arr):
    answer = [0] * n
    v = list(range(1,n+1))
    check = 1
    for i in range(n-1,-1,-1):
        to = arr[i]
        if to >= len(v):
            return []
        answer[i] = v[to]
        v.pop(to)
    return answer

for _ in range(int(input())):
    if answer := solution(int(input()), list(map(int, input().split()))): print(*answer)
    else: print("IMPOSSIBLE")