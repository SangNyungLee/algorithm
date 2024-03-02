import sys

sys.setrecursionlimit(10**9)
nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]


class Node:
    def __init__(self, nodeinfo):
        self.x = nodeinfo[0][0]
        self.data = nodeinfo[1]
        self.left_node = None
        self.right_node = None


def insert(node, info):
    if node == None:
        return Node(info)
    if info[0][0] < node.x:
        node.left_node = insert(node.left_node, info)
    else:
        node.right_node = insert(node.right_node, info)
    return node


def maketree(nodeinfo):
    nodes = []
    for i, node in enumerate(nodeinfo, 1):
        nodes.append((node, i))

    nodes.sort(key=lambda x: x[0][0])
    nodes.sort(key=lambda x: x[0][1], reverse=True)
    root = None
    for node in nodes:
        root = insert(root, node)
    return root

def pre_order(node):
    if node.left_node:
        

def preorder(root):
    def _preorder(node):
        if node:
            res.append(node.data)
            _preorder(node.left_node)
            _preorder(node.right_node)

    res = []
    _preorder(root)
    return res


# 후위 순회 함수
def postorder(root):
    def _postorder(node):
        if node:
            _postorder(node.left_node)
            _postorder(node.right_node)
            res.append(node.data)

    res = []
    _postorder(root)
    return res


def solution(nodeinfo):
    answer = []
    root = maketree(nodeinfo)
    answer.append(preorder(root))
    answer.append(postorder(root))
    return answer


print(solution(nodeinfo))
