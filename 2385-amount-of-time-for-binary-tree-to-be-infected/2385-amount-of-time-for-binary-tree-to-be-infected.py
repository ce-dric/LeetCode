# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = dict()

        infected = set()
        def dfs(node: TreeNode, parent: TreeNode) -> None:
            global start_node
            if node == None:
                return
            if node.val == start:
                start_node = node
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        time = 0
        buf = [start_node]
        while len(buf) > 0:
            time += 1
            buf2 = set()
            for node in buf:
                if node not in infected:
                    infected.add(node)
                    if node.left != None and node.left not in infected:
                        buf2.add(node.left)
                    if node.right != None and node.right not in infected:
                        buf2.add(node.right)
                    if parents[node] != None and parents[node] not in infected:
                        buf2.add(parents[node])
            buf = list(buf2)
            print(time,len(buf))

        return time-1