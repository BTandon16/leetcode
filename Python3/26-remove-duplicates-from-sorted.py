class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueLen = 0
        for i in range(len(nums)):
            if (uniqueLen == 0):
                uniqueLen += 1
                continue

            if (nums[i] > nums[uniqueLen - 1]):
                nums[uniqueLen] = nums[i]
                uniqueLen += 1
        return uniqueLen