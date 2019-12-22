package source20

import (
	"math"
	"sort"
)

/**
地址：https://leetcode-cn.com/problems/3sum-closest/
题目描述：
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 */

/**
解题思路：
方法一：暴力遍历三次。时间复杂度是O(n^3)
方法二：与第15题思路类似。先将数组排序O(NlogN)，重头遍历数组一次O(n)，两个指针分别指向前后来移动判断O(n)，外加一个min变量。时间复杂度是O(nlogn)+O(n)*O(n)。空间复杂度是O(1)
 */

func ThreeSumClosest(nums []int, target int) int {
	if nums == nil || len(nums) < 3 {
		return 0
	}

	sort.Ints(nums)
	result := nums[0]+nums[1]+nums[2]
	for i, v := range nums {
		if i > 0 && v == nums[i-1] {
			continue
		}
		left := i+1
		right := len(nums)-1
		for left < right {
			sum := v + nums[left] + nums[right]
			if math.Abs(float64(sum-target)) < math.Abs(float64(result-target)) {
				result = sum
			}
			if sum > target {
				right--
			} else if sum < target {
				left++
			} else {
				return result
			}
		}
	}
	return result
}