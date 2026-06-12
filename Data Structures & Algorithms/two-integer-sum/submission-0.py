class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, x in enumerate(nums):
            mydict[nums[i]] = x
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]