# https://leetcode.com/problems/fizz-buzz/


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [str(i) for i in range(1, n + 1)]
        
        for i in range(1, n + 1):
            s = []
            if i % 3 == 0: 
                s.extend(list("Fizz"))
            if i % 5 == 0: 
                s.extend(list("Buzz"))
            if s:
                result[i - 1] = ''.join(s)
                
        return result


'''
# Correct, but significantly slower due to more comparisons. 

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if (i % 15) == 0:
                result.append("FizzBuzz")
            elif (i % 3) == 0:
                result.append("Fizz")
            elif (i % 5) == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
'''
    
