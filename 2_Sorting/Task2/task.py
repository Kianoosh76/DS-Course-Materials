import bisect


def func(n, array):
    all = []
    for i in range(n):
        pos = bisect.bisect(all, array[i])
        if pos >= len(all):
            all.append(array[i])
        else:
            all[pos] = array[i]
    return len(all)
