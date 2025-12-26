class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracking(index, currTarget, combination):
            if currTarget == 0:
                result.append(combination.copy())
                return
            elif currTarget < 0:
                return
            
            prevNum = -1
            for i in range(index, len(candidates)):
                # Don't need to start with the same number multiple times
                if candidates[i] == prevNum:
                    continue
                # If we reach a number higher than the target, then this combination will never work
                if candidates[i] > target:
                    break
                combination.append(candidates[i])
                backtracking(i + 1, currTarget - candidates[i], combination)
                # Remove the number from the list if we can no longer find combinations with it
                combination.pop()
                prevNum = candidates[i]
        
        backtracking(0, target, [])
        return result

s = Solution()
s.combinationSum2([10,2,1,6,5,1,7], 8)