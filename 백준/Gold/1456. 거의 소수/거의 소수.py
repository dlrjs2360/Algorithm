A, B = map(int, input().split())
rootB = int(B ** 0.5) + 1
prime = [True] * rootB
prime[1] = False

for i in range(2, rootB):
    if not prime[i]: continue
    for j in range(i**2, rootB, i): prime[j] = False

answer = 0
for i in range(1, len(prime)):
    if not prime[i]: continue
    res = i * i
    while 1:
        if res > B: break
        answer += int(res >= A)
        res *= i

print(answer)