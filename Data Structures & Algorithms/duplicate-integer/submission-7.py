class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for num in nums:
            numbers.add(num)

        if len(numbers) != len(nums):
            return True
        return False