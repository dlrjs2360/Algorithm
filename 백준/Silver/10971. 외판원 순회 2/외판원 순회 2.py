def DFS(start,node,total,visited):
    global answer
    if start == node and bin(visited).split("b")[1] == "1"*n:
        answer = min(answer,total)
        return
    for i in range(n):
        if visited & (1 << i) or W[node][i] == 0:
            continue
        DFS(start, i, total+W[node][i], visited | (1 << i))

n = int(input())
W = [list(map(int,input().split())) for _ in range(n)]
answer = 1e9
DFS(1,1,0,0)

print(answer)