class Solution:
    def jump(self, nums: List[int]) -> int:
        # Base Case for 0 jumps
        if (len(nums) <= 1):
            return 0
        # Base Case for 1 jump
        maxThisJump = nums[0]
        numJumps = 1
        if maxThisJump >= (len(nums) - 1):
            return numJumps
        
        # More than 1 jump
        l = r = 0
        while r < (len(nums) - 1):
            if (l > maxThisJump):
                numJumps += 1
                maxThisJump = r   
            r = max(r, (l + nums[l]))
            if (r >= len(nums) - 1):
                numJumps += 1
                break
            l += 1
        return numJumps