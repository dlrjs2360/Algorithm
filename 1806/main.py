import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

n, s = map(int,input().split())
arr = list(map(int,input().split()))

# 불가능한 경우는 답을 0으로 설정
if sum(arr) >= s:
    ans = n
else:
    ans = 0

# 누적합 구하기
prefix = [0 for _ in range(n)]
prefix[0] = arr[0]
for i in range(1,n):
    prefix[i] = arr[i] + prefix[i-1]

# 투포인터로 가장 짧은 구간 구하기
start, end = 0, n-1
while n-1 >= end >= 0:
    subtotal = prefix[end] - prefix[start]
    res = end - start
    print(start, end, " res:", res, " subtotal:", subtotal, end=" ")
    # 구간이 이미 가장 짧은 구간보다 크거나 같으면 start를 더해서 구간을 좁히기
    if res >= ans:
        start += 1
    else: # 구간이 이미 가장 짧은 구간보다 작고 부분합이 s보다 크다면 end를 줄여서 더 작은 구간 찾기
        if subtotal >= s:
            ans = res
            print("| ans="+str(res))
            end -= 1
            continue
        # 구간이 이미 가장 짧은 구간보다 작고 부분합이 s보다 크다면 end를 키워서 구간을 넓히기
        end += 1
    print()

# 누적합 첫번째 예외사항 고치기(0번을 무조건 뺴기 때문에 발생하는 예외)
if prefix[0] >= s:
    ans = 1

print(ans)