class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsort = sorted(nums)
        tups = []

        for i, n in enumerate(numsort):
            if i > 0 and numsort[i] == numsort[i-1]:
                continue
            j = i + 1
            k = len(numsort) - 1

            while j < k:
                if i != j and i != k: 
                    z = numsort[j] + numsort[k]
                    x = z + n
                    if x > 0:
                        k -= 1
                    elif x < 0:
                        j += 1
                    elif x == 0:
                        if [n, numsort[j], numsort[k]] not in tups:
                            tups.append([n, numsort[j], numsort[k]])
                        j += 1
                        while j < k and numsort[j] == numsort[j-1]:
                            j += 1

        return tups