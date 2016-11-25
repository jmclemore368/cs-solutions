# https://leetcode.com/problems/word-ladder/


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        return self.breadthFirstSearch(beginWord, endWord, wordList)
            
    
    def breadthFirstSearch(self, beginWord, endWord, wordList):
        """
        Given some beginWord and endWord, we want to change beginWord 1 character at a time.
        Think of the transformation from beginWord -> endWord as a series of levels.
        Each level contains all possible transformations from the previous level that exist in wordList.
        Furthermore, no level contains words from any previous level. 
        With that said, we see this problem is essentially a BFS.
        If a transformation is endWord is possible, we will always eventually converge to it.
        
            hit*        Level 1
             |
            hot         Level 2
             |
          dot, lot      Level 3
           |    |
          dog   log     Level 4
           |
          cog*          Level 5

        """
        visited = set()
        ladder = 1 
        current_level = 1  
        next_level = 0 
        
        q = collections.deque()
        q.append(beginWord)
        
        while current_level:
            head = q.popleft()
            visited.add(head)
            current_level -= 1
            
            # For each character in word, we will replace it with every character in the alphabet.
            # Then, we see if this newWord exists in the set. If so, we have found a transformation.
            for i in range(len(head)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = head[:i] + c + head[i+1:]
                    
                    # If newWord is the endWord, we are done.
                    if newWord == endWord:
                        return ladder + 1
                    
                    # If newWord is in wordList, add it to q so that we may further BFS on it.
                    if newWord in wordList and newWord not in visited:
                        next_level += 1
                        q.append(newWord)
                        visited.add(newWord)
                        
            # When current_level = 0, then we have exhausted checking for all possible transformations for this level.
            # Now, we must check for all possible transformations for the next level.
            if current_level == 0:
                current_level = next_level
                next_level = 0
                ladder += 1
        
        # If we reach here, then current_level == 0 and no transformation was found.
        return current_level
        
                
        





                
