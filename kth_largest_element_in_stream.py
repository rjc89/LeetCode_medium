# https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/1029657/Python-heapq-solution-beats-98

from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.nums = nums
        self.heap = nums[:k]
        self.heap_size = len(self.heap)
        self.k = k
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            if i > self.heap[0]:
                heapq.heapreplace(self.heap, nums[i])
                
    def add(self, val: int) -> int:
        if self.heap_size < self.k:
            heapq.heappush(self.heap, val)
            self.heap_size += 1
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
            
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

s = KthLargest(["KthLargest", "add", "add", "add", "add", "add"],
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]])

print(s.add(["KthLargest", "add", "add", "add", "add", "add"],
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]))