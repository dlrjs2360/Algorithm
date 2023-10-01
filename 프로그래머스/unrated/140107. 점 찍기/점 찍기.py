from math import sqrt

def solution(k, d):
    answer = 0
    summ = 0

    for y in range(0, d + 1, k):
        x = d ** 2 - y ** 2
        cnt = sqrt(x) // k + 1
        summ += cnt

    return summ