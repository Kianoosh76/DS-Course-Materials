import random
import timeit


def qSortRandomPivot(arr, fst, lst):
    #start = timeit.default_timer()
    if fst >= lst: return

    i, j = fst, lst
    pivot = arr[random.randint(fst, lst)]

    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    qSortRandomPivot(arr, fst, j)
    qSortRandomPivot(arr, i, lst)
    #end = timeit.default_timer()
    #print('qSort Random Pivot Time: ' , end - start)
    return arr

