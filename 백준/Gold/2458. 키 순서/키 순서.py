# 나보다 큰 사람과 작은 사람의 수의 합이 n-1과 같아야 한다.

#입력
N, M = map(int, input().split())
height = [[0 for _ in range(N+1)] for _ in range( N+1)]

for _ in range(M):
    tall, short = map(int,input().split())
    height[tall][short] = 1

#플로이드 와샬 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if height[i][k] + height[k][j] == 2:
                height[i][j] = 1

#출력
answer = 0
for i in range(1, N+1):
    known_height = 0
    for j in range(1, N+1):
        known_height += height[i][j] + height[j][i]
    if known_height == N-1:
        answer += 1
print(answer)