package source250

import (
	"container/heap"
	"fmt"
	myHeap "muxi.leetcode.com/base/heap"
	"sort"
)

/**
地址：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
题目描述：
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

Example:
示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

 */

/**
  用时：8ms O(NlogN)
  内存：3.5MB
   */
func findKthLargest(nums []int, k int) int {
	sort.Ints(nums)
	return nums[len(nums)-k]
}


/**
  用时：144ms
  内存：4MB
   */
func findKthLargest_v2(nums []int, k int) int {
	h := myHeap.New()
	fmt.Println("heap1:", h)
	for _, v := range nums {
		if h.Len() >= k {
			if h.Top().(int) < v {
				h.PopFront()
			} else {
				continue
			}
		}
		h.Push(v)
		heap.Init(h)
		fmt.Println("heap2:", h)
	}
	fmt.Println("heap3:", h)
	return h.PopFront().(int)
}

