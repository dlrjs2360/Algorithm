'''
1. 모든 시간을 초로 변경
2. 구간별로 총 재생시간을 구해야 한다.
3. 시작구간이 빠른 순으로 정렬
4. 우선순위 큐를 사용하여 끝나는 구간을 탐색 -> 다음 로그를 확인하기 전에 확인
    a. start가 right보다 크다면 이전 구간과 아예 떨어짐.
    b. 누적개수를 변수로 만들어서 갱신해나가야 한다.
    c. start가 left를 넘어서면 left부터 start까지 
5. 재생횟수를 구하고 다음에 재생시간을 구하기.

# 다른방법 
1. 모든 시간을 초로 변경
2. 처음과 끝에서 먼저 광고시간만큼 계산하여 재생시간 계산
3. logs의 start와 end를 기준으로 광고시간만큼 계산
'''

from heapq import heappush,heappop

def convertor2(sec):
    h = sec // (60 * 60)
    sec %= (60 * 60)
    m = sec // 60
    sec %= 60
    s = sec
    return '%02d:%02d:%02d' % (h, m, s)

def convertor(time):
    h,m,s = map(int,time.split(':'))
    return h*3600 + m*60 + s

def solution(play_time, adv_time, logs):
    answer,res = convertor2(0),[]
    
    play_time, adv_time = convertor(play_time), convertor(adv_time)
    logs = sorted([(convertor(x.split('-')[0]),convertor(x.split('-')[1])) for x in logs])
    
    # 시작구간, 끝나는 구간을 저장
    startHeap, endHeap = [],[]
    for start,end in logs:
        heappush(startHeap,start)
        heappush(endHeap,end)
    
    # 구간마다 사람의 수 저장
    cnt,left = 0,0
    while startHeap or endHeap:
        # startHeap이 비었거나 end가 더 빠를 때
        if not startHeap or endHeap[0] <= startHeap[0]:
            tmp = heappop(endHeap)
            res.append([left,tmp,cnt])
            cnt -= 1
        else: 
            # startHeap, endHeap 모두 존재
            tmp = heappop(startHeap)
            res.append([left,tmp,cnt])
            cnt += 1
        left = tmp
    
    # 갯수 저장
    secArr = [0] * (play_time+1)
    for start,end,count in res:
        for i in range(start,end):
            secArr[i] = max(count,secArr[i])

    # 초를 갱신해가며 가장 큰 구간 찾기
    maxCount = total = sum(secArr[:adv_time])
    start = 0
    for t in range(adv_time,play_time+1):
        total += secArr[t] - secArr[start]
        start += 1
        if total > maxCount:
            answer = convertor2(start)
            maxCount = total
    return answer