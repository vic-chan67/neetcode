class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i, n in enumerate(nums):
            if (target - n not in checked):
                checked[n] = i
            else:
                if i <= checked[target - n]:
                    return [i, checked[target - n]]
                else:
                    return [checked[target - n], i]