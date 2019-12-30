package source100

/**
地址：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
题目描述：
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

Example:
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

 */

/**
二叉搜索树的概念：
1. 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
3. 它的左、右子树也分别为二叉搜索树
 */

func generateTrees(n int) []*TreeNode {
	if n < 1 {
		return nil
	}
	return generateChild(1, n)
}

func generateChild(start, end int) []*TreeNode {
	resList := make([]*TreeNode, 0)
	if start > end {
		resList = append(resList, nil)
		return resList
	}

	for i := start; i <= end; i++ {
		leftTreeList := generateChild(start, i-1)
		rightTreeList := generateChild(i+1, end)
		for _, leftNode := range leftTreeList {
			for _, rightNode := range rightTreeList {
				rootNode := &TreeNode{Val:i, Left: leftNode, Right: rightNode}
				resList = append(resList, rootNode)
			}
		}
	}
	return resList
}