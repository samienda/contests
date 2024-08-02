

from collections import defaultdict


n = int(input())
# n = 1000000
array = []


length = 0
for _ in range(n):
    x = input()
    array.append(x)
    length += len(x)


class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for w in word:

            index = ord(w) - ord('a')
            if not root.children[index]:
                newnode = TrieNode()
                root.children[index] = [newnode, 0]

            root.children[index][-1] += 1
            root = root.children[index][0]

    def find(self, word):

        count = 0
        root = self.root
        for w in word:

            index = ord(w) - ord('a')
            if not root.children[index]:
                return count

            count += root.children[index][-1]
            root = root.children[index][0]

        return count


trie = Trie()
# print(array)
for word in array:
    trie.insert(word)


total = 0
for word in array:
    total += (2 * trie.find(word[::-1]) - (n * len(word) + length))
print(abs(total))

# expected =
