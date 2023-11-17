N = int(input())
woman = list(map(int,input().split()))
man = list(map(int,input().split()))

uwm, dwm = [],[]
for x in woman:
    if x >= 0: uwm.append(x); continue
    dwm.append(x)

um, dm = [],[]
for x in man:
    if x >= 0: um.append(x); continue
    dm.append(x)

'''
나보다 큰 사람을 원하는 여자 중 가장 작은 사람부터 나보다 작은 사람을 원하는 가장 작은 남자를 선택
'''
answer = 0
dm.sort()
for w in sorted(uwm):
    while dm:
        m = dm.pop()
        if abs(m) <= abs(w): continue
        answer += 1
        break

'''
나보다 작은 사람을 원하는 여자 중 가장 큰 사람부터 나보다 큰 사람을 워하는 가장 큰 남자를 선택
'''
um.sort()
for w in sorted(dwm):
    while um:
        m = um.pop()
        if abs(m) >= abs(w): continue
        answer += 1
        break

print(answer)