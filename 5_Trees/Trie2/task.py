
class Node:
    def __init__(self):
        self.cnt = 0
        self.next = [None]*10

root = Node()
digit = [None]*26

def trieInsert(string):
    current = root
    for c in string:
        tmp_char = ord(c) - ord('a')
        tmp_digit = digit[tmp_char]
        if current.next[tmp_digit] == None:
            current.next[tmp_digit] = Node()
            current = current.next[tmp_digit]
        else:
            current = current.next[tmp_digit]
    current.cnt = current.cnt + 1

def main(dictionary, numpad, keyset):
    for i in range(len(numpad)):
        chars = numpad[i]
        for char in chars:
            tmp_char = ord(char) - ord('a')
            digit[tmp_char] = i
    for word in dictionary:
        trieInsert(word)
    dp = [0]*(len(keyset)+1)
    for i in range(len(keyset)):
        j = len(keyset) - i - 1
        current = root
        k = j
        dp[j] = 999999
        while k < len(keyset) and current is not None:
            current = current.next[keyset[k]]
            if current is None:
                break
            if current.cnt > 0 and dp[k+1] != -1:
                dp[j] = min(dp[j], 1 + dp[k+1])
            k = k + 1
        if dp[j] == 999999:
            dp[j] = -1
    return dp[0]

dic = ["am","axe","exam"
    ,"boy","colour","dam","dot","donkey",
    "fox","new","prim","prime","primeval","pry",
       "the","this","theory","van"]
numpad = [['a','b','c'],['d','e','f'],['g','h'],['i','j','y'],
          ['l','m','n'],['o','p','q'],['r','s'],['t','u'],
          ['v','w','x'],['k','z']]
keyset = [7,2,1,5,6,3,4,1,8,0,4]


