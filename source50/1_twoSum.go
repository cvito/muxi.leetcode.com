package source50

/**
地址：https://leetcode-cn.com/problems/two-sum/
题目描述：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 */

 /**
 解题思路：
 方法一：暴力遍历两次。时间复杂度是O(n^2)
 方法二：两遍hash方法，第一遍将值存进hash表，第二遍查找每一个值。时间复杂度是O(n)+空间复杂度O(n)
 方法三：一次hash方法。遍历一次值，每次去表中查找，不存在则存入。时间复杂度是O(n)+空间复杂度O(n)
  */


func TwoSum(nums []int, target int) []int {
	h := make(map[int]int)
	for i, num := range nums {
		v, ok := h[target - num]
		if !ok {
			h[num] = i
			continue
		}
		return []int{v, i}
	}
	return nil
}