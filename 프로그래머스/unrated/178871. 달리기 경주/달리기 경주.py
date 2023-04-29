from collections import defaultdict,deque
def solution(players, callings):
    idx = defaultdict(int)
    for i in range(L:=len(players)):
        idx[players[i]] = i
    for c in callings:
        origin,moved = idx[c], idx[c]-1
        idx[players[origin]] -= 1
        idx[players[moved]] += 1
        players[origin], players[moved] = players[moved], players[origin]
    return players