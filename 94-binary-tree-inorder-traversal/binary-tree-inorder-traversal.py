# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''res=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res'''

        '''more easiest approach 


        res=[]
        st=[]
        curr=root
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            res.append(curr.val)
            curr=curr.right
        return res '''

        res=[]
        curr=root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr=curr.right
            else:
                pred=curr.left
                while pred.right and pred.right!=curr:
                    pred=pred.right
                if not pred.right:
                    pred.right=curr
                    curr=curr.left
                else:
                    pred.right=None
                    res.append(curr.val)
                    curr=curr.right
        return res
