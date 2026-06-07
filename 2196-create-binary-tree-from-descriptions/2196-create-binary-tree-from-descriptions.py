# Definition for a binary tree node (provided by LeetCode)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes: dict[int, TreeNode] = {}
        children: set[int] = set()

        for parent_val, child_val, is_left in descriptions:
            # ensure both nodes exist
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

            # attach according to the flag
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

            # record that this value is a child of somebody
            children.add(child_val)

        # root = the single value that never appears as a child
        root_val = (set(nodes.keys()) - children).pop()
        return nodes[root_val]
