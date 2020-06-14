import bisect
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        print("start end:", arr)
        arr.sort()
        print("sort end:", arr)

        pre_val_sum=[0]
        size = len(arr)
        for v in arr:
            pre_val_sum.append(pre_val_sum[-1] + v)

        range_start, range_end = int(target/size), max(arr)
        res, diff = 0, target
        for i in range(range_start, range_end):
            it_index = bisect.bisect_left(arr, i)
            print("it_index", it_index)
            target_sum = pre_val_sum[it_index] + (size - it_index) * i
            curr_diff = abs(target_sum - target)
            if curr_diff < diff:
                res, diff = i, curr_diff
        return res

