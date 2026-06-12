class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        clist = list(sorted_dict)
        return clist[:k]