'''
만약에 6이라면?
10이 6보다 큼 -> 6이 5보다 큼 -> 10의 거듭제곱형태로 더이상 비교 불가능 -> 10,-1,-1,-1,-1 / +1,+1,+1,+1,+1,+1
반씩 나눠가면서 0으로 만들기 
'''

def solution(s):
    answer =  0
    stack = list(map(int,list(str(s))))[::-1]
    while stack:
        x = stack.pop()
        if x > 5:
            if stack:
                stack[-1] += 1
                answer += 10-x
            else:
                answer += 10-x+1
        elif x < 5:
            answer += x
        else:
            if stack and stack[-1] >= 5:
                stack[-1] += 1
                answer += 10-x
            else:
                answer += x
    return answer