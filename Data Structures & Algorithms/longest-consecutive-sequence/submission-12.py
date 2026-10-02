class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all = defaultdict(int)
        long = 0
        for num in nums:
            if all[num] == 0:
                all[num] = all[num - 1] + all[num + 1] + 1
                all[num - all[num - 1]] = all[num]
                all[num + all[num + 1]] = all[num]
                long = max(long, all[num])
        return long