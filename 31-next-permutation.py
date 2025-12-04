class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach: 
        # 1) If array in descending order, put it in ascending order 
        # 2) Else, keep iterating until either 
        # 2a) the last 2 element subarray is in ascending order 
        #       In this case, switch the 2 elements and return
        # OR
        # 2b) the subarray left is in descending order
        #       In this case, find the element in subarray just bigger than the element right before the subarray
        #       Put this new element as the element before subarray 
        #       and sort the remaining subarray with the element right before the subarray in ascending order and return

        # Maybe iterate backwards?
        n = len(nums)
        if (n == 1):
            return

        i = n - 1
        # Check if last 2 elements are in ascending order, if yes, swap and return
        if (nums[i] > nums [i - 1]):
            temp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = temp
            return
        
        # Find the first element from the back which is not in descending order
        while (nums[i] <= nums[i - 1]):
            i -= 1
            # If the entire array is in descending order, reverse it
            if (i == 0):
                nums.sort()
                # print(nums)
                return
        i -= 1
        j = n - 1
            
        # .sort() does not work on subarrays
        while (nums[j] <= nums[i]):
            j -= 1
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
        # nums[i + 1 : n].sort() 

        # Reverse the subarray from i + 1 to end
        i += 1
        j = n - 1
        while (j > i):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            j -= 1
            i += 1
        
        print(nums)
        return


s = Solution()
(s.nextPermutation([1]))
(s.nextPermutation([1,2,4,11,10,9,6,5,3]))