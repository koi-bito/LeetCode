class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            next_queue = []
            
            # nodes at the current level
            for node in queue:
                level_sum += node.val
                
                # add children
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            # average current
            level_average = level_sum / level_size
            result.append(level_average)
            
            # next level
            queue = next_queue
        
        return result
