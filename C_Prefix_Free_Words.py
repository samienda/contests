
n = int(input())
array = list(map(int, input().split()))


class TrieNode:
    def __init__(self):
        self.children = [None, None]
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.seen = set()
        
        
    def insert(self, num):
        root = self.root
        def backtrack(node, num, path):
            
            if num == 0:
                self.seen.add(path)
                return True
            
            found = False
            if path + '1' not in self.seen:
                if not node.children[1]:
                    node.children[1] = TrieNode()
                found = found or backtrack(node.children[1], num - 1, path + '1')
            
            if path + '0' not in self.seen:
                if not node.children[0]:
                    node.children[0] = TrieNode()
                found = found or backtrack(node.children[0], num - 1, path + '0')
            
            return found
        
        return backtrack(root, num, "")
    

trie = Trie()
for num in array:
    if not trie.insert(num):
        print("NO")
        break
else:
    print("YES")
    for c in sorted(trie.seen, key=lambda item:len(item)):
        print(c)