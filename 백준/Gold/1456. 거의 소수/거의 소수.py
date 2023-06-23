m, n = map(int, input().split())

prime = [True] * (int(n ** 0.5) + 1)
prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i**2, int(n ** 0.5) + 1, i):
            prime[j] = False

count = 0
for i in range(1, len(prime)):
    if prime[i]:
        res = i * i
        while 1:
            if res > n: break
            count += int(res >= m)
            res *= i

print(count)