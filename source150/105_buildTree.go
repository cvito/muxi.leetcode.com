package source150

/**
地址：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
题目描述：
根据一棵树的前序遍历与中序遍历构造二叉树。

Example:
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

 */

 /**
 思路：
 遍历前序数组，每个节点都是在中序数组中的位置假设为i，则中序数组的i左边为左子树,右边为右子树。利用递归思路。
  */

  /**
  用时：8ms
  内存：5.3MB
   */
func buildTree(preorder []int, inorder []int) *TreeNode {
	inOrderMap := make(map[int]int)
	for i, v := range inorder {
		inOrderMap[v] = i
	}
	return buildProgress(0, len(inorder), preorder, inorder, inOrderMap, new(int))
}

func buildProgress(left, right int, preOrders, inOrders []int, inOrderMap map[int]int, preIndex *int) *TreeNode {
	if left >= right {
		return nil
	}
	rootVal := preOrders[*preIndex]
	*preIndex += 1
	var root *TreeNode
	if v, ok := inOrderMap[rootVal]; ok {
		root = &TreeNode{Val:inOrders[v]}
		root.Left = buildProgress(left, v, preOrders, inOrders, inOrderMap, preIndex)
		root.Right = buildProgress(v+1, right, preOrders, inOrders, inOrderMap, preIndex)
	}
	return root
}