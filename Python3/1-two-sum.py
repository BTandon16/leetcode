class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)
        left = 0
        right = len(nums2) - 1
        while left < right:
            if (nums2[left] + nums2[right] == target):
                if (nums2[left] == nums2[right]):
                    return (nums.index(nums2[left]), nums.index(nums2[right], nums.index(nums2[left]) + 1))    
                return (nums.index(nums2[left]), nums.index(nums2[right]))
            elif (nums2[left] + nums2[right] > target):
                right -= 1
            else:
                left += 1
        return -1