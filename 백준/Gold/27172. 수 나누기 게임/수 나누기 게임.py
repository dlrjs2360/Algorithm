n = int(input())
card = list(map(int,input().split()))
pcard = sorted([(i,card[i]) for i in range(n)],key=lambda x: x[1])

visit = [False] * (int(1e6)+1)
idx = {}
for i,c in enumerate(card):
    visit[c] = True
    idx[c] = i

MAX = max(card)
answer = [0] * n
for i,x in pcard:
    for j in range(x*2,MAX+1,x):
        if visit[j]:
            answer[i] += 1
            answer[idx[j]] -= 1

print(*answer)