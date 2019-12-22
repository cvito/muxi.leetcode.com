package sort

func QuickSort(nums []int, left, right int) {
	if left > right {
		return
	}

	tl := left
	tr := right
	tmp := nums[tl]
	for tl < tr {
		for tl < tr && nums[tr] > tmp {
			tr--
		}
		if tl < tr {
			nums[tl] = nums[tr]
			tl++
		}

		for tl < tr && nums[tl] < tmp {
			tl++
		}
		if tl < tr {
			nums[tr] = nums[tl]
			tr--
		}
	}

	nums[tl] = tmp
	QuickSort(nums, left, tl-1)
	QuickSort(nums, tr+1, right)
}
