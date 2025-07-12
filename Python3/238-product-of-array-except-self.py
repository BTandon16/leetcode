class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First Solution - This method is really slow
        
        # prefMult = [1] * len(nums)
        # suffMult = [1] * len(nums)
        # answer = [1] * len(nums)
        # for i in range(len(nums)):
        #     if (i > 0):
        #         prefMult[i] = nums[i - 1] * prefMult[i - 1]
        #     # if (i < (len(nums) - 1)):
        #         suffMult[(len(nums) - 1) - i] = nums[(len(nums) - 1) - i + 1] * suffMult[(len(nums) - 1) - i + 1]
            
        # for i in range(len(nums)):   
        #     answer[i] = prefMult[i] * suffMult[i]
        # return answer

        # Second Solution - Improved (probably still not perfect tho)
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = nums[i - 1] * answer[i - 1]

        suffMult = 1
        for i in range(len(nums) - 2, -1, -1):
            suffMult  = suffMult * nums[i + 1]
            answer[i] = answer[i] * suffMult
        
        return answer