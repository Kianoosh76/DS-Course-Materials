class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


prev = None

def isbst(root):
    global prev
    prev = None
    return isbst_mainfunc(root)

def isbst_mainfunc(root):
    #using inorder travers
    global prev

    if root is None:
        return True

    if isbst_mainfunc(root.left) is False:
        return False

    if prev is not None and prev.value > root.value:
        return False

    prev = root
    return isbst_mainfunc(root.right)

