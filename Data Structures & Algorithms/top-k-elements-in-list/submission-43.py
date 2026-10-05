class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, nfreq in count.items():
            freq[nfreq].append(num)
        out = []
        for a in range(len(freq) - 1, -1,-1):
            for b in freq[a]:
                out.append(b)
                if len(out) == k:
                    return out
