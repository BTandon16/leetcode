from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        # 0 <= a, b, c, d < n
        # Each quadruplet returned [a, b, c, d] is distinct.
        # nums[a] + nums[b] + nums[c] + nums[d] == target
        # You may return the answer in any order.

        # Example 1:

        # Input: nums = [1,0,-1,0,-2,2], target = 0
        # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        # Example 2:

        # Input: nums = [2,2,2,2,2], target = 8
        # Output: [[2,2,2,2]]

        # Approach: Sort the input list in ascending order
        # Take the first x elements until we are left with 2 elements then use 2 sum

        output = []
        if (len(nums) < 4):
            return []
        
        nums.sort()

        for i in range(len(nums) - 3):
            if (i != 0):
                if (nums[i] == nums[i - 1]):
                    continue
            for j in range(i + 1, len(nums) - 2):
                if (j != i + 1):
                    if (nums[j] == nums[j - 1]):
                        continue

                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if (nums[i] + nums[j] + nums[l] + nums[r] == target):
                        # # Find a better (faster) way to check duplicates
                        # if [nums[i], nums[j], nums[l], nums[r]] not in output:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1]:
                            l += 1
                            if (l >= len(nums) - 1):
                                break
                        r -= 1
                    elif (nums[i] + nums[j] + nums[l] + nums[r] < target):
                        l += 1
                    elif (nums[i] + nums[j] + nums[l] + nums[r] > target):
                        r -= 1
        return output
    
s = Solution()
# print(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
# print(s.fourSum(nums = [2,2,2,2,2], target = 8))
# print(s.fourSum(nums = [-3,-2,-1,0,0,1,2,3], target = 0))
print(s.fourSum(nums = [-2,-1,-1,1,1,2,2], target = 0))
