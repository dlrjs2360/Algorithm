def spin(S,n):
    return S[n:]+S[:n]
    
def check(S,dic):
    stack = []
    for x in list(S):
        if not stack or x in ('(','[','{'):
            stack.append(x)
            continue
        if stack.pop() != dic[x]:
            return False
    return not stack
        
    
def solution(s):
    answer = 0
    dic = {'}':'{', ']':'[', ')':'('}
    for i in range(len(s)):
        answer += check(spin(s,i),dic)
    return answer