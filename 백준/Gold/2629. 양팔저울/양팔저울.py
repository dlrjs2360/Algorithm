N = int(input()) # N < 30
plumb = list(map(int,input().split())) # plumb <= 500
M = int(input()) # M < 7
marbles = list(map(int,input().split())) # marble <= 40000

MAX = 40001
res = [False] * MAX
res[0] = True

maxValue = 0
for p in plumb: # 30
    tmp = set()
    for i in range(max(maxValue+1, 1)):
        if not res[i]: continue
        if (p + i) <= MAX: tmp.add(p + i)
        tmp.add(abs(p - i))
        maxValue = max(maxValue, p+i)
    for x in tmp: res[x] = True

print(*("Y" if res[x] else "N" for x in marbles))
