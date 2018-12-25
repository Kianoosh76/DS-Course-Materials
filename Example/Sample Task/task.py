def lower_bound(A, x):
    if A[0] >= x:
        return -1
    ans = 0
    end = len(A)
    while end > ans + 1:
        mid = ans + end >> 1

        if A[mid] >= x:
            end = mid
        else:
            ans = mid
    return ans
