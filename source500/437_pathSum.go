package source500

/**
地址：https://leetcode-cn.com/problems/path-sum-iii/
题目描述：
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。


Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

 */


 /**
 思路：通过递归，判断左右子树各节点分别到0~i父节点的总数值

  */

  /**
  用时：8ms
  内存：4.5MB
   */
func pathSum(root *TreeNode, sum int) int {
	levelVal := make([]int, 1024)
	return inPathSum(root, sum, levelVal, 0)
}

func inPathSum(root *TreeNode, sum int, levelVal []int, level int) int {
	if root == nil {
		return 0
	}
	var nums int
	tmpSum := root.Val
	if tmpSum == sum {
		nums++
	}
	for i := level-1; i >= 0; i-- {
		tmpSum += levelVal[i]
		if tmpSum == sum {
			nums++
		}
	}
	levelVal[level] = root.Val
	nums += inPathSum(root.Left, sum, levelVal, level+1)
	nums += inPathSum(root.Right, sum, levelVal, level+1)
	return nums
}