package source100

/**
地址：https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/
题目描述：
给出二叉搜索树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

Example:
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

 */


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 /**
 思路：
 1. 每一层遍历完成，直到最后一层都是叶子节点
 2. 给定一个节点i, 如果存在右子节点，则右子为其总数+本身
 3. 如果存在父节点，并且自己为左子节点，则加上其父节点总数+本身

 思路：
 使用栈，中序遍历，用一个数组保存所有节点
  */

func bstToGst(root *TreeNode) *TreeNode {
	nodeList := inOrder(root)
	for i := len(nodeList)-2; i >= 0; i-- {
		nodeList[i].Val += nodeList[i+1].Val
	}
	return root
}

func inOrder(root *TreeNode) []*TreeNode {
	res := make([]*TreeNode, 0)
	if root != nil {
		res = append(res, inOrder(root.Left)...)
		res = append(res, root)
		res = append(res, inOrder(root.Right)...)
	}
	return res
}