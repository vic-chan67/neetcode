class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        occurences = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1
        
        for num, freq in frequency.items():
            occurences[freq].append(num)
        
        for i in range(len(occurences) -1, -1, -1):
            res.extend(occurences[i])
            if len(res) == k:
                return res