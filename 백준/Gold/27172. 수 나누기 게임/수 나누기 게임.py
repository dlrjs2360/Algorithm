n = int(input())
card = list(map(int,input().split()))

visit = [False] * (int(1e6)+1)
for i,c in enumerate(card): visit[c] = True

MAX = max(card)
answer = [0] * (MAX+1)
for x in sorted(card):
    for j in range(x*2,MAX+1,x):
        if visit[j]:
            answer[x] += 1
            answer[j] -= 1

print(*[answer[x] for x in card])