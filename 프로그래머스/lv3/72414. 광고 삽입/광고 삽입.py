from heapq import heappush,heappop

def numToTime(sec):
    h = sec // (60 * 60)
    sec %= (60 * 60)
    m = sec // 60
    sec %= 60
    s = sec
    return '%02d:%02d:%02d' % (h, m, s)

def timeToNum(time):
    h,m,s = map(int,time.split(':'))
    return h*3600 + m*60 + s

def solution(play_time, adv_time, logs):
    answer = numToTime(0)
    play_time, adv_time = timeToNum(play_time), timeToNum(adv_time)
    res = [0] * (play_time+1)
    for log in logs:
        start,end = map(timeToNum,log.split("-"))
        res[start] += 1
        res[end] -= 1
    for i in range(1,play_time+1):
        res[i] += res[i-1]
    left = 0
    MAX = total = sum(res[:adv_time])
    for t in range(adv_time,play_time+1):
        total -= res[left]
        total += res[t]
        left += 1
        if total > MAX:
            answer = numToTime(left)
            MAX = total
    return answer