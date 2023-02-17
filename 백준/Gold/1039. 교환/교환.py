n, k = map(int, input().split())
n_len = len(str(n))

s1, s2 = set(), set()
s1.add(n)

for _ in range(k):
    while s1:
        x = str(s1.pop())
        for i in range(n_len-1):
            for j in range(i+1, n_len):
                if x[j] == '0' and i == 0:
                    continue
                y = x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                s2.add(int(y))
    s2, s1 = s1, s2

s1 = list(s1)
s1.sort()
if len(s1) > 0:
    print(s1[-1])
else:
    print(-1)