class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLength = len(nums)
        i = numsLength - 1
        while (i >= 0):
            if (nums[i] == val):
                # Put the furthest away non val number on this index
                nums[i] = nums[numsLength - 1]
                numsLength -= 1
            i -= 1
        return numsLength