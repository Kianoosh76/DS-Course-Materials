import random

def find_kth(a, b, k):
    arr = a + b
    size = len(arr)
    left = 0
    right = size - 1
    while True:
        pivot = random.randint(left, right)
        new_pivot = partition(arr, left, right, pivot)
        pivot_distance = new_pivot - left
        if pivot_distance == k:
            return arr[new_pivot]
        elif k < pivot_distance:
            right = new_pivot - 1
        else:
            k -= pivot_distance + 1
            left = new_pivot + 1


def partition(arr, left, right, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    new_pivot = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[new_pivot], arr[i] = arr[i], arr[new_pivot]
            new_pivot += 1
    arr[right], arr[new_pivot] = arr[new_pivot], arr[right]
    return new_pivot
