'''
1. 필수로 이동해야할 방향이 정해져있음.
2. k-필수로이동해야할길이 만큼 중복으로 이동해야 한다. 중복으로 이동하기 떄문에 이 값이 홀수라면 impossible이다.
3. 필수로 이동해야할 길을 따라 이동하다가 도착지에 도착하거나 벽을 만나면 사전순으로 빠른 방향으로 중복이동하기
4. 사전순으로 빠른 순서는 'd','l','r','u'
'''

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    k -= abs(x-r)+abs(y-c)
    
    # 홀수인 경우 불가능
    if k < 0 or k%2 != 0:
        return "impossible"
    
    way = {'d':0, 'l':0, 'r':0, 'u':0}
    if x > r:
        way['u'] = x-r
    else:
        way['d'] = r-x
    if y > c:
        way['l'] = y-c
    else:
        way['r'] = c-y
        
    answer += 'd' * way['d']
    nd = min(k//2, n-(x+way['d']))
    answer += 'd'*nd
    way['u'] += nd
    k -= 2*nd
    
    answer += 'l' * way['l']
    nl = min(k//2, y-way['l']-1)
    answer += 'l'*nl
    way['r'] += nl
    k -= 2*nl
    
    answer += 'rl'*(k//2)
    answer += 'r'*way['r']
    answer += 'u'*way['u']
    
    return answer