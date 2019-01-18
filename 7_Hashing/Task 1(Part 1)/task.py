import string


def setup(dictionary):
    global words
    words = set(dictionary)


def suggestions(word):
    result = set()
    is_legit = word in words
    if not is_legit:
        # add char
        for i in range(len(word) + 1):
            for char in string.ascii_lowercase:
                possible = word[:i] + char + word[i:]
                if possible in words:
                    result.add(possible)
        #remove char
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
