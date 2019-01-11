class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        return Node(preorder[0])
    root = Node(preorder[0])
    div = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:(div + 1)], inorder[0:div])
    root.right = buildTree(preorder[(div + 1):], inorder[(div + 1):])
    return root


def postorder_traversal(root, list):
    if root:
        if root.left:
            postorder_traversal(root.left, list)
        if root.right:
            postorder_traversal(root.right, list)
        list.append(root.value)
        return list


def check(preorder, inorder, postorder):
    root = buildTree(preorder, inorder)
    root_postorder = postorder_traversal(root, [])
    if postorder == root_postorder:
        return True
    return False
