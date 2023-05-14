from collections import deque

turn = {
    "L":{
        "L": "D", "D": "U"
    },
    "R":{
        "L": "U", "D": "D"
    },
    "U":{
        "L": "L", "D": "R"
    },
    "D":{
        "L": "R", "D": "L"
    },
}

direction = {
    "L": [0,-1], "R": [0,1],
    "U": [-1,0], "D": [1,0]
}

n = int(input())
k = int(input())

graph = [['-']*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b] = "A"

l = int(input())
move = deque(list(input().split()) for _ in range(l))

head = [1,1]
snake = deque([[1,1]])
time = 0
way = "R"

while 1:
    time += 1
    head = [head[0]+direction[way][0],head[1]+direction[way][1]]
    if head in snake or not (1 <= head[0] <= n and 1 <= head[1] <= n): break
    snake.append(head)
    if graph[head[0]][head[1]] != "A": snake.popleft()
    else: graph[head[0]][head[1]] = "-"
    if move and time == int(move[0][0]):
        way = turn[way][move.popleft()[1]]

print(time)