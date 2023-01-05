import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")


from collections import deque
n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

Q = deque()
ans = []
for i in range(n):

    # 맨 뒤부터 현재 값보다 큰 값 제거
    while Q and Q[-1][0] > arr[i]:
        Q.pop()

    # 맨 앞부터 범위를 벗어난 값 제거
    while Q and Q[0][1] < i - k + 1:
        Q.popleft()

    # 현재 값 추가
    Q.append((arr[i], i))

    # 정답 추가
    ans.append(Q[0][0])

# 정답 출력
print(*ans)