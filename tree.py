class Node:
    def __init__(self, value: int , right=None, left=None) -> None:
        self.value = value
        self.right = right
        self.left = left

def display_tree(tree: Node):
    left = tree.left
    right = tree.right
    # import ipdb;ipdb.set_trace()
    if left:
        if left.right:
            display_tree(left.right)    
        if left.left:
            display_tree(left.left)
        print(left.value)

    if right:
        if right.right:
            display_tree(right.right)
        if right.left:
            display_tree(right.left)
        print(right.value)
    print(tree.value)
    return tree.value

if __name__ == '__main__':
    n1 = Node(value=0)
    n2 = Node(value=1)
    n3 = Node(value=2,right=n1, left=n1)
    n4 = Node(value=3, right=n3)
    display_tree(n4)

