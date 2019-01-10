def solve(n, k, a):
    a = sorted(a)

    # First Let's find smallest possible maximum for k days
    def is_max_ok(mx):
        tmp = 0
        for val in a:
            if val > mx:
                tmp += val - mx
        return tmp <= k

    max_lo = a[0]
    max_hi = a[-1]

    while max_hi - max_lo > 1:
        mid = int((max_hi + max_lo) / 2)
        if is_max_ok(mid):
            max_hi = mid
        else:
            max_lo = mid

    if is_max_ok(max_lo):
        ans_max = max_lo
    else:
        ans_max = max_hi

    # Now, Let's find greatest possible minimum for k days

    def is_min_ok(mn):
        tmp = 0
        for val in a:
            if val < mn:
                tmp += mn - val
        return tmp <= k

    min_lo = a[0]
    min_hi = a[-1]

    while min_hi - min_lo > 1:
        mid = int((min_hi + min_lo) / 2)
        if is_min_ok(mid):
            min_lo = mid
        else:
            min_hi = mid

    if is_min_ok(min_hi):
        ans_min = min_hi
    else:
        ans_min = min_lo

    if ans_min >= ans_max:
        if sum(a) % n != 0:  # We can only achieve it iff sum is divisible by 0
            return 1
        else:
            return 0
    else:
        return ans_max - ans_min
