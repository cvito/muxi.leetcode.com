package source50

import "math"

/**
地址：https://leetcode-cn.com/problems/container-with-most-water/
题目描述：
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
 */

 /**
 解题思路：
 方法一：采用双指针方式，前后指针，每次指针向更高方向移动
  */

 //时间16 ms，空间5.8MB
func MaxArea(height []int) int {
	if len(height) < 2 {
		return 0
	}

	left, right := 0, len(height)-1
	result := 0
	for left < right {
		sum := int(math.Min(float64(height[left]), float64(height[right]))) * (right - left)
		if sum > result {
			result = sum
		}
		if height[left] > height[right] {
			right--
		} else {
			left++
		}
	}
	return result
}