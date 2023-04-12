from collections import defaultdict

n,m = map(int,input().split())
preq = defaultdict(list)

count = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    preq[a].append(b)
    count[b] += 1

q = []
answer = [0] * (n+1)
for i in range(1,n+1):
    if count[i] == 0:
        q.append(i)
        answer[i] = 1

sem = 0
while q:
    sem += 1
    tmp = []
    for x in q:
        for y in preq[x]:
            count[y] -= 1
            if count[y] == 0:
                tmp.append(y)
                answer[y] = sem+1
    q = tmp

print(*answer[1:])