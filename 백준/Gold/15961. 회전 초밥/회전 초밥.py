from collections import defaultdict
n,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]
answer = 0
res = 0
kind = defaultdict(int)
for start in range(n+k):
    idx = start if start < n else start - n
    if kind[sushi[idx]] == 0:
        res += 1
    kind[sushi[idx]] += 1
    if start >= k:
        kind[sushi[start-k]] -= 1
        if kind[sushi[start-k]] == 0:
            res -= 1
    answer = max(answer,res + int(not kind[c]))

print(answer)