class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 of length m + n, contains m elements and n 0s
        # nums2  of length n, contains n elements
        
        # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        # Output: [1,2,2,3,5,6]
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if (i > 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                nums1[i] = 0
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
