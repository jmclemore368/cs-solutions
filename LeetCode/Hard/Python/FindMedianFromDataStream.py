# https://leetcode.com/problems/find-median-from-data-stream/


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # The goal is to maintain 2 heaps of equal size (at most 1 difference in size for odd num elements).
        # Min_heap contains the greater half. Max_heap contains the lower half.
        # For example, given [1,2,3,4,5,6]. 
        # You want [4,5,6] to be the elements of the min heap and [3,2,1] to be those of the max_heap
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return
        
        # If num <= root of min_heap, it should go in the max_heap (lower half).
        if num <= self.min_heap[0]:
            
            # If the heaps have the same size, just put it directly in max_heap
            # For example: min_heap = [26, 35, 28, 40], max_heap = [19, 16, 14, 14]
            # For num = 17. Note that 26 is the smallest element of the upper half of elements. 
            # Since 17 < 26, 17 doesn't belong in the upper half of elements.
            if len(self.max_heap) <= len(self.min_heap):
                heapq.heappush(self.max_heap, num * -1)
                
            # Else, max_heap has more elements than min_heap. We need to balance the heap sizes.
            # For example: min_heap = [26, 35, 28, 40], max_heap = [19, 16, 14, 14, 8]
            # For num = 25. Note 25 > 19. Therefore, it should actually go in min_heap.
            # For num = 17. Note 17 < 19. Therefore, we do a switch: put 19 into min_heap, and 17 into max_heap.
            else:
                if num > (self.max_heap[0] * -1):
                    heapq.heappush(self.min_heap, num)
                else:
                    top = heapq.heappop(self.max_heap) * -1  
                    heapq.heappush(self.min_heap, top)
                    heapq.heappush(self.max_heap, num * -1)
                    
        # Else, num > root of min_heap. In this case, it belongs to the min_heap (upperhalf).
        else:
            
            # If the heaps have the same size, just put it directly in min_heap
            # For example: min_heap = [26, 35, 28, 40], max_heap = [19, 16, 14, 14]
            # For num = 37, it needs to go into the min_heap. 
            if len(self.min_heap) <= len(self.max_heap):
                heapq.heappush(self.min_heap, num)
                
            # Else, min_heap has more elements than max_heap. We need to balance the heap sizes.
            # For example: min_heap = [26, 35, 37, 28, 40], max_heap = [19, 16, 14, 14, 8]
            # Since num is > root of min_heap, root of min_heap gets kicked out to lower half (max_heap) every time.
            else:
                top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, top * -1)
                heapq.heappush(self.min_heap, num)
                

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            min_top = float(self.min_heap[0])
            max_top = float(self.max_heap[0] * -1)
            return ((min_top + max_top) / 2)
        else:
            if len(self.min_heap) > len(self.max_heap):
                min_top = float(self.min_heap[0])
                return min_top
            else:
                max_top = float(self.max_heap[0] * -1)
                return max_top
           

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
