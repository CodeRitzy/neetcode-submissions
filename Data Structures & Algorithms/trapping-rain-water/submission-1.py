class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height) - 1
        lMax,rMax = height[l], height[r]
        total = 0
        while l < r:
            if height[l] < height[r]:
                if lMax < height[l]:
                    lMax = height[l]
                else: total += lMax - height[l]
                l += 1
            else:
                if rMax < height[r]:
                    rMax = height[r]
                else: 
                    total += rMax - height[r]
                r -= 1

        return total