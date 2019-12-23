package main

import (
	"fmt"
	. "muxi.leetcode.com/source50"
)

func main() {

	//1-twoSum
	//input := []int{2, 7, 11, 15}
	//target := 9
	//result := TwoSum(input, target)

	//2-AddTwoNumbers
	//input1 := []int{2,4,3}
	//l1 := GenLinkList(input1)
	//
	//input2 := []int{5,6,4}
	//l2 := GenLinkList(input2)
	//result := AddTwoNumbers(l1, l2)
	//tmp := result
	//for tmp != nil {
	//	fmt.Println("tmp:", tmp.Val)
	//	tmp = tmp.Next
	//}

	//4-
	//result := FindMedianSortedArrays([]int{3,4}, []int{1})


	//5-
	//result := LongestPalindrome("cbbd")


	//10-
	//result := IsMatch("mississippi", "mis*is*p*.")

	//11-
	result := MaxArea([]int{1,8,6,2,5,4,8,3,7})

	//15-threeSum
	//input := []int{-1, 0, 1, 2, -1, -4}
	//input := []int{-1, 0, 1, 2, -1, -4}
	//result := ThreeSum(input)


	//16-threeSumClosest
	//input := []int{-1, 0, 1, 2, -1, -4}
	//input := []int{0, 0, -2}
	//result := ThreeSumClosest(input, 1)


	fmt.Println("result: ", result)
}


