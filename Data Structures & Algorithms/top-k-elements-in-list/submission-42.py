class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, n in count.items():
            freq[n].append(num)
        out = []
        for i in range(len(freq) - 1,-1,-1):
            for num in freq[i]:
                out.append(num)
                if len(out) == k:
                    return out
        
