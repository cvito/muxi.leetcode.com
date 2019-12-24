package source50

/**
地址：https://leetcode-cn.com/problems/next-permutation/
题目描述：
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

 */

/**
解题思路：这是字典排序的题目。字典序算法介绍：https://blog.csdn.net/u011475134/article/details/75144248
字典序算法：
第一步：从右到左，找到第一个左边小于右边的数，设为list[a]。
第二步：从右到左，找到第一个大于list[a]的数，设为list[b]。
第三步：交换list[a],list[b]
第四步：将list[a]后面的数组，由小往大排列。
 */

func NextPermutation(nums []int)  {
	i := len(nums)-2
	for ; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			break
		}
	}
	if i >= 0 {
		j := len(nums)-1
		for ; j >= 0; j-- {
			if nums[j] > nums[i] {
				break
			}
		}
		swap(nums, i, j)
	}
	//i找不到，将整个数组反转
	reverse(nums, i+1)
}

func swap(nums []int, a, b int) {
	temp := nums[a]
	nums[a] = nums[b]
	nums[b] = temp
}

func reverse(nums []int, start int) {
	i, j := start, len(nums)-1
	for i < j {
		swap(nums, i, j)
		i++
		j--
	}
}