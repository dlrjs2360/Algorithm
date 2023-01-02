import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

n,m = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    x = arr[i]

    # 첫번째 원소는 prefix만 입력
    if i == 0:
        if x % m == 0:
            dp[i] += 1
        prefix[i] = x
        continue

    # 두번째 원소부터는 이전 prefix를 참조
    prefix[i] = x+prefix[i-1]

    # 현재 누적합이 나누어떨어지면 dp+1
    present = prefix[i]
    if present % m == 0:
        dp[i] += 1

    # dp에 이전까지 조건을 만족한 갯수를 모두 저장
    # 현재 prefix에서 이전 prefix들을 탐색하며 만약 나누어떨어지는 인덱스를 만나면 +1
    # 나누어 떨어진 인덱스의 dp값이 0이 아니라면 그 dp값을 더하고 break
    # break하는 이유는 나누어떨어진 인덱스가 있다면 그 때부터는 해당 dp의 값으로 그 이전을 대표할 수 있기 때문이다.
    j = i-1
    while j >= 0:
        past = prefix[j]
        if (present - past) % m == 0:
            if dp[j] != 0:
                dp[i] += dp[j]
                break
            dp[i] += 1
        j -= 1
print(prefix)
print(sum(dp))


'''answer = 0
for i in range(n):
    rest[i] = arr[i] % m
    if rest[i] == 0:
        answer += 1
print(rest)
'''



