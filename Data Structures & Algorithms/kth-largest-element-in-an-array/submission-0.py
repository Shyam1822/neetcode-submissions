class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # with sorting
        return sorted(nums)[::-1][k-1]
        