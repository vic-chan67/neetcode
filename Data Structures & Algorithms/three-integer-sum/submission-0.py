class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            left = i+1
            right = len(nums) - 1

            if i > 0 and n == nums[i-1]:
                continue
            
            while left < right:
                if n + nums[left] + nums[right] < 0:
                    left += 1
                elif n + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res

