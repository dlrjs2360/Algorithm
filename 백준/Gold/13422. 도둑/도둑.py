import sys
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    money = list(map(int, input().split()))

    if M == 1: return sum(1 for x in money if x < K)
    if M == N: return int(sum(money) < K)

    answer = 0
    S = 0
    for i in range(N+M-1):
        S += money[i % N]
        if i >= M: S -= money[i - M]
        if S < K and i >= M-1: answer += 1

    return answer

for _ in range(int(input())):
    print(solve())