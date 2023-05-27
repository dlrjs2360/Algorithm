from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
answer = [arr[0]]
for x in arr[1:]:
    if x > answer[-1]: answer.append(x)
    else: answer[bisect_left(answer,x)] = x
print(len(answer))