class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for num, freq in count.items():
            bucket[freq].append(num)
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # iterate from end to start
            for num in bucket[i]:                  # iterate over elements at that frequency
                result.append(num)
                if len(result) == k:
                    return result