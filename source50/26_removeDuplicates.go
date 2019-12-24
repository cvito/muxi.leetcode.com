package source50


/**
地址：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
题目描述：
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.


 */

/**
题目：移除掉多余的数字，并且改变输入的数组
解题思路：
方法一：用双指针，一前一后，判断不一致则将后的数字往前移动
 */


func RemoveDuplicates(nums []int) int {
	if len(nums) < 1 {
		return 0
	}
	i := 0
	for j := 1; j < len(nums); j++ {
		if nums[i] != nums[j] {
			i++
			nums[i] = nums[j]
		}
	}
	return i+1
}