def func(n, arr):
    a = [0] * (n + 1)
    for i in arr: a[i] = a[i - 1] + 1
    return n - max(a)
