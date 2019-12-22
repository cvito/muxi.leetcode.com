package source20

import (
	"math"
)

/**
地址：https://leetcode-cn.com/problems/longest-palindromic-substring/
题目描述：
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
 */

 /**
 解题思路：中心扩展算法
 遍历整个字符串，以当前字符为中心是一个情况，以两个字符间为中心也是一种情况。即可能情况是2N-1种。
  */

  //用时4ms，内存2.2MB
func LongestPalindrome(s string) string {
	if len(s) < 2 {
		return s
	}
	start, end := 0, 0
	for i := range s {
		len1 := searchMaxLen(s, i, i)
		len2 := searchMaxLen(s, i, i+1)
		maxLen := int(math.Max(float64(len1), float64(len2)))
		if maxLen > end + 1 - start {
			start = i - (maxLen-1) / 2
			end = i + maxLen / 2
		}
	}
	return s[start:end+1]
}

func searchMaxLen(s string, left int, right int) int {
	for (left >= 0 && right < len(s)) && s[left] == s[right] {
		left--
		right++
	}
	return right-left-1
}