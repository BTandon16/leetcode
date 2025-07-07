class Solution:   
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        maxDist = nums[0]
        while True:
            if (maxDist >= len(nums) - 1):
                return True
            
            # Change maxDist to the maximum possible distance, but keep checking every index to see if it increases (until it can get to the end)
            maxDist = max(maxDist, (i + nums[i]))
            if (i == maxDist):
                return False
            i += 1