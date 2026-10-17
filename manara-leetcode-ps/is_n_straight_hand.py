# Understand 
# INPUT int array of cands, int groupSize 
# OUTPUT return ture if she can rearrage the cand or false otheewise

# Example 
# hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# return True

# Brute Force, Time O(n^2), Space O(n)
# class Solution:
#     def isNStraightHand(self, hand, groupSize) -> bool:
#         if (len(hand) % groupSize) != 0:
#             return False
#         sorted_hand = sorted(hand)
#         while sorted_hand:
#             first = sorted_hand[0]
                
#             for card in range(first, first + groupSize):
#                 if card not in sorted_hand:
#                     return False

#                 sorted_hand.remove(card)
#         return True

# Bottleneck > due to search and delete cost O(n) and repate that on n time of cards

# Optimize > use hash tables ( Map )

# code 
class Solution:
     def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        for card in sorted(count):
            if count[card] == 0:
                continue

            while count[card] > 0:
                for next_card in range(card, card + groupSize):
                    if count.get(next_card, 0) == 0:
                        return False

                    count[next_card] -= 1

        return True

# Test Cases & Complixity, Time O(n+ulogu), O(u)
s = Solution()
print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
