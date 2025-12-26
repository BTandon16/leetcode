from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach: 
        # 1. i = 0
        # 2. Add current index to the combination list
        # 3. Compare total with target
        # 4. If less than target, repeat 2
        # 5. If equal to target, add combination to the result
        # 6. Return and increase the index for the addition to the list

        result = []
        def dfs(index, combination, total):
            if total == target:
                result.append(combination.copy())
                return
            elif total > target:
                return
            elif total < target:
                # If total is less than target, then add the current index to the combination
                combination.append(candidates[index])
                total += candidates[index]
                dfs(index, combination, total)
        
                # After removing the current index, check with the next index
                combination.pop()
                total -= candidates[index]
                if (index + 1 < len(candidates)):
                    dfs(index + 1, combination, total)
            return
        

        dfs(0, [], 0)
        return result
        
s = Solution()
s.combinationSum([2,3,5,7], 8)