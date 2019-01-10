class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
def insert(root,data):
    if data > root.value:
        if root.right:
            insert(root.right, data)
        else:
            root.right = Node(data)
    if data < root.value:
        if root.left:
            insert(root.left, data)
        else:
            root.left = Node(data)

#inorder is an array which we want to store the inorder traversal in it.
def inordertraversal(root, inorder):
    if root:
        # First recur on left child
        inordertraversal(root.left, inorder)

        # then print the data of node
        inorder.append(root.value)

        # now recur on right child
        inordertraversal(root.right, inorder)


mainroot = Node(5)
insert(mainroot,1)
insert(mainroot,3)
insert(mainroot,6)
insert(mainroot,8)
insert(mainroot,7)
insert(mainroot, 4)

mainroot2 = Node(10)
insert(mainroot2, 11)
insert(mainroot2, 4)
insert(mainroot2, 6)
insert(mainroot2, 7)
insert(mainroot2, 14)
insert(mainroot2, 9)


inorder1 = []
inorder2 = []
inordertraversal(mainroot, inorder1)
inordertraversal(mainroot2, inorder2)

#intersection in O(m + n)
# m is size of arr1, n is size of array2
finalarray = []
def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            # common element.
            finalarray.append(arr2[j])
            j += 1
            i += 1



# m = len(inorder1)
# n = len(inorder2)
# printIntersection(inorder1, inorder2, m, n)
# print(finalarray)

