# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    # MinStack() initializes the stack object.
    def __init__(self):
        # The normal stack
        self.stack = []
        # The stack of the minimum for each element added
        self.minimumStack = []
        # Eg -> Stack [2, 8, 6, 3, 1, 9, 4]
        #   Min Stack [2, 2, 2, 2, 1, 1, 1]
        
    # void push(int val) pushes the element val onto the stack.
    def push(self, val: int) -> None:
        self.stack.append(val)

        if (len(self.minimumStack) == 0):
            self.minimumStack.append(val)
        else:
            if (self.minimumStack[len(self.minimumStack) - 1] <= val):
                self.minimumStack.append(self.minimumStack[len(self.minimumStack) - 1])
            else:
                self.minimumStack.append(val)
        return
        
    # void pop() removes the element on the top of the stack.
    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()
        return
        
    # int top() gets the top element of the stack.
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    # int getMin() retrieves the minimum element in the stack.
    def getMin(self) -> int:
        return self.minimumStack[len(self.minimumStack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin() # return -2