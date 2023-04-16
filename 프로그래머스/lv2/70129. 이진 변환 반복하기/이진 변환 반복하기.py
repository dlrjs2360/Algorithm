def solution(s):
    cnt,zero = 0,0
    while s != '1':
        zero += len(s) - (c1:=s.count('1'))
        s = bin(c1).split('b')[1]
        cnt += 1
    return [cnt,zero]