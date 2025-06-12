'''计算给定二叉树的所有左叶子之和。'''

'''那么我来给出左叶子的明确定义：
节点A的左孩子不为空，且左孩子的左右孩子都为空（说明是叶子节点），
那么A节点的左孩子为左叶子节点'''

# 关键词
# 1.本质上还是一个遍历问题，主要在于确定“左叶子”的筛选判断条件
# 2.涉及节点的数值运算，采用后序遍历：左、右、中

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        # 递归终止条件
        # 1.空节点，返回值0
        if root is None:
            return 0
        # 2.叶子节点，返回值0
        if root.left is None and root.right is None:
            return 0
        
        # 单层递归逻辑
        # 1.左子树
        leftValue = self.sumOfLeftLeaves(root.left)  # 左
        # 2.左子树为左叶子节点，返回节点数值
        if root.left and not root.left.left and not root.left.right:  # 左子树是左叶子的情况
            leftValue = root.left.val

        # 3.右子树    
        rightValue = self.sumOfLeftLeaves(root.right)  # 右

        # 4.左右相加
        sum_val = leftValue + rightValue  # 中
        return sum_val