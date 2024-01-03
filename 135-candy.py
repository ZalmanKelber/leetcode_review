# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        ordered_ratings = sorted([i for i in range(len(ratings))], key=lambda x: ratings[x])
        for child in ordered_ratings:
            lt, rt = child, child
            while rt < len(ratings) - 1 and ratings[rt + 1] > ratings[rt] and candies[rt + 1] <= candies[rt]:
                candies[rt + 1] = candies[rt] + 1
                rt += 1
            while lt > 0 and ratings[lt - 1] > ratings[lt] and candies[lt - 1] <= candies[lt]:
                candies[lt - 1] = candies[lt] + 1
                lt -= 1
        return sum(candies)