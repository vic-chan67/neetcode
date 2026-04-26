class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        lProduct = 1
        for i in range(len(nums)):
            left.append(lProduct)
            lProduct *= nums[i]
        
        rProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            right.append(rProduct)
            rProduct *= nums[i]
        right.reverse()

        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        
        return res
