package source150

/**
地址：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
题目描述：
给定一个二叉树，原地将它展开为链表。

Example:
例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
 */

 /**
 思路：
 1. 找到i节点左子树的最大数值节点，即找到左子树的最右节点，记为preNode
 2. 将i节点的右子树放到preNode右子树
 3. 将i节点的左子树移动到右子树位置
 4. 递归i节点右子节点
  */

  /**
  用时：0ms
  内存：3MB
   */
func flatten(root *TreeNode)  {
	if root == nil {
		return
	}
	if root.Left == nil {
		flatten(root.Right)
		return
	}
	preNode := root.Left
	for preNode.Right != nil {
		preNode = preNode.Right
	}
	preNode.Right = root.Right
	root.Right = root.Left
	root.Left = nil
	flatten(root.Right)
}

