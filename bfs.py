class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None

def bfs(root):

    if root is None:
        return

    queue = []
    queue.append(root)

    while (len(queue) > 0):

        print(queue[0].value,end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(4)
root.left.right = Node(5)

bfs(root)
