from collections import defaultdict, deque


# def printnode(head):
#     curr = head
#     while curr:
#         print(f'{[curr.prev.val if curr.prev else None, curr.val,
#               curr.next.val if curr.next else None]} + ->')
#         curr = curr.next


class Node:
    def __init__(self, val, nex=None, pre=None) -> None:
        self.val = val
        self.next = nex
        self.prev = pre


dic = defaultdict(deque)

last = None
first = None

q = int(input())

queries = []
for _ in range(q):
    queries.append(list(map(str, input().split())))

# print(queries)


for querie in queries:
    # print(querie, last.val if last else None)
    if querie[0] == 'insert':
        x, y = querie[1:]
        node = Node(x)
        if not dic[y]:
            dic[x].append(node)
            if last:
                last.next = node
                node.prev = last
            if not first:
                first = node
                
            last = node
        else:
            target = dic[y][0]
            node.next = target.next
            node.prev = target
            target.next = node
            if node.next:
                node.next.prev = node

            dic[x].append(node)

            if last == target:
                last.next = node
                node.prev = last
                last = node

    else:

        x = querie[-1]

        
        if dic[x]:
     
            node = dic[x].popleft()
     
            prev = node.prev
            nex = node.next

            if prev:
                prev.next = nex

            if nex:
                nex.prev = prev

            if first == node:
                first = nex

            if last == node:
                last = prev

    # printnode(dic['3'][0])

    # print("end of end")

answer = []
head = first
while head:
    answer.append(head.val)
    head = head.next

print(*answer)
