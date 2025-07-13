class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) < sum(cost)):
            return -1
        
        startIndex = 0
        gasRem = 0
        for i in range(len(gas)):
            gasRem += (gas[i] - cost[i])
            if (gasRem < 0):
                gasRem = 0
                startIndex = i + 1
        return startIndex