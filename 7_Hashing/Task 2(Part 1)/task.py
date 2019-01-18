from hash_table import HashTable


def answer(arr, k):
    table = HashTable(1000003)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pair = table.get(k - arr[i] - arr[j])
            if pair is not None:
                if i not in pair and j not in pair:
                    return (arr[i], arr[j]) + (arr[pair[0]], arr[pair[1]])
            table.insert(arr[i] + arr[j], (i, j))
    return None
