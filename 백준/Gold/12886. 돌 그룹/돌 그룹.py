def BFS(s):
    visited = [[False] * (total + 1) for _ in range(total+1)]
    a,b = s[0],s[1]
    Q = deque()
    Q.append((a,b))
    visited[a][b] = True
    while Q:
        x,y = Q.popleft()
        z = total - x - y
        if x == y == z:
            return True
        for v1,v2 in [(x,y),(y,z),(z,x)]:
            if v1 > v2:
                v1,v2 = v2,v1
            v2 = v2-v1
            v1 = 2*v1
            v3 = total - v1 - v2
            v1,v2 = max(v1,v2,v3),min(v1,v2,v3)
            if not visited[v1][v2]:
                visited[v1][v2] = True
                Q.append((v1,v2))

    return False

from collections import deque
s = sorted(list(map(int,input().split())))
target = sum(s) // 3
total = sum(s)

if sum(s) % 3 != 0:
    print(0)
else:
    print(int(BFS(s)))
