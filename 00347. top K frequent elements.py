from typing import List
from collections import Counter
# solution 1
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        min_value = min(arr)
        max_value = max(arr)

        range_of_element = (max_value - min_value) + 1
        count = [0] * range_of_element

        for num in arr:
            count[num - min_value] += 1

        freq_num_pairs = []
        for idx, freq in enumerate(count):
            num = idx + min_value
            freq_num_pairs.append((freq, num))

        freq_num_pairs.sort(reverse=True)  # highest frequency first
        result = [num for freq, num in freq_num_pairs[:k]]
        return result
    
# solution 2
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        count = Counter(arr)
        return [item for item, freq in count.most_common(k)]