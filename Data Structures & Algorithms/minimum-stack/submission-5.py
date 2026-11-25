class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else: 
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        return self.stack[-1]
        

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            self.min -= pop

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.min
        return self.min

    def getMin(self) -> int:
        return self.min
        
