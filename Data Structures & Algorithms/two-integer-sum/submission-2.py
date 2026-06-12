class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in mydict:
                return [mydict[need], i]
            else:
                mydict[nums[i]] = i
