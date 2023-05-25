def dfs(idx, t):
    result[idx] = t
    visit[idx] = 1
    for i in range(n):
        if s[idx][i] == 1 and visit[i] == 0:
            dfs(i, -t)

n = int(input())
s = [[0] * n for i in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in a[1:]:
        s[i][j - 1] = 1
        s[j - 1][i] = 1

visit = [0 for i in range(n)]
result = [0 for i in range(n)]

for i in range(n):
    if visit[i] == 0:
        dfs(i, 1)

print(result.count(1))
for i in range(n):
    if result[i] == 1:
        print(i + 1, end=" ")
print()

print(result.count(-1))
for i in range(n):
    if result[i] == -1:
        print(i + 1, end=" ")