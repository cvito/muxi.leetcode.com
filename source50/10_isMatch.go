package source50

/**
地址：https://leetcode-cn.com/problems/regular-expression-matching/
题目描述：
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
 */

 /**
 解题思路：
 方法一：回溯法
 先判断常规字符，再判断'.'字符，再特殊判断'*'字符。
  */


func IsMatch(s string, p string) bool {
	if len(p) == 0 {
		return len(s) == 0
	}

	firstMatch := (len(s) != 0) && (s[0] == p[0] || p[0] == '.')
	if len(p) >= 2 && p[1] == '*' {
		return (IsMatch(s, p[2:])) || (firstMatch && IsMatch(s[1:], p))
	} else {
		return firstMatch && IsMatch(s[1:], p[1:])
	}
}