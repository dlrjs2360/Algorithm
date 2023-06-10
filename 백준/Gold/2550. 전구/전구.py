import bisect
n = int(input())

# d는 첫 번째 배열의 값의 순서를 유지하고 순서대로 두 번째 배열의 값을 저장하는 딕셔너리
d = {}

# 값이 아닌 순서를 기준으로 딕셔너리에 키만 저장
for i in map(int, input().split()):
    d[i] = 0

# 두번쨰 배열의 값을 첫번째 순서에 맞춰서 값으로 저장
for k, i in enumerate(map(int, input().split())):
    d[i] = k

# d.items(), values()를 사용하면 저장된 순서를 유지하며 탐색
res,idx = [],[]
for i in d.values():
    s = bisect.bisect_left(res, i)
    if s != len(res): res[s] = i
    else: res += [i]
    idx.append(s)

# 역 추적을 통한 정답 도출
print(l := len(res))
answer = []
for i in range(n - 1, -1, -1):
    if idx[i] == l - 1: answer += [list(d)[i]];l -= 1
print(*answer)