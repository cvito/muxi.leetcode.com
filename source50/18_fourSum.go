package source50

import (
	"sort"
)

/**
地址：https://leetcode-cn.com/problems/4sum/
题目描述：
Given an array nums of n integers and an integer target, are there elements a, b, c,
and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

 */

/**
解题思路：
方法一：在3sum题目的基础上思考。先排序，使用4个指针，遍历判断。
 */

 //时间8ms，空间2.8MB
func FourSum(nums []int, target int) [][]int {
	if len(nums) < 4 {
		return nil
	}
	sort.Ints(nums)
	len := len(nums)
	if (nums[0] + nums[1] + nums[2] + nums[3] > target) ||
		(nums[len-1] + nums[len-2] + nums[len-3] + nums[len-4] < target) {
		return nil
	}

	result := make([][]int, 0)
	for i := 0; i < len-3; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		for j := i+1; j < len-2; j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}
			twoSum := nums[i] + nums[j]
			k := j + 1
			g := len - 1
			for k < g {
				if twoSum + nums[k] + nums[g] > target {
					g--
				} else if twoSum + nums[k] + nums[g] < target {
					k++
				} else {
					result = append(result, []int{nums[i], nums[j], nums[k], nums[g]})
					for k < g && nums[k] == nums[k+1] {
						k++
					}
					for k < g && nums[g] == nums[g-1] {
						g--
					}
					k++
					g--
				}
			}
		}
	}
	return result
}