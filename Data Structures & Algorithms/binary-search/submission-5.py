class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mini = start + ((end - start) // 2)
            if nums[mini] < target:
                start = mini + 1
            elif nums[mini] > target:
                end = mini - 1
            else: return mini
        return -1