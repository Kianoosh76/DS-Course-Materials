class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.value == root2.value:
            return (mirror(root1.left, root2.right) and
                    mirror(root1.right, root2.left))
    return False


def isSymmetric(root):
    return mirror(root, root)




