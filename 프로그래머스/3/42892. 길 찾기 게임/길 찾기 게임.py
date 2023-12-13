import sys; sys.setrecursionlimit(10001)
from collections import namedtuple

Node = namedtuple('Node', ['x', 'y', 'id'])

def solution(nodeinfo):
    # 특정 노드를 기준으로 partition을 잘 하면 될 것 같습니다.
    # 우선 nodeinfo를 (x, y, id)의 배열로 바꿉니다.
    nodeinfo = [Node(x, y, id) for id, (x, y) in enumerate(nodeinfo, 1)]
    
    def preorder(arr):
        if len(arr) < 1:
            return [node.id for node in arr]
        
        # 전위순회부터 해보면, 배열에서 y좌표가 가장 큰 값을 pivot으로 두고
        # 먼저 pivot의 id를 리턴 배열에 넣은 뒤
        # x좌표의 대소를 기준으로 나뉜 두 배열에서
        # 전위순회를 재귀적으로 돌려주면 됩니다.
        pivot = max(arr, key=lambda node: node.y)
        
        res = [pivot.id]
        res += preorder([node for node in arr if node.x < pivot.x])
        res += preorder([node for node in arr if node.x > pivot.x])
        
        return res
    
    def postorder(arr):
        if len(arr) < 1:
            return [node.id for node in arr]
        
        pivot = max(arr, key=lambda node: node.y)
        
        res = []
        res += postorder([node for node in arr if node.x < pivot.x])
        res += postorder([node for node in arr if node.x > pivot.x])
        res.append(pivot.id)
        
        return res
        
    return preorder(nodeinfo), postorder(nodeinfo)