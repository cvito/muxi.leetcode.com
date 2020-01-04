package source250

/**
地址：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
题目描述：
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

Example:
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

 */

 /**
 思路：
 遍历每个节点，求出每个节点i的左右子树，是否有匹配的节点，当i节点的左右子树匹配的节点总数>=2,则说明这个节点i是所要求的公共祖先。
  */

  /**
  用时：36ms
  内存：10MB
   */
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	node, _ := commProgress(root, p, q)
	return node
}

func commProgress(root, p, q *TreeNode) (*TreeNode, int) {
	if root == nil {
		return nil, 0
	}
	if root == p && root == q {
		return root, 2
	}
	count := 0
	if root == p || root == q{
		count += 1
	}
	leftNode, leftCount	:= commProgress(root.Left, p, q)
	if leftCount == 2 {
		return leftNode, 2
	} else if leftCount + count == 2 {
		return root, 2
	}
	rightNode, rightCount := commProgress(root.Right, p, q)
	if rightCount == 2 {
		return rightNode, 2
	} else if rightCount + count == 2 {
		return root, 2
	}
	return root, leftCount + rightCount + count
}


//-==================
/**
  用时：12ms
  内存：7.1MB
   */
func lowestCommonAncestor_v2(root, p, q *TreeNode) *TreeNode {
	if root == nil || root == p || root == q {
		return root
	}
	leftNode := lowestCommonAncestor_v2(root.Left, p, q)
	rightNode := lowestCommonAncestor_v2(root.Right, p, q)
	if leftNode == nil {
		return rightNode
	} else if rightNode == nil {
		return leftNode
	}
	return root
}