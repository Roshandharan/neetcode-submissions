# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indicies = {val:idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l,r):
            if l>r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx +=1
            root = TreeNode(root_val)

            mid = indicies[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        
        return dfs(0, len(preorder)-1)
# TC : O(n)
# SC : O(n)
# Preorder starts from the root, we create a hashmap of inorder and map values(val:idx), the goal is to create lookup of O(1). the we contrsut root and keep mapping left and right but finding it in the in order list 
        