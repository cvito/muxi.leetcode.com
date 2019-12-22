package source20

import (
	"math"
)

/**
地址：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
题目描述：
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
 */

 /**
 解题思路：
  left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
  */


func FindMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	len1, len2 := len(nums1), len(nums2)
	if len1 > len2 {
		//保证len2>len1恒成立
		tmp := nums1
		nums1 = nums2
		nums2 = tmp
		len1, len2 = len(nums1), len(nums2)
	}

	iMin, iMax := 0, len1
	half := (len1 + len2 + 1) / 2
	for iMin <= iMax {
		i := (iMin + iMax) / 2
		j := half - i
		if i < iMax && nums2[j-1] > nums1[i] {
			iMin = i + 1
		} else if i > iMin && nums2[j] < nums1[i-1] {
			iMax = i - 1
		} else {
			var maxLeft float64
			if i == 0 {
				maxLeft = float64(nums2[j-1])
			} else if j == 0 {
				maxLeft = float64(nums1[i-1])
			} else {
				maxLeft = math.Max(float64(nums1[i-1]), float64(nums2[j-1]))
			}
			if (len1 + len2) % 2 == 1 {
				return maxLeft
			}

			var minRight float64
			if i == len1 {
				minRight = float64(nums2[j])
			} else if j == len2 {
				minRight = float64(nums1[i])
			} else {
				minRight = math.Min(float64(nums1[i]), float64(nums2[j]))
			}
			return (maxLeft + minRight) / 2.0
		}
	}
	return 0.0
}