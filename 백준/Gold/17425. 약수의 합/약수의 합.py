import sys
input = sys.stdin.readline

MAX = 1000000
ans = [0 for _ in range(MAX+1)]
for i in range(1,MAX+1):
    for j in range(i,MAX+1,i):
        ans[j] += i
    ans[i] += ans[i-1]
for _ in range(int(input())):
    n = int(input())
    print(ans[n])