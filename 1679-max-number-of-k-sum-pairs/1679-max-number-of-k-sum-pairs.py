class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        left , right = 0 , len(nums)-1
        count=0
        nums.sort()
        
        while left < right:
            target_sum=nums[left]+nums[right]
            
            if target_sum==k:
                count+=1
                left+=1
                right-=1
            
            elif target_sum<k:
                left+=1
            else:
                right-=1
                
        return count
            
            
        
        

                    
            
        