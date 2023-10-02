from heapq import heappush, heappop
from itertools import combinations_with_replacement, permutations

def cal_wait_time(waitings, n):
        total_time = 0
        counsel_list = []
        for _ in range(n): heappush(counsel_list, 0)
        for start, duration in waitings:
            prev_end = heappop(counsel_list)
            if start > prev_end: heappush(counsel_list, duration)
            else:
                wait_time = prev_end - start
                total_time += wait_time
                heappush(counsel_list, duration + wait_time)
        return total_time
    
def comb(n,k):
    cases = set()
    for comb in combinations_with_replacement([i for i in range(1, n - k + 2)], r=k):
        if sum(comb) != n: continue
        for perm in permutations(comb, k): cases.add(perm)
    return cases

def solution(k, n, reqs):
    result = 1e9
    waiting_list = [[] for _ in range(k)]
    for req in reqs: waiting_list[req[2] - 1].append([req[0], req[0] + req[1]])
    cases = comb(n,k)
    for case in cases:
        time = sum(cal_wait_time(waiting_list[i], case[i]) for i in range(k))
        result = min(result, time)

    return result