def func(n , m , arr):
    arr.sort()
    c = 0
    d = 0
    s = sum(arr)
    for i in range(n):
        if (arr[i] > d):
            d += 1
    #c += (arr[n - 1] - d)
    return s - arr[n - 1] - n + d
