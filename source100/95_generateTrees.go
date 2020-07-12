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



func respace(dictionary []string, sentence string) int {
    n, inf := len(sentence), 0x3f3f3f3f
    root := &Trie{next: [26]*Trie{}}
    for _, word := range dictionary {
        root.insert(word)
    }
    dp := make([]int, n + 1)
    for i := 1; i < len(dp); i++ {
        dp[i] = inf
    }
    for i := 1; i <= n; i++ {
        dp[i] = dp[i-1] + 1
        curPos := root
        for j := i; j >= 1; j-- {
            t := int(sentence[j-1] - 'a')
            if curPos.next[t] == nil {
                break
            } else if curPos.next[t].isEnd {
                dp[i] = min(dp[i], dp[j-1])
            }
            if dp[i] == 0 {
                break
            }
            curPos = curPos.next[t]
        }
    }
    return dp[n]
}

type Trie struct {
    next [26]*Trie
    isEnd bool
}

func (this *Trie) insert(s string) {
    curPos := this
    for i := len(s) - 1; i >= 0; i-- {
        t := int(s[i] - 'a')
        if curPos.next[t] == nil {
            curPos.next[t] = &Trie{next: [26]*Trie{}}
        }
        curPos = curPos.next[t]
    }
    curPos.isEnd = true
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

