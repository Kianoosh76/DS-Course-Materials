def linked_list_swap(node1, node2):
    if node1.prev == node2:
        node1, node2 = node2, node1
    if node1.prev:
        node1.prev.next = node2
    if node1.next and node1.next != node2:
        node1.next.prev = node2
    if node2.next:
        node2.next.prev = node1
    if node2.prev and node2.prev != node1:
        node2.prev.next = node1
    node1.next, node2.next = node2.next, (node1.next if node1.next != node2 else node1)
    node1.prev, node2.prev = (node2.prev if node2.prev != node1 else node2), node1.prev
