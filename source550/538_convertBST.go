package source550

/**
地址：https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
题目描述：
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。


Example:
输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

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
 思路1：可以按照中序将树节点放到数组中，从尾到头遍历，累加。
 思路2：借助栈，先遍历右子节点-->中节点-->左节点的顺序

  */

  /**
  用时：20ms
  内存：6.6MB
   */
func convertBST(root *TreeNode) *TreeNode {
	stack := make([]*TreeNode, 0)
	preSum := 0
	curNode := root
	for curNode != nil || len(stack) != 0 {
		for curNode != nil {
			stack = append(stack, curNode)
			curNode = curNode.Right
		}
		curNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		curNode.Val += preSum
		preSum = curNode.Val
		curNode = curNode.Left
	}
	return root
}