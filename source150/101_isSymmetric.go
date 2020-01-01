package source150

/**
地址：https://leetcode-cn.com/problems/symmetric-tree/
题目描述：
给定一个二叉树，检查它是否是镜像对称的。

Example:
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 */

 /**
 思路：
 A,B两棵树的根节点一定是相等的，然后A的左子树等于B的右子树，和A的右子树等于B的左子树。
  */

  /**
  用时：0ms
  内存：2.9MB
   */
func isSymmetric(root *TreeNode) bool {
	return isMirror(root, root)
}

func isMirror(t1 *TreeNode, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	}
	if t1 == nil || t2 == nil {
		return false
	}
	return t1.Val == t2.Val && isMirror(t1.Left, t2.Right) && isMirror(t1.Right, t2.Left)
}

