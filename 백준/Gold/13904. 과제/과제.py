import sys
import heapq

N = int(input())
reports = []
answer = [0] * 1001 # N 개의 최대값 +1 만큼 해준다.

for _ in range(N):
    day, value = map(int, sys.stdin.readline().split())
    reports.append([-value, day, value])

heapq.heapify(reports)

while reports:
    temp = heapq.heappop(reports)
    for i in range(temp[1], 0, -1):
        if answer[i] == 0:
            answer[i] = temp[2]
            break

print(sum(answer))