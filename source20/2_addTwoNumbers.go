package source20

import (
	. "muxi.leetcode.com/base/link"
)

/**
地址：https://leetcode-cn.com/problems/add-two-numbers/
题目描述：
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
 */

/**
解题思路：链表解题思路

 */


func AddTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	tmpl1, tmpl2, tmpRes := l1, l2, result
	carry := 0
	for tmpl1 != nil || tmpl2 != nil {
		var v1, v2 int
		if tmpl1 != nil {
			v1 = tmpl1.Val
			tmpl1 = tmpl1.Next
		}
		if tmpl2 != nil {
			v2 = tmpl2.Val
			tmpl2 = tmpl2.Next
		}

		sum := v1 + v2 + carry
		carry = sum / 10
		tmpRes.Next = &ListNode{Val:sum%10}
		tmpRes = tmpRes.Next
	}

	if carry != 0 {
		tmpRes.Next = &ListNode{Val:carry}
	}
	return result.Next
}