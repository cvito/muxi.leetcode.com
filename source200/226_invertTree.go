package source200

/**
地址：https://leetcode-cn.com/problems/invert-binary-tree/
题目描述：
翻转一棵二叉树。

Example:
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 */

 /**
 思路：
 交换i节点的每一层的左右子节点，从下往上，最后交换整个左右子树
  */

  /**
  用时：0ms
  内存：2.1MB
   */
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	invertTree(root.Left)
	invertTree(root.Right)
	tmp := root.Left
	root.Left = root.Right
	root.Right = tmp
	return root
}