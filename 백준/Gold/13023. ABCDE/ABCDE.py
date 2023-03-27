import sys
input = sys.stdin.readline

def DFS(node,cnt):
    global answer
    if cnt == 4 or answer == 1:
        answer = 1
        return
    for fnext in friends[node]:
        if not visit[fnext]:
            visit[fnext] = True
            DFS(fnext, cnt + 1)
            visit[fnext] = False
n,m = map(int,input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = 0

for start in range(n):
    visit = [False] * n
    visit[start] = True
    DFS(start,0)
    if answer == 1:
        break

print(answer)