
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) #4
        answer = [1] * length #[1,1,1,1]
        
        left_product = 1
        for i in range(length):
            answer[i] = left_product #at iteration 1 = 1
            left_product *= nums[i] # 1
        
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

        
