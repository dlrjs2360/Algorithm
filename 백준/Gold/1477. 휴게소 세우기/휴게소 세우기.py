import sys
input = sys.stdin.readline

def Check(v, mid) -> bool:
    cnt = 0
    for i in range(1, len(v)):
        cnt += (v[i] - v[i - 1] - 1) // mid
    return cnt

n, m, k, *v = map(int, open(0).read().split())
v.append(0); v.append(k); v.sort()

lo, hi = 0, k
while lo + 1 < hi:
    mid = lo + hi >> 1
    if Check(v, mid) > m: lo = mid
    else: hi = mid
print(hi)