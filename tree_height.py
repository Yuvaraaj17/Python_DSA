class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None

def height(root):

    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height :
        return left_height+1

    else:
        return right_height+1

root = Node(1)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(4)
root.left.right = Node(5)

height(root)