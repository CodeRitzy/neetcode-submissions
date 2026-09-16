# hashmap
# map num with count
# loop through list map num with occurence
# 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, nfreq in count.items():
            freq[nfreq].append(num)

        out = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                out.append(num)
                if len(out) == k:
                    return out
        return out

        
        
        
        