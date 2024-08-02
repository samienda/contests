n = int(input())
array = list(map(int, input().split()))

prefix = [0] + array[:]
array.append(0)
suffix = array[:]

for i in range(1, n):
    prefix[i] ^= prefix[i - 1]

for i in range(n - 1, 0, -1):
    suffix[i] ^= suffix[i + 1]

# print(prefix)
# print(suffix)

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None, None]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            curr = int(ch)
            if not node.children[curr]:
                newnode = TrieNode()
                node.children[curr] = newnode
            node = node.children[curr]

        node.is_end = True


def change(num):
    bit = ['0' for _ in range(40)]

    for i, b in enumerate(reversed(bin(num)[2:])):
        bit[i] = b

    return bit[::-1]

trie = Trie()
def find(num):
    # print(num)
    bits = trie.root
    ans = []
    for b in num:
        # print(b, bits.children)
        if b == '1' and bits.children[0]:
            bits = bits.children[0]
            ans.append(b)
        elif b == '0' and bits.children[1]:
            bits = bits.children[1]
            ans.append('1')
        else:
            bits = bits.children[int(b)]
            ans.append('0')
        # print(ans)

    return int("".join(ans), 2)




maximum = 0
# trie.insert(change(0))
for i in range(n + 1):
    trie.insert(change(prefix[i]))
    maximum = max(
        maximum,
        find(change(suffix[i]))
    )
    
print(maximum)