class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        i, j = 0,len(height) - 1
        leftMax, rightMax = height[i], height[j]
        while i < j:
            if (height[i] < height[j]):
                if (leftMax < height[i]):
                    leftMax = height[i]
                else:
                    total += leftMax - height[i]
                i += 1
            else:
                if (rightMax < height[j]):
                    rightMax = height[j]
                else:
                    total += rightMax - height[j]
                j -= 1
            
        return total