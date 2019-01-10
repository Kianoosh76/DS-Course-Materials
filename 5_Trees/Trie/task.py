import random
class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.zero = None
        self.one = None

def insert(root, a):
    current_node = root
    b = []
    i = 64
    while i > 0:
        b.append(a%2)
        a = a//2
        i -= 1

    b.reverse()
    for bit in b:
        if bit == 0:
            if current_node.zero == None:
                current_node.zero = Node(0)
                current_node = current_node.zero
            else:
                current_node = current_node.zero
        else:
            if current_node.one == None:
                current_node.one = Node(0)
                current_node = current_node.one
            else:
                current_node = current_node.one
    current_node.cnt += 1

def find_max_xor(root, a):
    current_node = root
    b = []
    i = 64
    while i > 0:
        b.append(a%2)
        a //= 2
        i -= 1
    b.reverse()
    ans = 0
    for bit in b:
        if bit == 0:
            if current_node.one == None:
                current_node = current_node.zero
                ans = ans*2
            else:
                current_node = current_node.one
                ans = ans*2 + 1
        else:
            if current_node.zero == None:
                current_node = current_node.one
                ans = ans*2
            else:
                current_node = current_node.zero
                ans = ans*2 + 1

    return  ans


def main(n, a):
    root = Node(0)
    partial_xor = []

    insert(root, 0)

    partial_xor.append(a[0])
    insert(root, a[0])

    max_xor = a[0]
    for i in range(n - 1):
        #print(i, " " , max_xor)
        n_xor = a[i+1] ^ partial_xor[i]
        partial_xor.append(n_xor)
        insert(root, n_xor)
        max_xor = max(max_xor, find_max_xor(root, n_xor))
    return max_xor








