package source20

import (
	"sort"
)

/**
地址：https://leetcode-cn.com/problems/3sum/
题目描述：
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example:
Given nums = [-1, 0, 1, 2, -1, -4]
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
 */

/**
解题思路：
方法一：暴力遍历三次。时间复杂度是O(n^3)
方法二：将三个数相加转为a+b=0-c --》即变为两数相加。时间复杂度是O(n^2)+空间复杂度O(n)
方法三：先将数组排序O(NlogN)，重头遍历数组一次O(n)，两个指针分别指向前后来移动判断O(n)。时间复杂度是O(nlogn)+O(n)*O(n)。
 */

func ThreeSum(nums []int) [][]int {
	if nums == nil || len(nums) < 3 {
		return nil
	}

	sort.Ints(nums)
	if nums[0] * nums[len(nums)-1] > 0 {
		//去掉整个数字同符合的情况
		return nil
	}

	result := make([][]int, 0)
	for i, v := range nums {
		//去掉相同数字的多次计算
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		sum := 0-nums[i]
		left := i+1
		right := len(nums)-1
		for left < right {
			tmpSum := nums[left] + nums[right]
			if tmpSum < sum {
				left++
			} else if tmpSum > sum {
				right--
			} else {
				result = append(result, []int{v, nums[left], nums[right]})
				for left < right && nums[left] == nums[left+1] {
					left++
				}
				for left < right && nums[right] == nums[right-1] {
					right--
				}
				left++
				right--
			}
		}
	}
	return result
}