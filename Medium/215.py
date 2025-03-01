class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        headp = []
        for num in nums:
            heapq.heappush(heap, num)

            if(len(heap) > k):
                headpq.popback(headp)
        return headp[0]
