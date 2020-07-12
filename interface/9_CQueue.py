class CQueue:

    def __init__(self):
        self.stack_master = []
        self.stack_tmp = []

    def appendTail(self, value: int) -> None:
        self.stack_master.append(value)


    def deleteHead(self) -> int:
        if not self.stack_master: return -1
        while len(self.stack_master) != 0:
            self.stack_tmp.append(self.stack_master.pop())
        head = self.stack_tmp.pop()
        while len(self.stack_tmp) != 0:
            self.stack_master.append(self.stack_tmp.pop())
        return head




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()