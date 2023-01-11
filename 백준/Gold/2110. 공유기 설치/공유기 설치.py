import sys
input = sys.stdin.readline

n, c = map(int,input().split())
house = [int(input()) for _ in range(n)]
house.sort()

answer = 0
left, right = 1, house[-1]-house[0]
while left <= right:
    mid = (left + right) // 2

    count = 1
    current = house[0]
    for i in range(1,len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]

    #print("left: ", str(left), "right: ", str(right), "mid: ", str(mid), "count: ",str(count))
    if count < c:
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1

print(answer)