def func(n, k):
    global t
    if k % 2 == 0:
        return -1
    t = k
    t -= 1
    a = [i + 1 for i in range(n)]

    def sl(l, r):
        global t
        if r - l < 2 or t == 0:
            return
        t -= 2
        m = (l + r) // 2
        a[m], a[m - 1] = a[m - 1], a[m]
        sl(l, m)
        sl(m, r)

    sl(0, n)
    if t != 0:
        return -1
    return a
