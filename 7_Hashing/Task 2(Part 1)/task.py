def smallest_period(str):
    p, q = 27, 10**9 + 7
    hash_list = hash(str, q, p)
    offset = p
    for T in range(1, len(str)):
        if is_period(hash_list, T, offset, q):
            return T
        offset = (offset * p) % q
    return 0


def is_period(hash_list, T, offset, q):
    return (hash_list[len(hash_list) - T - 1] * offset) % q == (hash_list[len(hash_list) - 1] - hash_list[T - 1]) % q


def hash(str, q, p):
    hash_list = [ord(str[0]) - ord('a') + 1]
    s = 1
    for i in range(1, len(str)):
        s = (s * p) % q
        hash_list.append((hash_list[i - 1] + (ord(str[i]) - ord('a') + 1) * s) % q)
    return hash_list
