# Understand 
# INPUT given a sequence of words wirrten in the alien language, and the order of alphabet
# OUTPUT return True if and only if the given words are sorted in the alien lang ...

# Example 
# words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# return True 

# Brute Force, Time O(N*L*K), Space O(1)
# class Solution:
#     def isAlienSorted(self, words, order:str) -> bool:
#         for i in range(len(words)-1):
#             word1 = words[i]
#             word2 = words[i+1]
#             for j in range(min(len(word1), len(word2))):
#                 rank1 = order.index(word1[j])
#                 rank2 = order.index(word2[j])

#                 if rank1 > rank2:
#                     return False
#                 elif rank1 < rank2:
#                     break
#             else:
#                 if len(word1) > len(word2):
#                     return False 
#         return True

# s = Solution()
# print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))

# Bottlenack > we use index() to search and this is cost time 

# Optimize > use hash table (map)

# code 
class Solution:
    def isAlienSorted(self, words, order:str) -> bool:
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                rank1 = order_map[(word1[j])]
                rank2 = order_map[(word2[j])]

                if rank1 > rank2:
                    return False
                elif rank1 < rank2:
                    break
            else:
                if len(word1) > len(word2):
                    return False 
        return True


# Test Case & Complixity, Time O(NK), Space O(K)
s = Solution()
print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
