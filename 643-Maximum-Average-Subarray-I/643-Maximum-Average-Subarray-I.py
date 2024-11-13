from typing import list


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[:k])
        max_avg = sum(nums[:k]) / k
        for i in range(k, n):
            cur_sum = cur_sum + nums[i] - nums[i - k]
            avg = cur_sum / k
            if avg > max_avg:
                max_avg = avg
        return max_avg
