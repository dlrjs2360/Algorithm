from collections import deque

def solution(S):
    answer = 1000
    queue = deque([(1, 0, 0)])
    visit = [[False] * (2 * S + 1) for _ in range(2 * S + 1)]

    while queue:
        emoticon, clip, time = queue.popleft()

        if visit[emoticon][clip]: continue

        if time >= answer: continue
        if emoticon == S: answer = min(answer, time); continue
        if emoticon > S: answer = min(answer, time + emoticon - S); continue

        visit[emoticon][clip] = True

        if clip > 0:
            queue.append((emoticon + clip, clip, time + 1))
        if emoticon > 0:
            queue.append((emoticon - 1, clip, time + 1))
        if emoticon > clip:
            queue.append((emoticon, emoticon, time + 1))
    return answer

print(solution(int(input())))