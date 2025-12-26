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
                if candidates[i] == prevNum:
                    continue
                combination.append(candidates[i])
                backtracking(i + 1, currTarget - candidates[i], combination)
                combination.pop()
                prevNum = candidates[i]
            

        backtracking(0, target, [])
        return result

s = Solution()
s.combinationSum2([10,2,1,6,5,1,7], 8)