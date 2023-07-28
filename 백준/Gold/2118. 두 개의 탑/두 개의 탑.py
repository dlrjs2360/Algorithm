import sys
input = sys.stdin.readline

n = int(input())
distance = [int(input()) for _ in range(n)]

point = [0] * (n + 1)

for i in range(n): point[i + 1] = point[i] + distance[i]
result = 0

total, right = point[-1], 1
for left in range(n):
    while right < n + 1 and point[right] - point[left] <= total - point[right] + point[left]:
        result = max(result, point[right] - point[left])
        right += 1

print(result)