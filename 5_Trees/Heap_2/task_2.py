def sum_between_two_Kth(arr, n, k1, k2):

    # Sort the given array
    arr.sort()

    result = 0
    for i in range(k1, k2-1):
        result += arr[i]
    return result
