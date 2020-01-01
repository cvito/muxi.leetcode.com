package source150

import "math"

/**
地址：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
题目描述：
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

Example:
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

 */

 /**
 思路：
 给定i节点，返回i左右子节点的最大深度,再加上自身，最终便是最大深度
  */

  /**
  用时：4ms
  内存：4.4MB
   */
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftMax := maxDepth(root.Left)
	rightMax := maxDepth(root.Right)
	max := int(math.Max(float64(leftMax), float64(rightMax))) + 1
	return max
}