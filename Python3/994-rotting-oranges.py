from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m x n grid
        # 0 represents empty cell
        # 1 represents good orange
        # 2 represents rotten orange

        # Each 2 can expand in 4 directions (up, down, right, left) and convert 1s into 2s (does not affect 0s)
        # Each iteration of expansion of all 2s is 1 minute
        # Return minimum time for all cells to be either 2s or 0s, else return -1


        # Approach: 
        # 1. Find each 2 in the grid and store them in a queue (set, so no duplicates)
        # 2. Find each 1 in the grid and count the total
        # 3. Run BFS through every 2 in the grid and remove from queue (Add a minute at the end of this queue)
        # 4. Change every 1 reached through BFS to 2 and add it to the queue. Reduce 1 from the total
        # 5. When the queue is finished, check the count of 1s and if it is more than 0, return -1
        queue = deque()
        oneCount = 0
        timeCount = 0
        queueCount = 0

        # Check for 1s and 2s
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    oneCount += 1
                elif (grid[i][j] == 2):
                    # queue.append([i,j])
                    queue.append([i,j])
        
        i = 0
        tempQueueCount = len(queue)
        visitedCount = 0
        # tempQueueCount = queueCount
        while (i <= (len(queue) - 1) and oneCount > 0):
            # print(queue[i][0], queue[i][1])
            # print(visitedCount)
            # grid[queue[i][0], queue[i][1]] is the coordinates in the grid
            # BFS from the queue
            if (queue[i][0] - 1 >= 0 and grid[queue[i][0] - 1][queue[i][1]] == 1):
                grid[queue[i][0] - 1][queue[i][1]] = 2
                oneCount -= 1
                queue.append([queue[i][0] - 1, queue[i][1]])

            if (queue[i][0] + 1 <= (len(grid) - 1) and grid[queue[i][0] + 1][queue[i][1]] == 1):
                grid[queue[i][0] + 1][queue[i][1]] = 2
                oneCount -= 1
                queue.append([queue[i][0] + 1, queue[i][1]])

            if (queue[i][1] - 1 >= 0 and grid[queue[i][0]][queue[i][1] - 1] == 1):
                grid[queue[i][0]][queue[i][1] - 1] = 2
                oneCount -= 1
                queue.append([queue[i][0], queue[i][1] - 1])

            if (queue[i][1] + 1 <= (len(grid[queue[i][0]]) - 1) and grid[queue[i][0]][queue[i][1] + 1] == 1):
                grid[queue[i][0]][queue[i][1] + 1] = 2
                oneCount -= 1
                queue.append([queue[i][0], queue[i][1] + 1])
            
            # Remove from queue after finishing BFS and add to the visitedCount
            queue.popleft()
            visitedCount += 1

            if (oneCount == 0):
                timeCount += 1
                break

            if (visitedCount == tempQueueCount):
                # Update current time to the next minute
                timeCount += 1
                # Get the new tempQueueCount (all the newly added 2s in the past minute)
                tempQueueCount = len(queue)
                # Set the visitedCount back to 0 for the new minute
                visitedCount = 0  
        
        # When the queue is empty OR all the 1s have already been converted
        if (oneCount == 0):
            return timeCount
        
        return -1
    
s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
# print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
# print(s.orangesRotting([[0,2]]))

