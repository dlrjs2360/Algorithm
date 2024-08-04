N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split())

dist = [[1e9] * N for _ in range(N)]

vrs = []

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            vrs.append([i,j,arr[i][j]])
            dist[i][j] = 0

for a,b,c in sorted(vrs, key= lambda d: d[2]):
    for i in range(N):
        for j in range(N):
            if (d := abs(a-i) + abs(b-j)) < dist[i][j]:
                arr[i][j] = c
                dist[i][j] = d

print(arr[X-1][Y-1] if dist[X-1][Y-1] <= S else 0)