n, b, w = map(int,input().split())
stone = list(input())

left, right = 0,0
white, black = int(stone[right] == "W"), int(stone[right] == "B")
answer = int(white >= w and black <= b)
while left <= right < n:
    #print(f"left: {left}, right: {right}, white: {white}, black: {black}, answer: {answer}")
    if white < w:
        right += 1
        if right >= n: break
        white += int(stone[right] == "W")
        black += int(stone[right] == "B")
    elif black > b:
        white -= int(stone[left] == "W")
        black -= int(stone[left] == "B")
        left += 1
    else:
        answer = max(right - left + 1, answer)
        right += 1
        if right >= n: break
        white += int(stone[right] == "W")
        black += int(stone[right] == "B")

print(answer)