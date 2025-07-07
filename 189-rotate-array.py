class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # The following code works, but it's really slow
        # for i in range((k % len(nums))):
        #     nums.insert(0, nums.pop(len(nums) - 1))

        def reverseArray(array: List[int], left: int, right: int):
            while left < right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        # Reduce k to a number less than the length of the list (rotate only when needed)
        k = k % len(nums)

        # Reverse entire array
        reverseArray(nums, 0, len(nums) - 1)

        # Reverse first k elements
        reverseArray(nums, 0, k - 1)

        # Reverse remaining elements
        reverseArray(nums, k, len(nums) - 1)
