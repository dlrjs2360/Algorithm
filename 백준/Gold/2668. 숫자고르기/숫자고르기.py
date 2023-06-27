n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n+1)

for i in range(1,n+1):
    cycle = set()
    node = i
    if not visited[node]:
        while 1:
            next_node = arr[node]

            # 싸이클이 완성되면 방문처리
            if next_node == i:
                cycle.add(next_node)
                for c in cycle:
                    visited[c] = True
                break

            # 싸이클이 완성될 때까지 진행
            if next_node not in cycle:
                cycle.add(next_node)
                node = next_node
            else:
                break

# 방문처리 리스트를 기반으로 정답 출력
print(visited.count(True))
for i in range(1,n+1):
    if visited[i]: print(i)