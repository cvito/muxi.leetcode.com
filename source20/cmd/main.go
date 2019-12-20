package main

import (
	"fmt"
	. "muxi.leetcode.com/source20"
)

func main() {

	//1-two-sum
	nums := []int{2, 7, 11, 15}
	target := 9
	result := TwoSum(nums, target)



	fmt.Println("result: ", result)
}


