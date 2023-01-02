import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

#  입력받기
n = int(input())

ans, start, end = 1, 1, 2
while end <= n//2+1: # 15 -> 7+8 // 9는 사용하지 안흔다. 연속된 수를 다룰 때 사실상 의미가 없다고 볼 수 있습니다.
    print(start, end, end =" ")
    if start >= end:
        end += 1
    subtotal = (end-start+1)*(start+end)//2
    print(subtotal) # start = subtotal을 줄이는데 사용한다/ 둥 = 늘리는데 사용한다.
    if subtotal == n:
        ans += 1
        end += 1
    elif subtotal < n:
        end += 1
    else:
        start += 1

print(ans)

