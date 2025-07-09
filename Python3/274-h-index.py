class Solution:    
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        i = n - 1
        hInd = 0
        while i > -1:
            if (citations[i] >= (n - i)):
                hInd = (n - i)
            else: 
                break
            i -= 1
        return hInd