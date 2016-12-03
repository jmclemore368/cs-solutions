# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import collections

def find_num_words(word):
    c = collections.Counter(word)

    # Get all the counts of duplicates
    duplicates = [c[key] for key in c.iterkeys() if c[key] > 1]

    denominator = 1
    for d in duplicates:
        denominator *= math.factorial(d)

    print duplicates
    print "num: " + str(len(word)) + "!"
    print "denom: " + str(denominator)

    return math.factorial(len(word)) / denominator

def find_rank_util_possible_repetition(word, sorted_word, rank, index):

    #print "\nWord is: " + word
    #print "Sorted word is: " + sorted_word
    #print "Char to find is: " + word[index]

    if index == len(word) - 1:
        #print 'final answer is: ' + str(rank)
        return rank + 1

    i = 0
    while i < len(sorted_word):
        remaining_chars = sorted_word[:i] + sorted_word[i + 1:]
        #print "Looking at char " + str(i) + " of word " + sorted_word + ": " + sorted_word[i]
        #print "Is " + sorted_word[i] + " == " + word[index] + "?"
        if sorted_word[i] == word[index]:
            #print "Yes. Fix this character. Recurse on: " + remaining_chars
            return find_rank_util_possible_repetition(word, remaining_chars, rank, index + 1)
        else:
            num_words = find_num_words(remaining_chars)
            print "No. How many words can be made from " + remaining_chars + "?: " + str(num_words)
            rank += num_words

            while i < len(sorted_word) and sorted_word[i] == sorted_word[i + 1]:
                i += 1
        i += 1

def find_rank(word):

    sorted_word = ''.join(sorted(word))
    print 'sorted word is: ' + sorted_word
    return find_rank_util_possible_repetition(word, sorted_word, 0, 0)


num_cases = int(raw_input())
result = []
for i in range(num_cases):
    word = raw_input().strip().lower()
    #rint 'word is: ' + word
    rank = find_rank(word)
    result.append(rank)

for r in result:
    print r
