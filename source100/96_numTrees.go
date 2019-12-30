package source100

/**
地址：https://leetcode-cn.com/problems/unique-binary-search-trees/
题目描述：
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

Example:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

 */

/**
二叉搜索树的概念：
1. 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
3. 它的左、右子树也分别为二叉搜索树
 */

 /**
 定义两个函数
1. G(n): 长度为n的序列的不同二叉搜索树个数。
2. F(i,n): 以i为根的不同二叉搜索树个数(1≤i≤n)。
G(n)=n∑i=1⋅F(i,n)
F(i,n)=G(i−1)⋅G(n−i)
 G(n)=n∑i=1⋅G(i−1)⋅G(n−i) (n>2)
 当前i，依赖于前面的数组
 G[0]=1
 G[1]=1
 G[2]=G[0]*G[1]+G[1]*G[0]=1*1+1*1=1+1=2
 G[3]=G[0]*G[2]+G[1]*G[1]+G[2]*G[0]=1*2+1*1+2*1=2+1+2=5
 ...
 ...
  */

func numTrees(n int) int {
	res := make([]int, n+1)
	res[0] = 1
	res[1] = 1
	for i := 2; i <= n; i++ {
		for j := 1; j <= i; j++ {
			res[i] += res[j-1]*res[i-j]
		}
	}
	return res[n]
}

