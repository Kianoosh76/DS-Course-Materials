from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import*

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == "__main__":

    pre = [8, 3, 5, 7, 6]
    size = len(pre)

    if (hasOnlyOneChild(pre, size) == False):
        failed("please try again 1")



    pre = [11, 10, 6, 8, 3]
    size = len(pre)
    if (hasOnlyOneChild(pre, size) == True):
        failed("please try again 2")