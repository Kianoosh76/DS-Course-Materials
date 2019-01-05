def func(n , b , arr):
    odd = 0
    even = 0
    cuts = []
    for i in range(n - 1):
        if (arr[i] % 2 != 0):
            odd = odd + 1
        else:
            even = even + 1
        if (odd == even):
            cuts.append(abs(arr[i + 1] - arr[i]))
    cuts.sort()
    ans = 0
    sum = 0
    for i in cuts:
        if (sum + i <= b):
            sum = sum + i
            ans = ans + 1
    return ans
