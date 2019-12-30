package source100

import "fmt"

/**
地址：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
题目描述：
给定一个二叉树，返回它的中序 遍历。

Example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
 */


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 //递归方式
func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	res := make([]int,0)
	if lRes := inorderTraversal(root.Left); lRes != nil {
		res = append(res, lRes...)
	}

	res = append(res, root.Val)
	if rRes := inorderTraversal(root.Right); rRes != nil {
		res = append(res, rRes...)
	}
	return res
}

//使用栈方式
func inorderTraversal_v2(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	stack := make([]*TreeNode, 0)
	result := make([]int, 0)
	currNode := root
	for currNode != nil || len(stack) != 0 {
		for currNode != nil {
			stack = append(stack, currNode)
			currNode = currNode.Left
		}
		if popNode := stack[len(stack)-1]; popNode != nil {
			fmt.Println("popNode.Val", popNode.Val)
			stack = stack[:len(stack)-1]
			result = append(result, popNode.Val)
			currNode = popNode.Right
		}
	}
	return result
}