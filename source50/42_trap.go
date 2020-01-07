package source50

import (
	"math"
)

/**
地址：https://leetcode-cn.com/problems/trapping-rain-water/
题目描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

比如：
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
 */

/**
解题思路：用双指针思路
 */

/**
 用时：4ms
 内存：2.8MB
  */
func trap(height []int) int {
	res := 0
	left, right := 0, len(height)-1
	leftMax, rightMax := 0, 0
	for left < right {
		if height[left] < height[right] {
			if height[left] >= leftMax {
				leftMax = height[left]
			} else {
				res += leftMax - height[left]
			}
			left++
		} else {
			if height[right] >= rightMax {
				rightMax = height[right]
			} else {
				res += rightMax - height[right]
			}
			right--
		}
	}
	return res
}

//==========使用数组记住i节点的左边高度和右边高度，遍历求出每个节点i的容量==================
/**
 用时：8ms
 内存：3.1MB
  */
func trap_v2(height []int) int {
	if len(height) == 0 {
		return 0
	}
	leftHeight := make([]int, len(height)-1)
	leftHeight[0] = height[0]
	for i := 1; i < len(height); i++ {
		leftHeight[i] = int(math.Max(float64(height[i]), float64(leftHeight[i-1])))
	}

	rightHeight := make([]int, len(height)-1)
	rightHeight[len(height)-1] = height[len(height)-1]
	for i := len(height)-2; i >= 0; i-- {
		rightHeight[i] = int(math.Max(float64(height[i]), float64(rightHeight[i+1])))
	}

	res := 0
	for i := 0; i <= len(height)-1; i++ {
		res += int(math.Min(float64(leftHeight[i]), float64(rightHeight[i]))) - height[i]
	}
	return res
}