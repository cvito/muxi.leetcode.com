package source150

/**
地址：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
题目描述：
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

Example:
例如，给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

 */

 /**
 思路：通过递归，遍历所有节点，时间复杂度O（N）
  */

  /**
  用时：0ms
  内存：3MB
   */
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}
	return progress(root, 0, make([][]int, 0))
}

func progress(root *TreeNode, level int, res [][]int) [][]int {
	if len(res) == level {
		res = append(res, []int{})
	}
	res[level] = append(res[level], root.Val)
	if root.Left != nil {
		res = progress(root.Left, level + 1, res)
	}
	if root.Right != nil {
		return progress(root.Right, level + 1, res)
	}
	return res
}

