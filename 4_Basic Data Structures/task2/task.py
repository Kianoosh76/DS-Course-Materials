def first_negatives(A, k):
    queue = []
    ans = []
    for i in range(len(A)):
        if A[i] < 0:
            queue.append(i)
        if i >= k-1:
            if len(queue) and i - queue[0] >= k:
                queue.pop(0)
            ans.append(A[queue[0]] if len(queue) else 0)
    return ans
