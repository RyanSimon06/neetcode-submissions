class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        mcon = 0

        while left < right:
            mult = min(heights[left], heights[right])
            con = mult * (right - left)
            if con > mcon:
                mcon = con
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mcon