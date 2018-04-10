# Definition for a binary tree node.
# class TreeNode(object):
#      def __init__(self, x):
#          self.val = x
#          self.left = None
#          self.right = None
#coding=utf-8
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        if root.left or root.right:
            temp=root.left
            root.left=root.right
            root.right=temp
        self.invertTree(root.left)  #注意这里的类方法调用，前面要加self
        self.invertTree(root.right)
        return root
