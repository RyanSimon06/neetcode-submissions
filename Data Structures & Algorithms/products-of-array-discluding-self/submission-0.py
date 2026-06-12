class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mydict = {}
        for i, n in enumerate(nums):
            result = 1
            copy = nums[:]
            copy.pop(i)
            for x in copy:
                result *= x
                mydict[i] = result
        mylist = list(mydict.values())
        return mylist