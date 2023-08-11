import sys
input = sys.stdin.readline

std = {"Y" : 0, "S" : 1}
check = {}
seat = []
count = 0

for _ in range(5):
    s = list(map(lambda x: std[x], input().rstrip()))
    seat.append(s)

def placement(arr, bit, length, cnt_y):
    global count
    if cnt_y >= 4:
        return
    if length == 7:
        count += 1
        return
    for x,y in arr:
        for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= i < 5 and 0 <= j < 5:
                sub_bit = 1 << (i * 5 + j)
                new_bit = bit + sub_bit
                if not bit & sub_bit and check.get(new_bit) == None:
                    check[new_bit] = 1
                    placement(arr + [[i,j]], new_bit, length+1, cnt_y+1 -seat[i][j])

for i in range(5):
    for j in range(5):
        if seat[i][j] == 1:
            start_bit = 1 << (i * 5 + j)
            placement([[i,j]], start_bit, 1, 0)
print(count)