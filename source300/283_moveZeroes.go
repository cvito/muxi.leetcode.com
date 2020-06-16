package source350

import "fmt"

/**
地址：https://leetcode-cn.com/problems/move-zeroes/
题目描述：
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

Example:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

 */

  /**
  用时：4ms
  内存：3.7MB
   */
func moveZeroes(nums []int)  {
	step := 0
	for i, v := range nums {
		if v == 0 {
			step += 1
		} else {
			index := i-step
			nums[index] = v
		}
	}
	for i := len(nums)-step; i < len(nums); i++ {
		nums[i] = 0
	}
}
