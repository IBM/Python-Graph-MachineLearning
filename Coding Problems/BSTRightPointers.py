from collections import deque
class Solution:
    def connect(self, root) :
        q = deque()
        if root:
            q.append(root)

        while q:
            size = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

"""
Steps:-
add root to queue
if its last node in q then add to q

"""