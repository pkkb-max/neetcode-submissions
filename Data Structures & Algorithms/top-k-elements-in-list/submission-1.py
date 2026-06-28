class Element:
    def __init__(self, value, count):
        self.value = value
        self.count = count

    def __lt__(self, other):
        return self.count < other.count
    
    def __repr__(self):
        return f"Element({self.value},{self.count})"

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        index = 0
        counts = {}
        elements = {}
        while index < len(nums):
            counts[nums[index]] = counts.get(nums[index], 0) + 1
            ele = Element(nums[index],counts[nums[index]])
            if ele.value in elements:
                elements[ele.value].count = ele.count
            elif len(heap) < k:
                heapq.heappush(heap, ele)
                elements[ele.value] = ele
            elif heap[0].count < counts[nums[index]]:
                del elements[heapq.heappop(heap).value]
                heapq.heappush(heap, ele)
                elements[ele.value] = ele
            heapq.heapify(heap)
            index+=1
        return [ele.value for ele in heap]