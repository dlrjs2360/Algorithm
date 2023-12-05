from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
children = [set() for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
plan = list(map(int, input().split())) # 방문 순서

start = 1
q= deque()
q.append(start)
visited[start]= 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if visited[next] == -1: # 방문 안한 곳
            visited[next] = visited[now] + 1 #visited를 통해 여러가지 경우의 수를 고려할 수 있다.
            children[now].add(next)
            q.append(next)
next_index = 1
for i in plan:
    if next_index == n:
        break
    c_length = len(children[i]) #노드 i의 자식들의 개수를 확인
    c1 = set(plan[next_index:next_index+c_length])  #노드i의 자식들이 나올 수 있는 index를 통해 그 안에 입력값 value를 모아놓은 집합
    c2 = children[i] #노드i의 자식들 집합
    if c1 != c2:
        print(0)
        exit()
    next_index += c_length
print(1)