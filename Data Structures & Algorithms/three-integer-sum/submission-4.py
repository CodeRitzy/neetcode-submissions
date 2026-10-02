class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            b = i + 1
            c = len(nums) - 1
            while b < c:
                if (a + nums[b] + nums[c] == 0):
                    out.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                elif a + nums[b] + nums[c] > 0:
                    c -= 1
                else: 
                    b += 1
                    
        return out