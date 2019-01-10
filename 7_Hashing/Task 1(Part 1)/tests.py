import random
from task import answer
from test_helper import failed


def solution(arr, k):
    sums = {}
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if k - arr[i] - arr[j] in sums:
                return (arr[i], arr[j]) + sums[k - arr[i] - arr[j]]
            sums[arr[i] + arr[j]] = (arr[i], arr[j])
    return None


def generate_test():
    return [random.randint(0, 10 ** 12) for i in range(random.randint(10, 1000))]


if __name__ == '__main__':
    for i in range(5):
        arr = generate_test()
        values = random.sample(arr, 4)
        result = answer(arr, sum(values))
        if result is None or len(set(result)) < 4 or sum(result) != sum(values):
            failed()
    for i in range(3):
        arr = generate_test()
        value = random.randint(0, 10 ** 12)
        result = answer(arr, value)
        ans = solution(arr, value)
        if ans is None != result is None:
            failed()
        elif ans is not None:
            if len(set(result)) < 4 or sum(result) != sum(ans):
                failed()
