# from test_helper import run_common_tests, failed, passed, get_answer_placeholders
#
#
# def test_answer_placeholders():
#     placeholders = get_answer_placeholders()
#     placeholder = placeholders[0]
#     if placeholder == "":       # TODO: your condition here
#         passed()
#     else:
#         failed()
#
#
# if __name__ == '__main__':
#     run_common_tests()
#     # test_answer_placeholders()       # TODO: uncomment test call
#
#
from test_helper import *
from task import *

if __name__ == '__main__':

    tests = [
        ([1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [4, 5, 2, 3, 1], True),
        ([25,15,10,4,12,22,18,24,50,35,31,44,70,66,90], [4,10,12,15,18,22,24,25,31,35,44,50,66,70,90], [4,12,10,18,24,22,15,31,44,35,66,90,70,50,25], True),
        ([2,7,3,6,8,11,5,9,4], [3,7,8,6,11,2,5,4,9], [3,8,11,7,6,4,9,5,2], False),
        ([8,5,9,7,1,12,2,4,11,3], [9,5,1,7,2,12,8,4,3,11], [9,1,2,12,7,5,11,3,4,8], False)
    ]
    for test in tests:
        test_function(test[-1], check, test[0], test[1], test[2])
