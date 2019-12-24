package source50

import (
	"fmt"
	. "muxi.leetcode.com/base/search"
	)

/**
地址：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
题目描述：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
 */

/**
解题思路：时间复杂度要求在O(logN),可以用二分查找。
 */

func Search(nums []int, target int) int {
	if len(nums) < 1 {
		return -1
	}
	if len(nums) == 1 {
		if nums[0] == target {
			return 0
		} else {
			return -1
		}
	}
	minIndex := findRotateIndex(nums, 0, len(nums)-1)
	fmt.Println("minIndex:", minIndex)

	if nums[minIndex] == target {
		return minIndex
	}
	if minIndex == 0 {
		return BinarySearch(nums, target)
	}
	if target < nums[0] {
		res := BinarySearch(nums[minIndex:], target)
		if res != -1 {
			return res + minIndex
		}
		return res
	}
	return BinarySearch(nums[:minIndex], target)
}

func findRotateIndex(nums []int, left, right int) int {
	if len(nums) < 2 || nums[left] < nums[right] {
		return 0
	}
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] > nums[mid+1] {
			return mid + 1
		} else {
			if nums[mid] > nums[left] {
				left = mid + 1
			} else {
				right = mid
			}
		}
	}
	return -1
}
