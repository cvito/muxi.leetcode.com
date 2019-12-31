package source100

/**
地址：https://leetcode-cn.com/problems/validate-binary-search-tree/
题目描述：
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

Example:

 */

/**
二叉搜索树的概念：
1. 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
3. 它的左、右子树也分别为二叉搜索树
 */

 /**
 思路：先通过中序，将数据放到数组中，遍历数组，判断是否为升序
  */

/**
执行用时 :8 ms
内存消耗 :6.8 MB
*/
func isValidBST(root *TreeNode) bool {
	nums := inOrder(root)
	for i, num := range nums {
		if i > 0 && num <= nums[i-1] {
			return false
		}
	}
	return true
}

func inOrder(root *TreeNode) []int {
	res := make([]int, 0)
	if root != nil {
		res = append(res, inOrder(root.Left)...)
		res = append(res, root.Val)
		res = append(res, inOrder(root.Right)...)
	}
	return res
}

