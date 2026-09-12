class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pervMAP = {} # value, indx

        for i, n in enumerate(nums):
            diff = target -n 
            if diff in pervMAP:
                return [pervMAP[diff] ,i]
            pervMAP[n]=i
        return