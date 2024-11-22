class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_l = 0
        zero_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            max_l = max(max_l, i - start)

        return max_l
