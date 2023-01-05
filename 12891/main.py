import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

s, p = map(int,input().split())
arr = input()
contain = list(map(int,input().split()))
word = ["A","C","G","T"]
def getAns(check):
    for i in range(4):
        if check[i] < contain[i]:
            return 0
    else:
        return 1

ans = 0
check = [0] * (4)
start = 0
end = start+p-1

for x in arr[start:end + 1]:
    if x in word:
        check[word.index(x)] += 1

while end < s:
    ans += getAns(check)

    if arr[start] in word:
        check[word.index(arr[start])] -= 1
    start += 1

    end += 1
    if end >= s:
        break
    if arr[end] in word:
        check[word.index(arr[end])] += 1

print(ans)