# https://leetcode.com/submissions/detail/83163467/


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Map character frequencies.
        mapping = {}
        for char in s:
            if not char in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1
       
        # Push frequencies into max-heap to obtain desired ordering.
        heap = []
        for char, freq in mapping.iteritems():
            
            # Multiply by -1 to invert, since heapq is min-heap by default.
            heapq.heappush(heap, (freq * -1, char))  
            
            
        # Pop all values from heap to get final result.
        result = []
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(freq * -1 * char)  # Multiple by -1 again to revert 
            
        return ''.join(result)
        
        
 
