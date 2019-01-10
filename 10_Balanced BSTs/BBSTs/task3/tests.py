from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from random import shuffle
from random import randint
from task import func as func
from task_copy import func as func_judge

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()

def test_generator(n):
    li = [i for i in range(n)]
    shuffle(li)
    return li
if __name__ == '__main__':
    test_nums = [10, 10, 100, 1000]
    for test_num in test_nums:
        li = test_generator(test_num)
        assert func(li) == func_judge(li)
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call


