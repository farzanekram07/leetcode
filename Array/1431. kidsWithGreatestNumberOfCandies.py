class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)
        return results
