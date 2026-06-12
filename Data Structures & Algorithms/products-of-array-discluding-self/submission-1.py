class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mydict = {}
        mydict["lists"] = []
        mydict["product"] = []
        for i, n in enumerate(nums):
            left = nums[:i]
            right = nums[i+1:]
            mydict["lists"].append(left + right)
        for prod in mydict["lists"]:
            results = 1
            for x in prod:
                results *= x
            mydict["product"].append(results)
        mylist = list(mydict.get("product"))
        return mylist