from tree_height import height
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None

def bfs_recursive(root):
    h = height(root)
    for i in range(1, h+1):
        current_level(root, i)

def current_level(node, level):
    if node is None:
        return
    if level == 1:
        print(node.value,end=" ")
        return node.value
    elif level > 1 :
        current_level(node.left, level-1)
        current_level(node.right, level-1)
root = Node(1)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(4)
root.left.right = Node(5)

bfs_recursive(root)