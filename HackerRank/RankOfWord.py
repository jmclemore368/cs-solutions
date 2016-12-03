# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import collections

def find_num_permutations(word):
    """
    The number of permutations of a string of length n is: n! / (c1! * c2 * ... * cn!)
    Where ck gives the number of occurrences of each distinct character.
    
    For example, given "SUCCSS", the number of permutations is then:
          6!
     ------------
     3! * 2! * 1!
    
    """
    c = collections.Counter(word)
    numerator = math.factorial(len(word))
    denominator = 1 
    for key in c.iterkeys():
        denominator *= math.factorial(c[key])
    return numerator / denominator

def find_rank_util_possible_repetition(word, sorted_word, rank, index):
    if index == len(word) - 1:
        return rank + 1

    i = 0
    while i < len(sorted_word):
        remaining_chars = sorted_word[:i] + sorted_word[i + 1:]

        if sorted_word[i] == word[index]:
            return find_rank_util_possible_repetition(word, remaining_chars, rank, index + 1)
        else:
            rank += find_num_permutations(remaining_chars)
            # If the next chars are the same, then they will not create any new words. Skip over these.
            while i < len(sorted_word) and sorted_word[i] == sorted_word[i + 1]:
                i += 1
                
        i += 1

        
def find_rank(word):
    sorted_word = ''.join(sorted(word))
    return find_rank_util_possible_repetition(word, sorted_word, 0, 0)


num_cases = int(raw_input())
result = []
for i in range(num_cases):
    word = raw_input().strip().lower()
    rank = find_rank(word)
    result.append(rank)

for r in result:
    print r
