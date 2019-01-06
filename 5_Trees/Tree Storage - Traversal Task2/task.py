class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


minimum = 0
maximum = 0


def find_left_right(node, distance):
    global minimum, maximum
    if node is None:
        return
    if distance < minimum:
        minimum = distance
    elif distance > maximum:
        maximum = distance
    find_left_right(node.left, distance - 1)
    find_left_right(node.right, distance + 1)


def vertical(node, column, distance, list):
    if node is None:
        return

    if distance == column:
        list[-1].append(node.value)

    vertical(node.left, column, distance - 1, list)
    vertical(node.right, column, distance + 1, list)


def verticalOrder(root):
    list = []
    global minimum, maximum
    find_left_right(root, 0)
    for column in range(minimum, maximum + 1):
        list.append([])
        vertical(root, column, 0, list)
    return list




