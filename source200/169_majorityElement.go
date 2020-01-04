package source200

import "sort"

/**
地址：https://leetcode-cn.com/problems/majority-element/
题目描述：
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
求众数。

Example:
示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
 */


  /**
  用时：24ms
  内存：5.9MB
   */
func majorityElement(nums []int) int {
	sort.Ints(nums)
	return nums[len(nums)/2]
}