class Node:
    def __init__(self, data, node_left, node_right):
        self.data = data
        self.node_left = node_left
        self.node_right = node_right
def pre_order(node):

n = int(input())
tree ={}
for _ in range(n):
    data, node_left, node_right = input().split()
    tree[data] = Node(data, node_left, node_right)
