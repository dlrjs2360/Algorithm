from heapq import heappop,heappush

def convert(s):
    h,m = map(int,s.split(":"))
    return h*60 + m

def solution(book_time):
    answer, remain = 0, 0
    stack = []
    for s,e in sorted(book_time):
        s,e = convert(s),convert(e)
        while stack:
            if stack[0] <= s:
                remain += 1
                heappop(stack)
            else:
                break
        if remain > 0:
            remain -= 1
        else:
            answer += 1
        heappush(stack, e+10)
    return answer