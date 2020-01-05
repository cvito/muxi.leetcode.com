package source200

import "math"

/**
地址：https://leetcode-cn.com/problems/min-stack/
题目描述：
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
 */

/**
 用时：20ms
 内存：7.5MB
  */
type MinStack struct {
	myStack []int
	min int
}


/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{
		myStack: make([]int, 0),
		min: math.MaxInt32,
	}
}


func (this *MinStack) Push(x int)  {
	if x <= this.min {
		this.myStack = append(this.myStack, this.min)
		this.min = x
	}
	this.myStack = append(this.myStack, x)
}


func (this *MinStack) Pop()  {
	l := len(this.myStack)
	if l <= 0 {
		return
	}

	last := this.myStack[l-1]
	this.myStack = this.myStack[:l-1]

	l = len(this.myStack)
	if last == this.min && l > 0 {
		this.min = this.myStack[l-1]
		this.myStack = this.myStack[:l-1]
	}
}


func (this *MinStack) Top() int {
	l := len(this.myStack)
	if l <= 0 {
		return 0
	}
	return this.myStack[l-1]
}


func (this *MinStack) GetMin() int {
	return this.min
}