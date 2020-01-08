package source150

import "fmt"

/**
地址：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
题目描述：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

Example:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

 */

 /**
 思路：
  */

  /**
  用时：16ms
  内存：3.2MB
   */
func maxProfit(prices []int) int {
	if len(prices) <= 1 {
		return 0
	}
	max, inIndex := 0, -1
	for i := 0; i < len(prices); i++ {
		fmt.Println("val:", prices[i])
		if inIndex == -1 {
			if i < len(prices)-1 && prices[i] < prices[i+1] {
				inIndex = i
			}
			continue
		}
		if prices[i] == prices[inIndex] {
			continue
		}
		fmt.Println("inIndex:", prices[inIndex])
		if prices[i] > prices[inIndex] {
			v := prices[i] - prices[inIndex]
			if v > max {
				max = v
			}
		} else {
			inIndex = i
		}
	}
	return max
}
