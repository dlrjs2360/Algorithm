import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")


from collections import defaultdict
n = int(input())

dp = [0] * (n+1)
count = [0] * (n+1)
graph = defaultdict(list)

for i in range(1,n+1):
    t, c, *arr = map(int,input().split())
    dp[i] = t
    count[i] = c
    for x in arr:
        graph[i].append(x)

# 블로그에서 얻은 알고리즘
for i in range(1,n+1):
    tmp = 0
    for j in graph[i]:
        tmp = max(tmp,dp[j])
    dp[i] += tmp

print(max(dp))






# 맨 처음 내가 생각한 알고리즘
# 1.선행작업이 없는 작업을 먼저 선정

# 2.수행가능한 작업들 중 가장 적게 걸리는 시간을 구해서 시간을 증가시킴
# 3.시간을 증가시켜서 수행가능한 작업들 중 완료된 작업을 구함
# 4.작업이 완료됨에 따라 더 수행가능한 작업이 있는지 확인 후 수행가능한 작업으로 이동
# 5.2번부터 다시 반복

# 6.더 이상 수행가능한 작업이 없다면 종료
