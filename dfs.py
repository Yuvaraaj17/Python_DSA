class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None
    
def dfs(node):
    if node == None :
        return 0
    
    dfs(node.left)
    dfs(node.right)
    print(node.value)
    return node.value

root = Node(10)
root.left = Node(5)
root.right = Node(6)

dfs(root)