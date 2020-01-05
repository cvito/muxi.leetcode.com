package source50

import "fmt"

/**
地址：https://leetcode-cn.com/problems/valid-parentheses/
题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

Example:
输入: "()"
输出: true

输入: "()[]{}"
输出: true

 */

/**
 用时：0ms
 内存：2MB
  */
func isValid(s string) bool {
	stack := make([]int32, 0)
	for _, v := range s {
		fmt.Println("v:", v)
		if len(stack) == 0 {
			stack = append(stack, v)
			continue
		}
		c1 := stack[len(stack)-1]
		if isMatch(c1, v) {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, v)
		}
	}
	if len(stack) == 0 {
		return true
	}
	return false
}

func isMatch(c1, c2 int32) bool {
	if c1 == '(' && c2 == ')' {
		return true
	} else if c1 == '{' && c2 == '}' {
		return true
	} else if c1 == '[' && c2 == ']' {
		return true
	}
	return false
}