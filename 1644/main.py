import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', "r")

n = int(input())

# 에라토스테네스의 체
a = [False, False] + [True] * (n - 1)
prime = []
for i in range(2, n +1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

ans = 0
start, end = 0, 0
while end <= len(prime):
    tmp = sum(prime[start:end])
    if tmp == n:
        ans += 1
        end += 1
    elif tmp < n:
        end += 1
    else:
        start += 1

print(ans)

