from test_helper import *
from task import *

if __name__ == '__main__':
    tests = [
        ([-10, -6, -2, 0, 4, 6, 10, 17, 30], 3, 3),
        ([10, 11, 12], 9, -1),
        ([1, 1, 1, 1, 1, 1], 2, 5),
        ([-1, 0, 1, 2, 3], 2, 2)
    ]
    for test in tests:
        test_function(test[-1], lower_bound, test[0], test[1])
