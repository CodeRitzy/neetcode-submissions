class Solution:
    def maxArea(self, heights: List[int]) -> int:
        units = 0
        i, j = 0, len(heights) - 1
        while i < j:
            units = max(min(heights[i], heights[j]) * (j - i), units)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return units

            