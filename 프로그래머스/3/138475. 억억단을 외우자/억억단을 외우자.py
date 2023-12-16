def solution(e, starts):
    dp_count = [0] * (e + 1)
    for div in range(2, e + 1):
        for jump in range(0, e + 1, div):
            dp_count[jump] += 2

    for root in range(1, int(e ** 0.5) + 1):
        dp_count[root ** 2] += 1

    dp_div = [0] * (e + 1)
    max_count = 0
    for idx in range(e, 0, -1):
        if max_count <= dp_count[idx]:
            max_count = dp_count[idx]
            dp_div[idx] = idx
        else:
            dp_div[idx] = dp_div[idx + 1]

    return [dp_div[start] for start in starts]