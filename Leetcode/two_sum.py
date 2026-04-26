from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            current = nums[i]
            needed = target - current

            if needed in h:
                return [h[needed], i]
            
            h[current] = i

        return []            
