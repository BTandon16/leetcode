class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueLen = 1
        count = 1
        temp = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] == temp):
                if (count < 2):
                    count += 1
                    nums[uniqueLen] = nums[i]
                    uniqueLen += 1
            elif (nums[i] > temp):
                nums[uniqueLen] = nums[i]
                temp = nums[uniqueLen]
                count = 1
                uniqueLen += 1
        return uniqueLen