class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = defaultdict(int)
        long = 0
        for num in nums:
            if ns[num] == 0:
                ns[num] = ns[num - 1] + ns[num + 1] + 1
                ns[num - ns[num - 1]] = ns[num]
                ns[num + ns[num + 1]] = ns[num]
            long = max(long, ns[num])
        return long