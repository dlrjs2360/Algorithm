def DFS(idx,cnt,total):
    global answer
    if total == target:
        answer = min(answer,cnt)
        return
    if idx >= m:
        return
    DFS(idx+1, cnt+1, total | students[idx])
    DFS(idx+1, cnt, total)

n,m = map(int,input().split())
students = [0] * m
target = 0
for i in range(n):
    target |= (1 << i)

for i in range(m):
    q, *arr = map(int,input().split())
    tmp = 0 if students[i] == 0 else students[i]
    for p in arr:
        tmp |= (1 << (p-1))
    students[i] = tmp

answer = 1e9
DFS(0,0,0)
print(answer if answer < 1e9 else -1)