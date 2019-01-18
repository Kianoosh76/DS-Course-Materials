import task
import random
import string
from time_limit import put_limit
from test_helper import failed


def sol_setup(dictionary):
    global words
    words = set(dictionary)


def sol_suggestions(word):
    result = set()
    is_legit = word in words
    if not is_legit:
        # add char
        for i in range(len(word) + 1):
            for char in string.ascii_lowercase:
                possible = word[:i] + char + word[i:]
                if possible in words:
                    result.add(possible)
        # remove char
        for i in range(len(word)):
            possible = word[:i] + word[i + 1:]
            if possible in words:
                result.add(possible)
        # change char
        for i in range(len(word)):
            for char in string.ascii_lowercase:
                possible = word[:i] + char + word[i + 1:]
                if possible in words:
                    result.add(possible)
    return is_legit, result


if __name__ == '__main__':
    put_limit(10)
    try:
        dic = {''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 50))) for _ in range(10000)}
        test = {''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10))) for _ in range(10000)}
        task.setup(dic)
        sol_setup(dic)
        for word in test:
            if task.suggestions(word) != sol_suggestions(word):
                failed("Wrong Answer!")
    except Exception:
        failed("Timed Out!")
