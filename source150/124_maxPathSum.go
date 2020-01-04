package source150

import (
	"math"
)

/**
地址：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
题目描述：
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

Example:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
 */

  /**
  用时：24ms
  内存：6.7MB
   */
func maxPathSum(root *TreeNode) int {
	max := math.MinInt64
	maxProgress(root, &max)
	return max
}

func maxProgress(root *TreeNode, max *int) int {
	if root == nil {
		return 0
	}
	leftMax := int(math.Max(float64(maxProgress(root.Left, max)), 0))
	rightMax := int(math.Max(float64(maxProgress(root.Right, max)), 0))
	rootMax := root.Val + leftMax + rightMax
	*max = int(math.Max(float64(*max), float64(rootMax)))
	return root.Val + int(math.Max(float64(leftMax), float64(rightMax)))
}


