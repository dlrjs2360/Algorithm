def Eratos(n):
    visit_era = [False, False] + [True] * (n - 1)
    prime_era = []
    for i in range(2, n + 1):
        if visit_era[i]:
            if i > 1000:
                prime_era.append(i)
            for j in range(2 * i, n + 1, i):
                visit_era[j] = False
    return prime_era

prime = Eratos(10000)
from collections import deque
T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    visit = {a}
    Q = deque()
    Q.append((a,0))
    while Q:
        node, count = Q.popleft()
        if node == b:
            print(count)
            break
        for idx in range(4):
            for change in range(10):
                tmp = int(str(node)[:idx] + str(change) + str(node)[idx + 1:])
                if tmp > 1000 and tmp in prime and tmp not in visit:
                    visit.add(tmp)
                    Q.append((tmp, count+1))
