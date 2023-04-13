def solution(n, costs):
    answer = 0
    parent = [x for x in range(n)]
    
    def ancestor(node):
        if parent[node] != node:
            parent[node] = ancestor(parent[node])
        return parent[node]

    for a,b,c in sorted(costs,key=lambda x:x[2]):
        if (pa:=ancestor(a)) != (pb:=ancestor(b)):
            if pa > pb:
                parent[pa] = pb
            else:
                parent[pb] = pa
            answer += c
            
    return answer