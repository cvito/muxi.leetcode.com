package source20

/**
地址：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
题目描述：
Given a string, find the length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

 */

 /**
 解题思路：
 方法一：使用窗口滑动思路。遍历整个字符串O(N)，用hash表存储数据，再用一个变量记住maxLong。时间复杂度为O(N)，空间复杂度为O(k)
 前后两个指针，一个记住开始的位置，一个记住最大长度位置。
  */


  //执行结果:12 ms, 3MB
func LengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	max := 0
	set := make(map[string]bool)
	for i, j := 0, 0; i < len(s) && j < len(s); {
		if len(s) - i < max {
			//最后剩下的长度已经小于已知的长度，则可以直接退出，不用继续遍历
			return max
		}
		if _, ok := set[string(s[j])]; !ok {
			set[string(s[j])] = true
			j++
			if len(set) > max {
				max = len(set)
			}
		} else {
			delete(set, string(s[i]))
			i++
		}
	}
	return max
}

//优化滑动窗口:12ms, 3.1MB(居然没有比上个更优)
//思路：hash表记录的value是i的下标。一旦发现已经有存在的字符，则直接跳到相同字符的下标i`+1，而不是通过i++来一步一步判断。
func LengthOfLongestSubstring_V2(s string) int {
	if len(s) == 0 {
		return 0
	}
	max := 0
	set := make(map[uint8]int)
	for i, j := 0, 0; j < len(s); j++ {
		if len(s) - i < max {
			//最后剩下的长度已经小于已知的长度，则可以直接退出，不用继续遍历
			return max
		}
		if v, ok := set[s[j]]; ok {
			if v > i {
				i = v
			}
		}
		if j-i+1 > max {
			max = j-i+1
		}
		set[s[j]] = j+1
	}
	return max
}