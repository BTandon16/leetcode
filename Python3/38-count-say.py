class Solution:
    def countAndSay(self, n: int) -> str:
        # Iterative Solution
        i = 1
        out = "1"
        output = ""
        while (i < n):
            count = 0
            for j in range(len(out)):
                if j == 0:
                    curr = out[j]
                    count = 1
                    continue
                
                if out[j] != curr:
                    output += (str(count) + curr)
                    count = 1
                    curr = out[j]
                else:
                    count += 1
            
            out = output + (str(count) + curr)
            output = ""
            i += 1
        
        return out

s = Solution()
s.countAndSay(1)

